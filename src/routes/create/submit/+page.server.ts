import type { PageServerLoad, Actions } from './$types';
import { redirect, error } from '@sveltejs/kit';
import { submit, return_tempquest_data } from '$lib/server/createaquest';
export const load: PageServerLoad = async ({ url, cookies }) => {
  const email = cookies.get("email");
  if (!email) throw error(400, "Missing email cookie");

  const tempquest = await return_tempquest_data(email);

  if (tempquest.question === 0) {
    throw redirect(303, '/create/quest_storage');
  }

  return { tempquest: tempquest}
};

export const actions: Actions = {
    default: async ({ request, cookies }) => {
        const email = cookies.get("email");
        if (!email) throw error(400, "Missing email cookie");
        const formData = await request.formData();

        //CHANGE
        const info = Object.fromEntries(formData) as { fake: string; };
        //CHANGE

        const questID = await submit(email);
        throw redirect(302, '/dashboard');
        
    }
};