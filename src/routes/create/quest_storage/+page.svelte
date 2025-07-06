<script lang="ts">
	import { QuestionPreview } from '$lib/components';
	import Navigation2 from '$lib/components/navigation/Navigation2.svelte';
	import '$lib/css/app.css';
	export let data;
	const { tempquest } = data;
	import { Refresh } from '$lib/components';
</script>

<!-- Full screen container -->
<div
	class="fixed inset-0 -z-[100] mt-[100vh] h-[300vh] w-screen overflow-hidden bg-[#4c4c61] dark:bg-[#1F1F39]"
></div>
<div class="mr-[1rem] ml-[1rem] flex min-h-screen flex-col bg-[#4c4c61] dark:bg-[#1F1F39]">
	<!-- Header -->
	 
	<h1 class="mb-0 ml-[5px] pt-[86px] text-[32px] font-bold text-white">Create a Quest</h1>
	<p class="mt-0 mb-[10px] ml-[5px] text-[12px] text-[#B8B8D2]">
		Great job on finishing a section of the form! Just remember that 10 Questions is the maximum
		amount of questions that can be submitted. You have options to
		{#if tempquest?.question != '10'}
			go to the next question,
		{/if} access other questions, return to the home page, or submit what you have.
	</p>
	<!-- Form Section -->
	<div
		class="box-border flex flex-grow flex-col mb-[95px] gap-4 rounded-t-2xl bg-white px-6 py-8 dark:bg-[#2F2F42]"
	>
	<div class="gap-0">
		<h1 class="text-center mb-[10px] text-[18px] dark:text-white">Preview</h1>
		<hr class="dark:border-white" />
		<hr class="dark:border-white" />
		<hr class="dark:border-white" />
		<hr class="dark:border-white" />
	</div>
		<div class="gap-0 dark:text-white">
			<h2 class="mt-[0px] mb-[5px] text-[16px] underline">Quest Classification</h2>
			{#if !tempquest.quest_title}
				<div><script>location.replace('/create/main')</script></div>
			{/if}
			<p class="text-[14px] ml-[30px]">
				<span class="font-bold">Quest Title:&nbsp;&nbsp;</span>{tempquest?.quest_title}
			</p>
			<p class="text-[14px] ml-[30px]">
				<span class="font-bold">Quest Type:&nbsp;&nbsp;</span>{tempquest?.quest_type}
			</p>
			<p class="text-[14px] ml-[30px]">
				<span class="font-bold">Access:&nbsp;&nbsp;</span>{tempquest?.access}
				<br><br>
			</p>
			<hr class="dark:border-white" />
		</div>
		{#each Array.from({ length: 10 }, (_, i) => i + 1) as number}
	{#if tempquest[`question_${number}`]}
		<QuestionPreview
			number={number}
			image={tempquest[`image_${number}`]}
			correctanswer={tempquest[`correctanswer_${number}`]}
			explanation={tempquest[`explanation_${number}`]}
			answerchoicea={tempquest[`answerchoicea_${number}`]}
			answerchoiceb={tempquest[`answerchoiceb_${number}`]}
			answerchoicec={tempquest[`answerchoicec_${number}`]}
			answerchoiced={tempquest[`answerchoiced_${number}`]}
			question={tempquest[`question_${number}`]}
		/>
		<Navigation2 number={number}/>
	{/if}
{/each}

{#if !Array.from({ length: 10 }, (_, i) => i + 1).some(n => tempquest[`question_${n}`])}
	<Navigation2 number={0}/>
{/if}


	</div>
</div>
