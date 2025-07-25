<script lang="ts">
	import { Websocket } from '@utils';
	import { Header, Text } from '@ui';
	import { Flex, Frame } from 'sk-clib';
	import { onMount } from 'svelte';

	import { setRegisterCtx } from './ctx.svelte';
	import { AccountTypeForm, CodeForm, CredentialForm, Success } from './_forms';
	import { CapacitorCookies } from '@capacitor/core';

	let { _state, _verification_state } = setRegisterCtx();

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

		type PostResponseType = {
			verification_id?: string;
		};

		_state.ws.on('auth:signup:post', async (error, data: PostResponseType) => {
			if (error) {
				console.error(error, data)
				return
			}

			const { verification_id } = data;
			_verification_state.id = verification_id;
		});

		type ConfirmCodeResponseType = {
			token?: string
		}

		_state.ws.on('auth:signup:confirm_code', async(error, data: ConfirmCodeResponseType) => {
			const {token} = data;
			if (!token) throw new Error("No token present");
			
			console.log("Yippie you have a new token!")

			await CapacitorCookies.setCookie({
				"key": "token",
				"value": token
			})
			
		})
	});
</script>

<Flex col fill class="mt-20">
	<!-- Header -->
	<Header xxl bold class="ml-4 sm:ml-0">Sign Up</Header>
	<Text lg class="ml-4 opacity-80 sm:ml-0">{stepTextMap[_state.step]}</Text>

	<!-- Form Section -->
	<Frame flex col fill class="mt-2 box-border rounded-t-2xl p-6 bg-white dark:bg-[#2F2F42]">
		{_state.step}
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
