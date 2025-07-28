<script lang="ts">
	// === Core ===
	import { Websocket } from '@utils';
	import { onMount } from 'svelte';

	// === Components ===
	import { Header, Text } from '@ui';
	import { Flex, Frame } from 'sk-clib';
	import { CodeForm, CredentialForm, Success } from './_forms';

	// === Websocket ===
	import { auth_login_post, auth_login_confirm_code } from './_ws';

	// === Context ===
	import { setLoginCtx } from './ctx.svelte';
	import { Steps } from '@components';
	import type { StepsHelpers } from '@components/steps/ctx.svelte';

	let ctx = setLoginCtx();
	const _state = ctx._state;

	let step_helper: StepsHelpers | undefined = $state(undefined);

	const stepTextMap: Record<string, string> = {
		credential: 'Let\'s hit the road! All you gotta to is log in to DriveHenrico!',
		code: 'Well, that\'s not all. We also have to verify your information.'
	};

	$effect(() => {
		if (!step_helper) return;
		if (_state.loggedin) {
			step_helper.ctx.step = step_helper.get_step_idx('done');
		}
	});

	onMount(async () => {
		_state.ws = new Websocket('/auth/login');
		await _state.ws.connect();

		_state.ws.on('auth:login:post', (error, data) => auth_login_post(ctx, error, data));
		_state.ws.on('auth:login:confirm_code', (error, data) =>
			auth_login_confirm_code(ctx, error, data)
		);

		_state.ws.onerror = (error, data) => {
			console.error('Oh no... its broken...', error, data);
		};
	});

	const steps = [
		{ name: 'credential', component: CredentialForm },
		{ name: 'code', component: CodeForm },
		{ name: 'done', component: Success }
	];
</script>

<Flex col fill class="mt-20">
	<!-- Header -->
	<Header xxl bold class="ml-4 sm:ml-0">Sign In</Header>
	<Text lg class="ml-4 opacity-80 sm:ml-0">{stepTextMap[_state.step]}</Text>

	<!-- Form Section -->
	<Frame flex col fill class="mt-2 box-border rounded-t-2xl bg-white p-6 dark:bg-[#2F2F42]">
		<Steps {steps} bind:helper={step_helper} />
	</Frame>
</Flex>
