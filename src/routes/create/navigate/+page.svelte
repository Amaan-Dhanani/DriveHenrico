<script lang="ts">
	import '$lib/css/app.css';
	export let data;
	let { tempquest } = data;
	import { goto } from '$app/navigation';
	let selected = '';
	import RadioVertical from '$lib/components/selectotherquestion/components/RadioVertical.svelte';
	import { Logo } from '$lib/components';
</script>

<!-- Full screen container -->
<div
	class="fixed inset-0 -z-[100] mt-[100vh] h-[300vh] w-screen overflow-hidden bg-[#4c4c61] dark:bg-[#1F1F39]"
></div>
<div class="mr-[1rem] ml-[1rem] flex min-h-screen flex-col bg-[#4c4c61] dark:bg-[#1F1F39]">
	<!-- Header -->
	 <Logo/>
	<h1 class="mb-0 ml-[5px] pt-[86px] text-[32px] font-bold text-white">Create a Quest</h1>
	<p class="mt-0 mb-[10px] ml-[5px] text-[12px] text-[#B8B8D2]"></p>
	<!-- Form Section -->
	<div
		class="box-border flex flex-grow flex-col h-screen gap-4 rounded-t-2xl bg-white px-6 py-8 dark:bg-[#2F2F42]"
	>
		<div class="gap-0">
			<h1 class="mb-[10px] text-center text-[18px] dark:text-white">Navigate Previously Done Sections</h1>
			<hr class="dark:border-white" />
			<hr class="dark:border-white" />
			<hr class="dark:border-white" />
			<hr class="dark:border-white" />
		</div>
		<RadioVertical
	name="navigation"
	visibleCount={tempquest.question + 1}
	selected=""
	className=""
	pillClass=""
/>
<button
			class="h-12 mb-[10px] mt-[20px] rounded-xl bg-red-600 text-white transition hover:bg-red-700"
			aria-label="back" on:click={() => goto('/create/quest_storage')}
		>
			Back
		</button>
	</div>
	
</div>

