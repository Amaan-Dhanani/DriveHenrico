export const email_regexp = /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$/;


const one_day = 60 * 60 * 24;

export const cookie_options = {
	httpOnly: true,
	secure: true,
	path: "/",
	maxAge: one_day
} as const;



import { connect_to_db } from "./db";
import { error } from "@sveltejs/kit";

export async function get_user_id(email: string): Promise<string | null> {
	const mongoose = await connect_to_db();
	if (!mongoose || !mongoose.connection.db) throw error(500, "Database connection failed");

	const user = await mongoose.connection.db.collection('users').findOne({ email });
	if (!user) {
		console.log("User not found for email:", email);
		return null;
	}
	return user._id.toString();
}