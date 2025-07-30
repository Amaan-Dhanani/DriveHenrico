/* eslint-disable @typescript-eslint/no-explicit-any */
import { getContext, setContext } from 'svelte';
import type { Step } from './types';
import { Websocket } from '@utils';

class ChallengeState {
	public id = $state<string | undefined>();
}

class State {
	public session_ws = $state<Websocket | undefined>();
	public step = $state<Step>('credential');
	public error = $state<string | undefined>(undefined);
	public loggedin = $state<boolean>(false);
}

export function createLogin() {
	const _state = new State();
	const _challenge_state = new ChallengeState();

	return { _state, _challenge_state };
}

export function getLoginData() {
	const NAME = 'login-ctx' as const;
	return {
		NAME
	};
}

export function setLoginCtx() {
	const { NAME } = getLoginData();

	const login = {
		...createLogin()
	};

	setContext(NAME, login);

	return {
		...login
	};
}

type LoginGetReturn = ReturnType<typeof setLoginCtx>;
export function getLoginCtx() {
	const { NAME } = getLoginData();
	return getContext<LoginGetReturn>(NAME);
}
