import { connect_to_db } from "./db";
import { error } from "@sveltejs/kit";
import { get_user_id } from "./utils";
import { ObjectId } from "mongodb";
import { redirect } from '@sveltejs/kit';
import randomstring from "randomstring"

export async function return_tempquest_data(email: string): Promise<any> {
	const mongoose = await connect_to_db();
	if (!mongoose || !mongoose.connection.db) throw error(500, "Database connection failed");

	const _idStr = await get_user_id(email);
	if (!_idStr) throw error(404, "User ID not found");

	const _id = new ObjectId(_idStr);
	const collection = mongoose.connection.db.collection("tempquest");

	const doc = await collection.findOne({ _id });
	if (!doc) { return "" };

	return {
		...doc,
		_id: doc._id.toString(),
	};
}


export async function wrong_question_access(email: string, page_num: number): Promise<void> {
	const mongoose = await connect_to_db();
	if (!mongoose || !mongoose.connection.db) throw error(500, "Database connection failed");

	const _idStr = await get_user_id(email);
	if (!_idStr) throw error(404, "User ID not found");

	const _id = new ObjectId(_idStr);
	const collection = mongoose.connection.db.collection('tempquest');

	const doc = await collection.findOne({ _id });
	if (!doc) {
		throw redirect(303, `/create/main`);
	};
	const storedQuestion = doc.question;
	if (page_num >= storedQuestion + 2) {
		throw redirect(303, `/create/question${storedQuestion + 1}`);
	}


}

export async function tempquest_pass(email: string, info: Record<string, any>): Promise<void> {
	const mongoose = await connect_to_db();
	if (!mongoose || !mongoose.connection.db) throw error(500, "Database connection failed");

	const _idStr = await get_user_id(email);
	if (!_idStr) throw error(404, "User ID not found");

	const _id = new ObjectId(_idStr);
	const collection = mongoose.connection.db.collection('tempquest');

	// First: push data
	await collection.updateOne(
		{ _id },
		{ $set: info },
		{ upsert: true }
	);

	// Then: re-fetch document to determine which question field exists
	const updatedDoc = await collection.findOne({ _id });

	let questionNumber = 0;
	if (updatedDoc) {
		for (let i = 10; i >= 1; i--) {
			if (`question_${i}` in updatedDoc) {
				questionNumber = i;
				break;
			}
		}
	}

	// Update the question field after checking
	await collection.updateOne(
		{ _id },
		{ $set: { question: questionNumber } }
	);
}


export async function submit(email: string): Promise<{ gen_id: string }> {
	const mongoose = await connect_to_db();
	if (!mongoose || !mongoose.connection.db) throw error(500, "Database connection failed");

	const _idStr = await get_user_id(email);
	if (!_idStr) throw error(404, "User ID not found");

	const _id = new ObjectId(_idStr);
	const db = mongoose.connection.db;

	const tempCollection = db.collection('tempquest');
	const questsCollection = db.collection('quests');
	const achievementsCollection = db.collection('achievements');

	// Get the document from tempquest
	const tempDoc = await tempCollection.findOne({ _id });
	if (!tempDoc) throw error(404, "Temporary document not found");

	// Remove the original _id so MongoDB generates a new one
	const { _id: _, ...docData } = tempDoc;

	const gen_id = randomstring.generate({
		length: 6,
		charset: "alphabetic"
	}).toUpperCase();

	// Add created_at and user ID to the new document
	const newQuest = {
		...docData,
		userid: _idStr,
		id: gen_id,
		created_at: new Date()
	};

	// Insert into quests collection
	const insertResult = await questsCollection.insertOne(newQuest);

	// Delete the original tempquest document
	await tempCollection.deleteOne({ _id });

	// Update achievements collection
	const updateResult = await achievementsCollection.updateOne(
		{ userid: _idStr },
		{
			$inc: { quest_created: 1 },
			$setOnInsert: { created_at: new Date() }
		},
		{ upsert: true }
	);

	// Return both mongo ID and gen_id
	return {
		gen_id
	};
}