<script lang="ts"> 
	import { cn } from '$lib/components/utils';
	import type { Props } from "..";

	let {
		children, // currently unused
		class: className,

		// --- Default Classes 
		inputClass = $bindable('dark:bg-[#3E3E55] dark:text-white dark:border-[0px] border-[1px] border-[#e0e0e2] rounded-3 px-3 py-4 w-full text-[14px] rounded-[12px]'),
		labelClass = $bindable('text-[#858597] text-[14px]'),

		// --- User Defined Classes
		classLabel = $bindable(''),

		// --- Textarea Props
		label = $bindable(undefined),
		cap = $bindable(undefined),

		...rest
	}: Props = $props();

	let inputCls = $state(cn(inputClass, className));
	let labelCls = $state(cn(labelClass, classLabel));
	let width = $state(0);

	$effect(() => {
		inputCls = cn(inputClass, className);
		labelCls = cn(labelClass, classLabel);
	});
</script>

{#if label !== undefined} 
	<label class={labelCls} for={rest.id}>{label}</label>
{/if}

<textarea
	class={inputCls}
	maxlength={cap}
	oninput={(e) => width = (e.target as HTMLTextAreaElement)?.value.length}
	{...rest}
></textarea>

{#if cap !== undefined}
	<p class="dark:text-white text-right text-[12px]">{width}/{cap}</p>
{/if}
