import { getContext, setContext } from 'svelte';
import type { Step } from './types';
import { Websocket } from '@utils';

class VerificationState {
	public id = $state<string | undefined>();
}

class State {
	public ws = $state<Websocket | undefined>();
	public step = $state<Step>('credential');
	public error = $state<string | undefined>(undefined);
	public registered = $state<boolean>(false);
}

export function createRegister() {
	const _state = new State();
	const _verification_state = new VerificationState();

	return { _state, _verification_state };
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
