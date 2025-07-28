import type { WebsocketError } from '@lib/types';
import { CapacitorCookies } from '@capacitor/core';
import type { getLoginCtx } from '../ctx.svelte';

type ConfirmCodeResponseType = {
	token?: string;
};

export async function auth_login_confirm_code(
	ctx: ReturnType<typeof getLoginCtx>,
	error: WebsocketError,
	data: ConfirmCodeResponseType
) {

	const { token } = data;
	if (!token) throw new Error('No token present');

	console.info(`New token setting: ${token}`);

	await CapacitorCookies.setCookie({
		key: 'token',
		value: token
	});

	ctx._state.loggedin = true;
}
