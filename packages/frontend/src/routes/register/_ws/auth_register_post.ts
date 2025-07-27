import type { WebsocketError } from '@lib/types';
import { getRegisterCtx } from '../ctx.svelte';

type PostResponseType = {
	verification_id?: string;
};

export async function auth_register_post(
	ctx: ReturnType<typeof getRegisterCtx>,
	error: WebsocketError,
	data: PostResponseType
) {
	const { _verification_state } = ctx;

	if (error) {
		console.error(error, data);
		return;
	}

	const { verification_id } = data;
	_verification_state.id = verification_id;
}
