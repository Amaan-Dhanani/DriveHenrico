<script lang="ts">
	import { cn } from '$lib/components/utils';
	import { goto } from '$app/navigation';

	export let name: string;
	export let selected: string;
	export let className = '';
	export let pillClass = '';
	export let visibleCount: number = 10; // number of buttons to display

	const allOptions = [
		{ value: 'Main', link: '/create/main' },
		{ value: 'Question 1', link: '/create/question1' },
		{ value: 'Question 2', link: '/create/question2' },
		{ value: 'Question 3', link: '/create/question3' },
		{ value: 'Question 4', link: '/create/question4' },
		{ value: 'Question 5', link: '/create/question5' },
		{ value: 'Question 6', link: '/create/question6' },
		{ value: 'Question 7', link: '/create/question7' },
		{ value: 'Question 8', link: '/create/question8' },
		{ value: 'Question 9', link: '/create/question9' },
		{ value: 'Question 10', link: '/create/question10' },
	];

	const baseClass =
		'h-[30px] rounded-[5px] text-[18px] px-4 flex items-center justify-center bg-gray-200 text-black peer-checked:bg-[#3D5CFF] peer-checked:text-white';
</script>

<div class={cn("flex flex-col select-none flex-wrap gap-2 justify-center items-center", className)}>
	{#each allOptions.slice(0, visibleCount) as { value, link }}
		<!-- svelte-ignore a11y_unknown_aria_attribute -->
		<!-- svelte-ignore a11y_no_static_element_interactions -->
		<!-- svelte-ignore a11y_click_events_have_key_events -->
		<div on:click={() => goto(link)}>
			<label class="cursor-pointer">
				<input
					type="radio"
					name={name}
					value={value}
					required
					bind:group={selected}
					class="hidden peer"
				/>
				<div class={cn(baseClass, pillClass)}>
					{value}
				</div>
			</label>
		</div>
	{/each}
</div>
