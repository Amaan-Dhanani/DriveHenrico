<script lang="ts">
	// === Core ===
	import { Websocket } from '@utils';
	import { onMount } from 'svelte';

	// === Components ===
	import { Header, Text } from '@ui';
	import { Flex, Frame } from 'sk-clib';
	import { AccountTypeForm, CodeForm, CredentialForm, Success } from './_forms';

	// === Websocket ===
	import { auth_signup_post, auth_signup_confirm_code } from './_ws';

	// === Context ===
	import { setRegisterCtx } from './ctx.svelte';
	import { Steps } from '@lib/components';
	import type { StepsHelpers } from '@lib/components/steps/ctx.svelte';

	let ctx = setRegisterCtx();
	const _state = ctx._state;

	let step_helper: StepsHelpers | undefined = $state(undefined);

	const stepTextMap: Record<string, string> = {
		credential: 'Enter your desired email and password to start your journey!',
		type: 'Enter your name and your account type to continue with the registration process.',
		code: 'Last Step! All we have to do is verify your information.'
	};

	$effect(() => {
		if (!step_helper) return;
		if (_state.registered) {
			step_helper.ctx.step = step_helper.get_step_idx('done');
		}
	});

	onMount(async () => {
		_state.ws = new Websocket('/auth/signup');
		await _state.ws.connect();

		_state.ws.on('auth:signup:post', (error, data) => auth_signup_post(ctx, error, data));
		_state.ws.on('auth:signup:confirm_code', (error, data) =>
			auth_signup_confirm_code(ctx, error, data)
		);

		_state.ws.onerror = (error, data) => {
			console.error('Oh no... its broken...', error, data);
		};
	});

	const steps = [
		{ name: 'credential', component: CredentialForm },
		{ name: 'account_type', component: AccountTypeForm },
		{ name: 'code', component: CodeForm },
		{ name: 'done', component: Success }
	];
</script>

<Flex col fill class="mt-20">
	<!-- Header -->
	<Header xxl bold class="ml-4 sm:ml-0">Sign Up</Header>
	<Text lg class="ml-4 opacity-80 sm:ml-0">{stepTextMap[_state.step]}</Text>

	<!-- Form Section -->
	<Frame flex col fill class="mt-2 box-border rounded-t-2xl bg-white p-6 dark:bg-[#2F2F42]">
		<Steps {steps} bind:helper={step_helper} />
	</Frame>
</Flex>
