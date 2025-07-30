import type { WebsocketError } from '@lib/types';
import { getRegisterCtx } from '../ctx.svelte';

type PostResponseType = {
	challenge_id?: string;
};

export async function register_success(
	ctx: ReturnType<typeof getRegisterCtx>,
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
