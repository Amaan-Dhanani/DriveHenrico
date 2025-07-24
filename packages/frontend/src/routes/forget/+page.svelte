<script lang="ts">
	import { Input, CodeInput } from '@components';
	import { Header, Text } from '@ui';
	import { Button, Flex, Frame } from 'sk-clib';
	let selected = '';
	
	async function onsubmit(event: Event) {
		event.preventDefault(); // Stop default behavior

		const formData = Object.fromEntries(new FormData(event.target as HTMLFormElement));
		
		console.log("Submitting", formData)
	}
</script>

<Flex col fill class="mt-20">
	<!-- Header -->
	<Header xxl bold class="ml-4 sm:ml-0">Forgot Password?</Header>
	<Text lg class="opacity-80 ml-4 sm:ml-0">Reset your password now!</Text>

	<!-- Form Section -->
	<Frame flex col fill class="mt-2 box-border rounded-t-2xl p-6 bg-white dark:bg-[#2F2F42]">
		<form class="box-border flex size-full flex-col" {onsubmit}>
			<Input class="mb-4" type="email" id="email_input" name="email" label="Enter your email below." />
			
			<Button type="submit" class="rounded-xl text-white cursor-pointer mb-4">Send Code</Button>

			<CodeInput classWrapper="pb-[3px]" name="code" />
			<p class="text-[#858597] text-[14px]">Verify the code below. DEV NOTE: THIS LOCKS MOBILE USERS TO THE NUMBERIC KEYBOARD!</p>
			<Button type="submit" class="rounded-xl text-white cursor-pointer mb-4">Verify Code</Button>


			<Flex row center class="gap-2">
				<Text lg class="opacity-80">Remember your password?</Text>
				<a href="/login" class="text-primary underline font-bold">Sign In</a>
			</Flex>
			<Flex row center class="gap-2">
				<Text lg class="opacity-80">Don't have an account?</Text>
				<a href="/register" class="text-primary underline font-bold">Sign Up</a>
			</Flex>
		</form>
	</Frame>
</Flex>
