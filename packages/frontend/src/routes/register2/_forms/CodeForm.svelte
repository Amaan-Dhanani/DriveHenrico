<script lang="ts">
	// === Core ===
	import { onMount } from 'svelte';

	// === Components ===
	import { Text } from '@ui';
	import { Button } from 'sk-clib';
	import { TextRedactor, CodeInput } from '@components';

	// === Context ===
	import { getLoginCtx } from '../ctx.svelte';
	import { getStepsCtx } from '@components/steps/ctx.svelte';
	let { _helpers } = getStepsCtx();
<<<<<<< Updated upstream:packages/frontend/src/routes/register2/_forms/CodeForm.svelte
	const { _state, _verification_state, _session_initiate_state } = getLoginCtx();
=======
	const { _state, _challenge_state } = getLoginCtx();
>>>>>>> Stashed changes:packages/frontend/src/routes/login/_forms/CodeForm.svelte

	onMount(() => {
		const { email, password } = _helpers.mergeSteps(
			'credential',
		);

		_session_initiate_state.setAll({ method: 'email', email, password });

		
		_state.session_ws?.send("session:initiate", {method: "email", email, password})
	});

	async function onsubmit(event: Event) {
		event.preventDefault();

		_helpers.captureForm(event);
		const { code } = _helpers.mergeSteps('code');

		if (!code) throw new Error('Missing code');
		if (!_challenge_state.id) throw new Error('Missing Challenge');

<<<<<<< Updated upstream:packages/frontend/src/routes/register2/_forms/CodeForm.svelte
		_state.session_ws?.send('session:verify', {
			challenge_id: _verification_state.id,
			value: code
=======
		_state.ws?.send('auth:login:confirm_code', {
			id: _challenge_state.id,
			code
>>>>>>> Stashed changes:packages/frontend/src/routes/login/_forms/CodeForm.svelte
		});
	}
</script>

<form class="box-border flex size-full flex-col gap-4" {onsubmit}>
	<span class="text-center dark:text-white">Verify Code</span>

	<Text class="text-center text-sm"
		>We just emailed a code to <TextRedactor
			text={_helpers.mergeSteps('credential').email}
			class="text-primary"
		/>. Please check your inbox. If it isn't found, it could be in your spam.</Text
	>
	<CodeInput classWrapper="pb-[3px]" name="code" />

	<Button type="submit" class="mb-4 cursor-pointer rounded-xl text-white">Continue</Button>
</form>
