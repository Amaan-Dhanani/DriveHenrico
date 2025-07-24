<script lang="ts">
	import { Text } from '@ui';
	import { Input } from '@components';
	import { Button, Flex } from 'sk-clib';
	import { getRegisterCtx } from '../ctx.svelte';

	let { _state, _user_input } = getRegisterCtx();

	type CredentialFormData = {
		email?: string;
		password?: string;
		name?: string;
	};

	async function onsubmit(event: Event) {
		event.preventDefault(); // Stop default behavior
		const formData: CredentialFormData = Object.fromEntries(
			new FormData(event.target as HTMLFormElement)
		);
		const { email, password, name } = formData;

		if (!email || !password || !name) {
			throw new Error('Missing email, password, or name');
		}

		// Update user input
		_user_input.name = name;
		_user_input.email = email;
		_user_input.password = password;

		// Prompt Step Change
		_state.step = 'type';
	}
</script>

<form class="box-border flex size-full flex-col" {onsubmit}>
	<Input class="mb-4" type="text" id="name_input" name="name" label="Full Name" />
	<Input class="mb-4" type="email" id="email_input" name="email" label="Email" />
	<Input type="password" class="mb-8" id="password_input" label="Password" name="password" />

	<Button type="submit" class="mb-4 cursor-pointer rounded-xl text-white">Sign Up</Button>

	<Flex row center class="gap-2">
		<Text lg class="opacity-80">Already have an account?</Text>
		<a href="/login" class="text-primary font-bold underline">Sign In</a>
	</Flex>

</form>
