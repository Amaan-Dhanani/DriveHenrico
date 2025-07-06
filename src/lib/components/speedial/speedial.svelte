<script lang="ts">
	import { writable } from 'svelte/store';
	import { LightDark } from '..';
	import { Refresh } from '..';

	let isActive$ = writable(false);

	const cn = (...classes: (string | boolean | undefined | null)[]) =>
		classes.filter(Boolean).join(' ');
</script>

<!-- Speed Dial -->
<div class="fixed top-6 left-6 z-50 flex items-center space-x-3">
	{#if $isActive$}
		<!-- Refresh Button -->
		<Refresh />

		<!-- Light/Dark Toggle Button -->
		<LightDark />
	{/if}

	<!-- Anchor FAB (Plus icon) -->
	<button
		class="group w-14 h-14 rounded-full bg-gray-800 hover:bg-gray-700 text-white shadow-lg flex items-center justify-center transition"
		on:click={() => isActive$.update(v => !v)}
	>
		<!-- Static Plus Icon -->
		<svg
			class="w-6 h-6"
			fill="none"
			stroke="currentColor"
			stroke-width="2"
			viewBox="0 0 24 24"
		>
			<path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4" />
		</svg>
	</button>
</div>
