<script lang="ts">
	
	// === Core ===
	import '../app.css';
	import { onMount } from 'svelte';

	// === Components ===
	import { Flex, Frame } from 'sk-clib';

	// === State ===
	import { global_theme$ } from '@state';
	let mode$ = global_theme$.theme$;

	onMount(() => {
		const unsubscribe = mode$.subscribe((v) => {
			document.documentElement.classList.toggle('dark', v === 'dark');
		});
		return () => unsubscribe();
	});

	let { children } = $props();
</script>

<Flex fill class=" bg-backdrop-light dark:bg-backdrop overflow-y-auto">
	<Frame flex col class="animate sm:max-w-3/4 md:max-w-3/5 lg:max-w-3/4 mx-auto w-full max-w-full ">
		{@render children()}
	</Frame>
</Flex>
