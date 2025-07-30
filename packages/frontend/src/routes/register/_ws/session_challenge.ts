import type { WebsocketError } from '@lib/types';
import { getRegisterCtx } from '../ctx.svelte';

type PostResponseType = {
    challenge_id?: string;
};

export async function session_challenge(
    ctx: ReturnType<typeof getRegisterCtx>,
    error: WebsocketError,
    data: PostResponseType
) {
    if (error) {
        console.error(error, data);
        return;
    }	

    ctx._challenge_state.id = data.challenge_id
    console.info("Saved challenge id", data.challenge_id)
}
