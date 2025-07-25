<script lang="ts">

	// === Core ===
	import { Websocket } from '@utils';
	import { onMount } from 'svelte';

	// === Components ===
	import { Header, Text } from '@ui';
	import { Flex, Frame } from 'sk-clib';
	import { AccountTypeForm, CodeForm, CredentialForm, Success } from './_forms';

	// === Websocket ===
	import {auth_signup_post, auth_signup_confirm_code} from "./_ws"

	// === Context ===
	import { setRegisterCtx } from './ctx.svelte';
	let { _state } = setRegisterCtx();

	const stepTextMap: Record<string, string> = {
		credential: 'Enter your desired email and password to start your journey!',
		type: 'Enter your name and your account type to continue with the registration process.',
		code: 'Last Step! All we have to do is verify your information.',
	};

	$effect(() => {
		console.log(_state.step);
	});

	onMount(async () => {
		_state.ws = new Websocket('/auth/signup');
		await _state.ws.connect();
		_state.ws.on('auth:signup:post', auth_signup_post)
		_state.ws.on('auth:signup:confirm_code', auth_signup_confirm_code)
	});
	
</script>

<Flex col fill class="mt-20">
	<!-- Header -->
	<Header xxl bold class="ml-4 sm:ml-0">Sign Up</Header>
	<Text lg class="ml-4 opacity-80 sm:ml-0">{stepTextMap[_state.step]}</Text>

	<!-- Form Section -->
	<Frame flex col fill class="mt-2 box-border rounded-t-2xl p-6 bg-white dark:bg-[#2F2F42]">
		{#if _state.step == 'credential'}
			<CredentialForm />
		{:else if _state.step == 'type'}
			<AccountTypeForm />
		{:else if _state.step == 'code'}
			<CodeForm />
		{:else if _state.step == "success"}
			<Success/>
		{/if}
	</Frame>
</Flex>
