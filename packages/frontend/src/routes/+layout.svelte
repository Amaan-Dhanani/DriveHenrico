<script lang="ts">
	import '../app.css';

	import { Flex, Frame } from 'sk-clib';

	let { children } = $props();
</script>


<Flex fill class="bg-backdrop overflow-y-auto">
	<Frame flex col class="mx-auto max-w-full md:max-w-1/2">
		{@render children()}
	</Frame>
</Flex>