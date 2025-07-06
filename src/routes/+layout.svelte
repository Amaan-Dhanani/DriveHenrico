<script lang="ts">

  // Global CSS Import
  import '$lib/css/app.css';

	import { page } from '$app/state';
	import { onMount } from 'svelte';
	import { LightDark } from '$lib/components';
	import { global_mode$ } from '$lib/components/darklight/mode';
	import Speedial from '$lib/components/speedial/speedial.svelte';

	let pageName = page.url.pathname;

	let mode$ = global_mode$.mode$;

	onMount(() => {
		mode$.subscribe((v) => {
			localStorage.theme = v;
			document.documentElement.classList.toggle('dark', v === 'dark');
		});
	});
</script>


{#if pageName === "/register" || pageName === "/login" || pageName === "/account"}
  <div class="w-full -z-10000 bg-[#F0F0F2] dark:bg-[#1F1F39]">
    <main class="size-full">
      <slot />
      <Speedial />
    </main>
  </div>
{:else if pageName === "/dashboard"}
  <div class="w-full -z-10000 bg-[#3D5CFF]">
    <main class="size-full">
      <slot />
      <Speedial />
    </main>
  </div>
{:else if pageName.startsWith("/create")}
  <div class="w-full -z-10000 bg-[#4c4c61] dark:bg-[#1F1F39]">
    <main class="size-full">
      <slot />
      <Speedial />
    </main>
  </div>
{/if}


<style>
	main {
		max-width: 30rem;
		margin-inline: auto;
	}
</style>


<div>


    <script src="https://cdn.botpress.cloud/webchat/v3.0/inject.js" defer></script>
<script src="https://files.bpcontent.cloud/2025/06/29/22/20250629224018-MY8I7PZ5.js" defer></script>
<style>
  .bpFab {
    bottom: 100px !important;
  }
</style>
    
</div>