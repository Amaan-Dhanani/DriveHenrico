import { redirect } from "@sveltejs/kit";
import type { Actions } from "./$types";

export const actions: Actions = {
	default: async (event) => {
		const cookieOptions = { path: '/' }; // Ensure cookies are removed from root path
		event.cookies.delete("auth-token", cookieOptions);
		event.cookies.delete("email", cookieOptions);
		event.cookies.delete("name", cookieOptions);
		throw redirect(301, "/");
	}
};
