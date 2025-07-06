<script lang="ts">
	import '$lib/css/app.css';
	import { goto } from '$app/navigation';
	import Navigation from '$lib/components/navigation/Navigation.svelte';
	import { Logo } from '$lib/components';
</script>

<!-- Full screen container -->
<div
	class="fixed inset-0 -z-[100] mt-[100vh] h-[300vh] w-screen overflow-hidden bg-[#4c4c61] dark:bg-[#1F1F39]"
></div>
<div class="mr-[1rem] ml-[1rem] flex min-h-screen flex-col bg-[#4c4c61] dark:bg-[#1F1F39]">
	<!-- Header -->
	 <Logo/>
	<h1 class="mb-0 ml-[5px] pt-[86px] text-[32px] font-bold text-white">Creation Page</h1>
	<p class="mt-0 mb-[10px] ml-[5px] text-[12px] text-[#B8B8D2]"></p>
	<!-- Form Section -->
	<div
		class="mb-[95px] box-border flex flex-grow flex-col gap-4 rounded-t-2xl bg-white px-6 py-8 dark:bg-[#2F2F42]"
	>
		<div class="gap-0 dark:text-white">
			<h2 class="mt-0 text-[16px]">
				Do you want to make create a class for your students to access?
			</h2>
			<button
				type="submit"
				class="mt-[20px] h-12 w-full rounded-xl bg-[#3d5cff] text-center text-white hover:cursor-pointer"
                on:click={() => goto('/create/class')}
			>
				Create a Class
			</button>
			<div class="inline-flex w-full items-center justify-center">
				<hr class="my-8 h-px w-64 border-0 bg-gray-200 dark:bg-gray-700" />
				<span
					class="absolute left-1/2 -translate-x-1/2 bg-white px-3 font-medium text-gray-900 dark:bg-[#2F2F42] dark:text-white"
					>or</span
				>
			</div>
            <h2 class="mt-0 text-[16px]">
				Do you want to make create a quest, which you can also add to your class?
			</h2>
            <button
				class="mt-[20px] h-12 w-full rounded-xl bg-[#3d5cff] text-center text-white hover:cursor-pointer"
                on:click={() => goto('/create/main')}
			>
				Create a Quest
			</button>
            <br><br><hr class="dark:border-white" />
			<button
				class="mt-[20px] w-full mb-[10px] h-12 rounded-xl bg-red-600 text-white transition hover:bg-red-700"
				aria-label="back"
				on:click={() => goto('/dashboard')}
			>
				Back
			</button>

		</div>
	</div>
</div>
<Navigation/>
