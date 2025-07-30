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
	const { _challenge_state } = ctx;

	if (error) {
		console.error(error, data);
		return;
	}	

	const { challenge_id } = data;
	_challenge_state.id = challenge_id;
}
