import type { PageServerLoad, Actions } from './$types';
import { redirect, error } from '@sveltejs/kit';
import { lvl_redirect } from '$lib/server/class_and_levels';

export const actions: Actions = {
    default: async ({ request, url, cookies }) => {
        const pageName = Number(url.pathname.slice(-1)) || -9;
        const email = cookies.get("email");
        if (!email) throw error(400, "Missing email cookie");
        const formData = await request.formData();

        // CHANGE: Access the 'res' property, not the whole object
        const res1 = Object.fromEntries(formData) as { res: string };
        
        if (res1.res === "win") {
            console.log("win");
            await lvl_redirect(email, pageName)
            throw redirect(302, '/play_storage');
        } else {
            console.log("lose");
            throw redirect(302, '/play_storage');
        }
    }
};
