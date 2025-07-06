<script>
	export let number;
	export let question = "";
	export let answerchoicea = "";
	export let correctanswer = "";
	export let answerchoiceb = "";
	export let answerchoicec = "";
	export let answerchoiced = "";
	export let explanation = "";
	export let image = "";
</script>

<div class="gap-0 dark:text-white">
	<h2 class="mt-0 mb-1 text-[16px] underline">Question {number}</h2>

	{#if question}
		<p class="text-[14px] ml-[30px]"><span class="font-bold">Question:&nbsp;&nbsp;</span>{question}</p>
	{/if}

	{#if answerchoicea}
		<p class="text-[14px] ml-[30px]"><span class="font-bold">Answer Choice A:&nbsp;&nbsp;</span>{answerchoicea}</p>
	{/if}

	{#if answerchoiceb}
		<p class="text-[14px] ml-[30px]"><span class="font-bold">Answer Choice B:&nbsp;&nbsp;</span>{answerchoiceb}</p>
	{/if}

	{#if answerchoicec}
		<p class="text-[14px] ml-[30px]"><span class="font-bold">Answer Choice C:&nbsp;&nbsp;</span>{answerchoicec}</p>
	{/if}

	{#if answerchoiced}
		<p class="text-[14px] ml-[30px]"><span class="font-bold">Answer Choice D:&nbsp;&nbsp;</span>{answerchoiced}</p>
	{/if}

	{#if correctanswer}
		<p class="text-[14px] ml-[30px]"><span class="font-bold">Correct Answer:&nbsp;&nbsp;</span>{correctanswer}</p>
	{/if}

	{#if explanation}
		<p class="text-[14px] ml-[30px]"><span class="font-bold">Explanation:&nbsp;&nbsp;</span>{explanation}</p>
	{/if}

	{#if image}
		<!-- svelte-ignore a11y_img_redundant_alt -->
		<img 
			src={image} 
			alt="Image" 
			class="w-full max-w-sm h-auto mt-4 rounded shadow-md object-contain"
		/>
	{/if}
	<hr class="dark:border-white mt-[15px]" />
</div>
