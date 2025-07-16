<script lang="ts">
	import { Input, Dropdown, DropdownBtn } from '@components';
	import { Header, Text } from '@ui';
	import { Button, Flex, Frame } from 'sk-clib';

	async function onsubmit(event: Event) {
		event.preventDefault(); // Stop default behavior

		const formData = Object.fromEntries(new FormData(event.target as HTMLFormElement));

		console.log('Submitting', formData);
	}
</script>

<Flex col fill class="mt-20">
	<!-- Header -->
	<Header xxl bold>Get Started</Header>
	<Text lg class="opacity-80">Enter your details below to start your journey!</Text>
	<!-- Form Section -->
	<Frame flex col fill class="mt-2 box-border rounded-t-2xl p-6 dark:bg-[#2F2F42]">
			TO BE DISPLAYED, IF YOU ARE LOGGED IN
		<form class="flex flex-row items-end gap-4 rounded-t-xl bg-white px-6 dark:bg-[#2F2F42]">
			<div class="flex-1">
				<Input type="text" id="name_input" name="name" label="Name" value="NAME IN BATABASE" />
			</div>
			<Button class="text-white">Update</Button>
		</form>
		<form class="flex flex-row items-end gap-4 bg-white p-6 pb-0 dark:bg-[#2F2F42]">
			<div class="flex-1">
				<Input type="email" id="email_input" name="email" label="Email" value="EMAIL IN DATABASE" />
			</div>
			<Button class="text-white">Update</Button>
		</form>
			TO BE DISPLAYED WHENEVER
		<div class="flex flex-row items-end gap-4 bg-white p-6 pb-0 dark:bg-[#2F2F42]">
			<Dropdown>
				<DropdownBtn link="/account">Option</DropdownBtn>
				<DropdownBtn link="/account">Option</DropdownBtn>
				<DropdownBtn link="/account">Option</DropdownBtn>
				<DropdownBtn type="divider"/>
				
			
			</Dropdown>
		</div>
	</Frame>
</Flex>
