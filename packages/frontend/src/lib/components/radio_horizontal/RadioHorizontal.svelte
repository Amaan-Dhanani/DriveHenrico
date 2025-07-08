<script lang="ts">
	import { Frame } from 'sk-clib';
	import { cn } from '../../utils';
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

<Frame flex col>
	<p class={cn('mb-[10px] text-[14px] text-[#858597]', labelClass)}>{label}</p>
	<div class={cn('flex flex-wrap justify-center gap-2 select-none', divClass)}>
		{#each options as { value }}
			<label class="cursor-pointer">
				<input type="radio" {name} {value} required bind:group={selected} class="peer hidden" />
				<div class={cn(baseClass, inputClass)}>
					{value}
				</div>
			</label>
		{/each}
	</div>
</Frame>
