import type { WebsocketError } from '@lib/types';
import { getLoginCtx } from '../ctx.svelte';

type PostResponseType = {
	challenge_id?: string;
};

export async function login_success(
	ctx: ReturnType<typeof getLoginCtx>,
	error: WebsocketError,
	data: PostResponseType
) {
<<<<<<< Updated upstream:packages/frontend/src/routes/register2/_ws/login_success.ts
=======
	const { _challenge_state } = ctx;

>>>>>>> Stashed changes:packages/frontend/src/routes/login/_ws/auth_login_post.ts
	if (error) {
		console.error(error, data);
		return;
	}	

<<<<<<< Updated upstream:packages/frontend/src/routes/register2/_ws/login_success.ts
	const {method, email, password} = ctx._session_initiate_state

	// Start Session Connection
	await ctx._state.session_ws?.connect();
	ctx._state.session_ws?.send('session:initiate', { method, email, password });
=======
	const { challenge_id } = data;
	_challenge_state.id = challenge_id;
>>>>>>> Stashed changes:packages/frontend/src/routes/login/_ws/auth_login_post.ts
}
