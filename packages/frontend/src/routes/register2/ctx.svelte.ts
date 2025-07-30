/* eslint-disable @typescript-eslint/no-explicit-any */
import { getContext, setContext } from 'svelte';
import type { Step } from './types';
import { Websocket } from '@utils';

class ChallengeState {
	public id = $state<string | undefined>();
}

class SessionInitiateState {
	public method = $state<string | undefined>();
	public email = $state<string | undefined>();
	public password = $state<string | undefined>();

	public setAll(obj: any) {
		const { method, email, password } = obj;
		this.method = method;
		this.email = email;
		this.password = password;
	}
}

class State {
	public session_ws = $state<Websocket | undefined>();
	public step = $state<Step>('credential');
	public error = $state<string | undefined>(undefined);
	public loggedin = $state<boolean>(false);
}

export function createLogin() {
	const _state = new State();
<<<<<<< Updated upstream:packages/frontend/src/routes/register2/ctx.svelte.ts
	const _verification_state = new VerificationState();
	const _session_initiate_state = new SessionInitiateState();

	return { _state, _verification_state, _session_initiate_state };
=======
	const _challenge_state = new ChallengeState();

	return { _state, _challenge_state };
>>>>>>> Stashed changes:packages/frontend/src/routes/login/ctx.svelte.ts
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
