<script lang="ts">
	import { enhance } from '$app/forms';
	import '$lib/css/app.css';
	import ImageSubmitter from "$lib/components/image_submitter/ImageSubmitter.svelte";
	export let data;
	const { tempquest } = data;
	import { RadioHorizontal } from '$lib/components';
	let selected2 = tempquest.correctanswer_2 || 'A';
	import { Textarea } from '$lib/components';
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
		class="box-border flex flex-grow flex-col rounded-t-2xl bg-white px-6 py-8 dark:bg-[#2F2F42]"
	>
		<h1 class="mb-[5px] text-center text-[18px] dark:text-white mb-4">Question 2</h1>
			<h2 class="mb-[5px] text-[16px] dark:text-white">Question</h2>
			<Textarea
				id="question_2"
				name="question_2"
				required
				cap={1850}
				class="mb-[10px]"
				value={tempquest?.question_2}
				placeholder="Enter question here. Maximum length 1850 characters."
			/>
			<h2 class="mb-[5px] text-[16px] dark:text-white">Answer Choice A</h2>
			<Textarea
				id="answerchoicea_2"
				name="answerchoicea_2"
				required
				cap={1850}
				value={tempquest?.answerchoicea_2}
				placeholder="Enter Answer Choice A here. Maximum length 1850 characters."
			/>
			<h2 class="mb-[5px] text-[16px] dark:text-white">Answer Choice B</h2>
			<Textarea
				id="answerchoiceb_2"
				name="answerchoiceb_2"
				required
				cap={1850}
				value={tempquest?.answerchoiceb_2}
				placeholder="Enter Answer Choice B here. Maximum length 1850 characters."
			/>
			<h2 class="mb-[5px] text-[16px] dark:text-white">Answer Choice C</h2>
			<Textarea
				id="answerchoicec_2"
				name="answerchoicec_2"
				required
				cap={1850}
				value={tempquest?.answerchoicec_2}
				placeholder="Enter Answer Choice C here. Maximum length 1850 characters."
			/>
			<h2 class="mb-[5px] text-[16px] dark:text-white">Answer Choice D</h2>
			<Textarea
				id="answerchoiced_2"
				name="answerchoiced_2"
				required
				cap={1850}
				value={tempquest?.answerchoiced_2}
				placeholder="Enter Answer Choice D here. Maximum length 1850 characters."
			/>
			<h2 class="mb-[5px] text-[16px] dark:text-white">Explanation (optional)</h2>
			<Textarea
				id="explanation_2"
				name="explanation_2"
				cap={1850}
				rows={3}
				value={tempquest?.explanation_2}
				placeholder="Optionally explain the reasoning behind the correct answer or provide extra context. Max length - 1850 chars."
			/>
			<h2 class="mb-[5px] text-[16px] dark:text-white">Image Attachment (optional)</h2>
			<ImageSubmitter name="image_2" id="image_2" dataURI={tempquest?.image_2}/>

		<div class="gap-0">
			<h2 class="mt-[10px] mb-[5px] text-[16px] dark:text-white">Correct Answer</h2>
				<RadioHorizontal
					name="correctanswer_2"
					bind:selected={selected2}
					options={[
						{ label: 'A', value: 'A' },
						{ label: 'B', value: 'B' },
						{ label: 'C', value: 'C' },
						{ label: 'D', value: 'D' },
					]}
				/>

		</div>
		<br>
		<!-- Submit Button -->
		<button
			class="mt-[20px] h-12 w-full rounded-xl bg-[#3d5cff] text-center text-white hover:cursor-pointer"
		>
			Continue Quest Creation
		</button>
		<button
			class="h-12 mb-[10px] mt-[20px] rounded-xl bg-red-600 text-white transition hover:bg-red-700"
			aria-label="back" on:click={() => goto('/create/quest_storage')}
		>
			Back
		</button>
	</form>
</div>
