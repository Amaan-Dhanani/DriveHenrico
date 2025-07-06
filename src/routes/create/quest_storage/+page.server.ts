import type { PageServerLoad } from './$types';
import { error } from '@sveltejs/kit';
import { return_tempquest_data } from '$lib/server/createaquest';

export const load: PageServerLoad = async ({ url, cookies }) => {
  const email = cookies.get("email");
  if (!email) throw error(400, "Missing email cookie");


  const tempquest = await return_tempquest_data(email);

  return { tempquest: tempquest}
};