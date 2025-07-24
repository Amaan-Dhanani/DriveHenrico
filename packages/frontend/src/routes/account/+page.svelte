<script lang="ts">
	import { Input, Dropdown } from '@components';
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

	</Frame>
</Flex>
