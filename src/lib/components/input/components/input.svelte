<script lang="ts">

    // --- Logic ---
    import { cn } from '$lib/components/utils';
    import type { Props } from ".."
    
    let {
        children,
        class: className,
        
        // --- Default Classes 
        inputClass = $bindable('dark:bg-[#3E3E55] truncate dark:text-white dark:border-[0px] border-[1px] border-[#e0e0e2] rounded-3 px-3 py-4 w-full text-[14px] w-full rounded-[12px] px-4 py-3'),
        labelClass = $bindable('text-[#858597] text-[14px]'),

        // --- User Defined Classes
        classLabel = $bindable(''),

        // --- Input Props
        label = $bindable(undefined),

        ...rest
    }: Props = $props();


    // Setup Input's class

    let inputCls = $state(cn(inputClass, className));
    let labelCls = $state(cn(labelClass, classLabel))
    $effect(() => {
        inputCls = cn(inputClass, className)
        labelCls = cn(labelClass, classLabel)
    })

</script>


{#if label !== undefined} 
    <label class={labelCls} for={rest.id}>{label}</label>
{/if}

<input class={inputCls} {...rest}/>


