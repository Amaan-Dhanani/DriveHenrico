import { getContext, setContext } from 'svelte';
import type { Step } from './types';
import { Websocket } from '@utils';

class VerificationState {
    public id = $state<string | undefined>();
}

class UserInput {
    public email = $state<string | undefined>();
    public password = $state<string | undefined>();
	public name = $state<string | undefined>();
    public account_type = $state<string | undefined>();
    public code = $state<string | undefined>();
}

class State {
	public ws = $state<Websocket | undefined>();
	public step = $state<Step>("credential");
	public error = $state<string | undefined>(undefined);
}

export function createRegister() {
	const _state = new State();
    const _user_input = new UserInput();
    const _verification_state = new VerificationState();

	return { _state, _user_input, _verification_state };
}

export function getRegisterData() {
	const NAME = 'login-ctx' as const;
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
