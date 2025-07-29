import type { WebsocketError } from '@lib/types';
import { getLoginCtx } from '../ctx.svelte';

type PostResponseType = {
	verification_id?: string;
};

export async function login_success(
	ctx: ReturnType<typeof getLoginCtx>,
	error: WebsocketError,
	data: PostResponseType
) {
	if (error) {
		console.error(error, data);
		return;
	}	

	const {method, email, password} = ctx._session_initiate_state

	// Start Session Connection
	await ctx._state.session_ws?.connect();
	ctx._state.session_ws?.send('session:initiate', { method, email, password });
}
