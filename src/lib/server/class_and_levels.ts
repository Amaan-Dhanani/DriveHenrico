import { connect_to_db } from "./db";
import { error } from "@sveltejs/kit";
import { get_user_id } from "./utils";
import { ObjectId } from "mongodb";


export async function new_class(email: string): Promise<string> {
	const mongoose = await connect_to_db();
	if (!mongoose || !mongoose.connection.db) throw error(500, "Database connection failed");
    console.log("Connected to database");

	const _idStr = await get_user_id(email);
	if (!_idStr) throw error(404, "User ID not found");

	const userObjectId = new ObjectId(_idStr);
	const db = mongoose.connection.db;

	const tempCollection = db.collection('classes');

	// Create a new document
	const newDoc = {
		user_id: userObjectId.toString(),
		created_at: new Date(),
	};

	const result = await tempCollection.insertOne(newDoc);

	if (!result.acknowledged) throw error(500, "Failed to insert document");

	return result.insertedId.toString();
}


export async function lvl_redirect(email: string, page_num: number): Promise<void> {
	const mongoose = await connect_to_db();
	if (!mongoose || !mongoose.connection.db) throw error(500, "Database connection failed");

	const _idStr = await get_user_id(email);
	if (!_idStr) throw error(404, "User ID not found");

	const _id = new ObjectId(_idStr);
	const collection = mongoose.connection.db.collection('achievements');

	await collection.updateOne(
		{ _id },
		{ $set: { level: page_num } },
		{ upsert: true }
	);
}

export async function get_lvl(email: string): Promise<number> {
  const mongoose = await connect_to_db();
  if (!mongoose || !mongoose.connection.db) throw error(500, "Database connection failed");

  const _idStr = await get_user_id(email);
  if (!_idStr) throw error(404, "User ID not found");

  const _id = new ObjectId(_idStr);
  const collection = mongoose.connection.db.collection('achievements');

  const doc = await collection.findOne({ _id });
  if (!doc) throw error(404, "User achievements not found");

  // Assuming 'level' field exists and is a number
  if (typeof doc.level !== 'number') throw error(500, "Level data invalid or missing");

  return doc.level;
}
