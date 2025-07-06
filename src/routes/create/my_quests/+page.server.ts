// src/routes/quests/+page.server.ts
import type { PageServerLoad } from './$types';
import { get_user_id } from '$lib/server/utils';
import { connect_to_db } from '$lib/server/db'; // Adjust path as needed
import { error } from '@sveltejs/kit';
import { return_tempquest_data } from '$lib/server/createaquest'; // Assuming this import was missing

export const load: PageServerLoad = async ({ cookies }) => {
  const email = cookies.get('email');
  if (!email) throw error(400, 'Missing email cookie');

  const _idStr = await get_user_id(email);
  if (!_idStr) throw error(404, 'User ID not found');

  const mongoose = await connect_to_db();
  if (!mongoose || !mongoose.connection.db) throw error(500, 'Database connection failed');

  const db = mongoose.connection.db;
  const questsCollection = db.collection('quests');

  const quests = await questsCollection
    .find({ userid: _idStr })
    .project({ quest_title: 1, created_at: 1, id: 1, _id: 0 })
    .toArray();

  const tempquest = await return_tempquest_data(email);

  return {
    quests,
    tempquest
  };
};
