<script lang="ts">
	import { cn } from '$lib/components/utils';

	export let options: { label: string; value: string }[] = [];
	export let name: string;
	export let selected: string;
	export let className = '';
	export let pillClass = '';

	const baseClass =
		'h-[30px] rounded-[5px] text-[12px] px-4 flex items-center justify-center bg-gray-200 text-black peer-checked:bg-[#3D5CFF] peer-checked:text-white';
</script>
<div class={cn("flex select-none flex-wrap gap-2 justify-center", className)}>
	{#each options as { label, value, }}
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
				{label}
			</div>
		</label>
	{/each}
</div>
