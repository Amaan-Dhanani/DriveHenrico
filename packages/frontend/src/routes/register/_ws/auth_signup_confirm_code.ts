import type { WebsocketError } from '@lib/types';
import { CapacitorCookies } from '@capacitor/core';

type ConfirmCodeResponseType = {
	token?: string;
};

export async function auth_signup_confirm_code(
	_: WebsocketError,
	data: ConfirmCodeResponseType
) {

	const { token } = data;
	if (!token) throw new Error('No token present');

	console.info(`New token setting: ${token}`);

	await CapacitorCookies.setCookie({
		key: 'token',
		value: token
	});
}
