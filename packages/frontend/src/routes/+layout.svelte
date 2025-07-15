<script lang="ts">
	import '../app.css';

	import { Flex, Frame } from 'sk-clib';

	let { children } = $props();
</script>


<Flex fill class="bg-backdrop overflow-y-auto">
    <Frame flex col class="animate mx-auto w-full max-w-full sm:max-w-3/4 md:max-w-3/5 lg:max-w-3/4 ">
        {@render children()}
    </Frame>
</Flex>