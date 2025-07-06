<script lang="ts">
	import type { PageData } from './$types';
	import '$lib/css/app.css';
	export let data: PageData;
	import { Navigation } from '$lib/components';
	import { Logo } from '$lib/components';
</script>

<!-- Full screen container -->
<div
	class="fixed inset-0 -z-[100] mt-[100vh] h-[300vh] w-screen overflow-hidden bg-[#3D5CFF]"
></div>
<div class="mr-[1rem] ml-[1rem] flex min-h-screen flex-col bg-[#3D5CFF]">
	<!-- Header -->
	<Logo alt={true}/>
<h1 class="mb-0 ml-[5px] pt-[86px] text-[32px] font-bold text-white">Hi, {data.name.split(' ')[0]}</h1>
		<p class="mt-0 mb-[10px] ml-[5px] text-[14px] text-white">Welcome back to QuestOwl!</p>
	<!-- Form Section -->
	<div
		class="mb-[95px] box-border flex flex-grow flex-col gap-4 rounded-t-2xl bg-white px-6 py-8 dark:bg-[#2F2F42]"
	>
			<div class="gap-0 dark:text-white">
				<h2 class="mt-0 text-[16px]">
					
				</h2>
				<div
					class="box-border flex flex-grow flex-col rounded-t-2xl bg-white px-6 py-8 dark:bg-[#2F2F42]"
				>
					<button
						type="submit"
						class="mt-[20px] h-12 w-full rounded-xl bg-[#3d5cff] text-center text-white hover:cursor-pointer"
					>
						My Quests
					</button>
					<button
						type="submit"
						class="mt-[20px] h-12 w-full rounded-xl bg-[#3d5cff] text-center text-white hover:cursor-pointer"
					>
						My Classes
					</button>
					<button
						type="submit"
						class="mt-[20px] h-12 w-full rounded-xl bg-[#3d5cff] text-center text-white hover:cursor-pointer"
					>
						Quest Library
					</button>
					<button
						type="submit"
						class="mt-[20px] h-12 w-full rounded-xl bg-[#3d5cff] text-center text-white hover:cursor-pointer"
					>
						Notifications
					</button>
					
				</div>
			</div>
	</div>
	<Navigation/>
</div>

