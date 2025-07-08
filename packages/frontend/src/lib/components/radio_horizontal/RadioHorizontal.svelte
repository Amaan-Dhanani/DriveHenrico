<script lang="ts">
	import { cn } from "../../utils";
	export let options: { value: string }[] = [];
	export let name: string;
	export let label: string = '';
	export let selected: string;
	export let divClass = '';
	export let inputClass = '';
	export let labelClass = '';

	const baseClass =
		'h-[30px] rounded-[5px] text-[12px] px-4 flex items-center justify-center bg-gray-200 text-black peer-checked:bg-[#3D5CFF] peer-checked:text-white';
</script>
<p class={cn("text-[#858597] text-[14px] mb-[10px]", labelClass)}>{label}</p>
<div class={cn("flex select-none flex-wrap gap-2 justify-center", divClass)}>
	{#each options as { value }}
		<label class="cursor-pointer">
			<input
				type="radio"
				name={name}
				value={value}
				required
				bind:group={selected}
				class="hidden peer"
			/>
			<div class={cn(baseClass, inputClass)}>
				{value}
			</div>
		</label>
	{/each}
</div>
