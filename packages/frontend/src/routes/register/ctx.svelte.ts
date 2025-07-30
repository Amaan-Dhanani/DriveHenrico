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
	public register_ws = $state<Websocket | undefined>();
	public session_ws = $state<Websocket | undefined>();
	public step = $state<Step>('credential');
	public error = $state<string | undefined>(undefined);
	public registered = $state<boolean>(false);
}

export function createRegister() {
	const _state = new State();
	const _challenge_state = new ChallengeState();
	const _session_initiate_state = new SessionInitiateState();

	return { _state, _challenge_state, _session_initiate_state };
}

export function getRegisterData() {
	const NAME = 'register-ctx' as const;
	return {
		NAME
	};
}

export function setRegisterCtx() {
	const { NAME } = getRegisterData();

	const register = {
		...createRegister()
	};

	setContext(NAME, register);

	return {
		...register
	};
}

type RegisterGetReturn = ReturnType<typeof setRegisterCtx>;
export function getRegisterCtx() {
	const { NAME } = getRegisterData();
	return getContext<RegisterGetReturn>(NAME);
}
