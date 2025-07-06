<script lang="ts">
	import '$lib/css/app.css';
	import { writable } from 'svelte/store';

	type Quest = { quest_title: string; created_at: string; id: string };
	type TempQuest = { [key: string]: string };

	export let data: {
		quests: Quest[];
		tempquest: TempQuest;
	};

	const { tempquest } = data;

	const selectedQuest = writable<Quest | null>(null);

	function openQuest(quest: Quest) {
		selectedQuest.set(quest);
	}

	function goBack() {
		selectedQuest.set(null);
	}
</script>

<div class="mx-auto max-w-3xl p-6">
	{#if $selectedQuest}
		<!-- Clear page and show QuestionPreview list for selected quest -->
		<button
			on:click={goBack}
			class="mb-4 rounded bg-indigo-600 px-4 py-2 text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500"
		>
			← Back to Quests
		</button>

		<h2 class="mb-4 text-2xl font-bold text-indigo-700">Quest: {$selectedQuest.quest_title}</h2>
		<!---get everything from tempquest and put it in line by line-->
	{:else}
		<!-- Show list of quests -->
		<h1 class="mb-6 text-4xl font-bold text-indigo-700">Your Quests</h1>

		{#if data.quests.length > 0}
			<ul class="space-y-4">
				{#each data.quests as quest}
					<!-- svelte-ignore a11y_no_noninteractive_element_to_interactive_role -->
					<li
						role="button"
						tabindex="0"
						class="cursor-pointer rounded-lg bg-white p-5 shadow-md hover:shadow-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
						on:click={() => openQuest(quest)}
						on:keydown={(e) => (e.key === 'Enter' || e.key === ' ') && openQuest(quest)}
					>
						<div class="text-xl font-semibold">{quest.quest_title}</div>
						<div class="mt-1 text-sm text-gray-500">{quest.id}</div>
						<div class="mt-1 text-sm text-gray-500">
							{new Date(quest.created_at).toLocaleString()}
						</div>
					</li>
				{/each}
			</ul>
		{:else}
			<p class="text-center text-gray-600">No quests found.</p>
		{/if}
	{/if}
	<button
				class="mt-[20px] w-full mb-[10px] h-12 rounded-xl bg-red-600 text-white transition hover:bg-red-700"
				aria-label="back"
				on:click={() => goto('/dashboard')}
			>
				Back
			</button>
</div>
