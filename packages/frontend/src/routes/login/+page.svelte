<script lang="ts">
	import { Input } from '@components';
	import { Header, Text } from '@ui';
	import { Button, Flex, Frame } from 'sk-clib';
	let selected = '';

	async function onsubmit(event: Event) {
		event.preventDefault(); // Stop default behavior

		const formData = Object.fromEntries(new FormData(event.target as HTMLFormElement));

		console.log('Submitting', formData);
	}
</script>

<Flex col fill class="mt-20">
	<!-- Header -->
	<Header xxl bold class="ml-4 sm:ml-0">Sign In</Header>
	<Text lg class="ml-4 opacity-80 sm:ml-0">Welcome back to DriveHenrico!</Text>

	<!-- Form Section -->
	<Frame flex col fill class="mt-2 box-border rounded-t-2xl bg-white p-6 dark:bg-[#2F2F42]">
		<form class="box-border flex size-full flex-col" {onsubmit}>
			<Input class="mb-4" type="text" id="name_input" name="name" label="Full Name" />
			<Input class="mb-4" type="email" id="email_input" name="email" label="Email" />
			<Input
				type="password"
				class="mb-[12px]"
				id="password_input"
				label="Password"
				name="password"
			/>

			<Button type="submit" class="mb-4 cursor-pointer rounded-xl text-white">Sign In</Button>

			<Flex row center class="gap-2">
				<Text lg class="opacity-80">Don't have an account?</Text>
				<a href="/register" class="text-primary font-bold underline">Sign Up</a>
			</Flex>
			<Flex row center class="gap-2">
				<Text lg class="opacity-80">Forgot Password?</Text>
				<a href="/forget " class="text-primary font-bold underline">Click here</a>
			</Flex>
		</form>
	</Frame>
</Flex>
