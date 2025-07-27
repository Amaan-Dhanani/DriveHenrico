<script lang="ts">
	import '../app.css';
    import { onMount } from 'svelte';
    import { global_mode$ } from '@components/lightdark/mode';

	import { Flex, Frame } from 'sk-clib';

    let mode$ = global_mode$.mode$;

	onMount(() => {
		mode$.subscribe((v) => {
			localStorage.theme = v;
			document.documentElement.classList.toggle('dark', v === 'dark');
		});
	});

	let { children } = $props();
</script>


<Flex fill class=" bg-backdrop-light dark:bg-backdrop overflow-y-auto">
    <Frame flex col class="animate mx-auto w-full max-w-full sm:max-w-3/4 md:max-w-3/5 lg:max-w-3/4 ">
        {@render children()}
    </Frame>
</Flex>