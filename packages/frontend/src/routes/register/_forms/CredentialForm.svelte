<script lang="ts">
	// === Components ===
	import { Text } from '@ui';
	import { Input } from '@components';
	import { Button, Flex } from 'sk-clib';

	// === Context ===
	import { getStepsCtx } from '@components/steps/ctx.svelte';
	let { _helpers } = getStepsCtx();
</script>

<form class="box-border flex size-full flex-col" onsubmit={_helpers.next}>
	<Input class="mb-4" type="email" id="email_input" name="email" label="Email" />
	<Input type="password" class="mb-8" id="password_input" label="Password" name="password" />

	<Button type="submit" class="mb-4 cursor-pointer rounded-xl text-white">Sign Up</Button>

	<Flex row center class="gap-2">
		<Text lg class="opacity-80">Already have an account?</Text>
		<a href="/login" class="text-primary font-bold underline">Sign In</a>
	</Flex>
</form>
