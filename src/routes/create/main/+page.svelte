<script lang="ts">
	import { enhance } from '$app/forms';
	import '$lib/css/app.css';
	import { Input } from '$lib/components';
	export let data;
	const { tempquest } = data;
	import { RadioHorizontal } from '$lib/components';
	let selected = tempquest.quest_type || 'IceQuest Platformer';
	let selected2 = tempquest.access || 'Public';
	import { goto } from '$app/navigation';
	import { Refresh } from '$lib/components';
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
	<p class="mt-0 mb-[10px] ml-[5px] text-[12px] text-[#B8B8D2]">
		Unknown subheading
	</p>

	<!-- Form Section -->
	<form
		method="POST"
		autocomplete="off"
		use:enhance
		class="box-border flex flex-grow flex-col gap-4 rounded-t-2xl bg-white px-6 py-8 dark:bg-[#2F2F42]"
	>
		<h1 class="mb-[5px] text-center text-[18px] dark:text-white">Quest Classification</h1>
		<div class="gap-0">
			<h2 class="mb-[5px] text-[16px] dark:text-white">Categories</h2>
			<RadioHorizontal
				name="quest_type"
				bind:selected
				options={[
					{ label: 'IceQuest Platformer', value: 'IceQuest Platformer' },
				]}
			/>
		</div>
		<div class="gap-0">
			<h2 class="mt-[10px] mb-[5px] text-[16px] dark:text-white">Quest Title</h2>
			<Input type="text" id="quest_title" name="quest_title" value={tempquest?.quest_title} required />
		</div>
		<div class="gap-0">
			<h2 class="mt-[5px] mb-[5px] text-[16px] dark:text-white">Access</h2>
			<div class="flex flex-row ml-[20px]">
				<RadioHorizontal
					name="access"
					bind:selected={selected2}
					options={[
						{ label: 'Public', value: 'Public' },
						{ label: 'Private', value: 'Private' }
					]}
				/>
			</div>
		</div>
		<!-- Submit Button -->
		<button class="h-12 w-full rounded-xl bg-[#3d5cff] text-center text-white hover:cursor-pointer mt-[20px]">
			Continue Quest Creation
		</button>
		<button
			class="h-12 mb-[10px] mt-[20px] rounded-xl bg-red-600 text-white transition hover:bg-red-700"
			aria-label="back" on:click={() => goto('/dashboard')}
		>
			Back
		</button>
	</form>
</div>
