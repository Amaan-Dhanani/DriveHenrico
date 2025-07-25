<script lang="ts">
	// --- Logic ---
	import { cn } from '@lib/utils';
	import type { Props } from '..';
	import { Flex, Frame } from 'sk-clib';

	let {
		class: className,
		classWrapper = $bindable(''), // User Defined
		wrapperClass = $bindable(`
            gap-2 px-[25%] flex justify-center
        `), // User Over-writable
		classContainer = $bindable(''), // User Defined
		containerClass = $bindable(`
            flex
        `), // User Over-writable
		codeInputClass = $bindable(`
            w-full
			min-w-[2rem]
			max-w-[3rem]
			max-w-[2rem]
			aspect-4/5
            rounded
            border focus:border-gray-300 border-[var(--color-primary)] focus:outline-none
            text-center text-lg placeholder:opacity-40 dark:text-white
        `), // User Over-writable
		length = $bindable(6),
		value = $bindable(''),
		placeholder = $bindable(null),
		name = $bindable(null),
		onchange = $bindable(undefined),
		...rest
	}: Props = $props();

	// Setup CodeInput's class
	let wrapperCls = $state(cn(wrapperClass, classWrapper));
	let containerCls = $state(cn(containerClass, classContainer));
	let codeInputCls = $state(cn(codeInputClass, className));

	$effect(() => {
		wrapperCls = cn(wrapperClass, classWrapper);
		containerCls = cn(containerClass, classContainer);
		codeInputCls = cn(codeInputClass, className);
	});

	// Generate "Array" of Inputs and Values
	let values: string[] = $state(Array(length).fill(''));
	let inputs: HTMLInputElement[] = $state([]);

	// Make a reactive joined variable
	let joined = $state(''); // I luv runes :)
	$effect(() => {
		joined = values.join('');
	});

	// ========= Events =========
	function oninput(event: Event, index: number) {
		const input_element = event.target as HTMLInputElement;
		let input_value = input_element.value;

		// Remove non-digit chars
		input_value = input_value.replace(/\D/g, '');

		// Over-write functionality
		if (input_value.length > 1) {
			input_value = input_value.slice(-1);
		}

		// Save the current value at that index
		values[index] = input_value;

		// Move focus over
		if (input_value && index < length - 1) {
			inputs[index + 1]?.focus();
		}
	}

	function onkeydown(event: KeyboardEvent, index: number) {
		if (event.key === 'Backspace') {
			event.preventDefault();

			// Clear current index and don't move
			if (values[index]) {
				values[index] = '';
				return;
			}

			// Assume no current index
			// Move back, clear previous
			inputs[index - 1]?.focus();
			values[index - 1] = '';
		}

		if (event.key === 'Delete') {
			event.preventDefault();

			// Assume no current index
			// Shift and clear next index
			for (let i = index; i < length - 1; i++) {
				values[i] = values[i + 1];
			}
			values[length - 1] = ''; // Clear the last box after the shift
		}

		if (event.key === 'ArrowLeft' && index > 0) {
			inputs[index - 1]?.focus();
		}

		if (event.key === 'ArrowRight' && index < length - 1) {
			inputs[index + 1]?.focus();
		}

		if (event.key === 'ArrowLeft' && index == 0) {
			inputs[index]?.focus();
			snapRight(event);
		}
	}

	function onpaste(event: ClipboardEvent) {
		event.preventDefault();

		// Get contents of clipboard (what was pasted)
		const pasted = event.clipboardData?.getData('text') ?? '';
		if (!pasted) return;

		// Pull out only numbers
		const numbers = pasted.slice(0, length).replace(/\D/g, '').split('');

		// Fill in padding
		values = [...numbers, ...Array(length - numbers.length).fill('')];

		// Focus on last box
		inputs[Math.min(numbers.length, length - 1)]?.focus();
	}

	function snapRight(event: Event) {
		const input_element: HTMLInputElement = event.target as HTMLInputElement;

		requestAnimationFrame(() => {
			const length = input_element.value.length;
			input_element.setSelectionRange(length, length);
		});
	}
</script>

<Flex row class={wrapperCls}>
	{#each values as _, idx}
		<Frame class={containerCls}>
			<input
				bind:this={inputs[idx]}
				bind:value={values[idx]}
				name={null}
				{placeholder}
				oninput={(e) => oninput(e, idx)}
				onkeydown={(e) => onkeydown(e, idx)}
				onfocus={snapRight}
				onmousedown={snapRight}
				{onpaste}
				class={codeInputCls}
				inputmode="numeric"
				maxlength="2"
				pattern="[0-9]"
				autocomplete="one-time-code"
				{...rest}
			/>
		</Frame>
	{/each}

	<!-- Hidden Input -->
	<input type="hidden" {name} bind:value={joined} />
</Flex>

<!--@component
	- Concept Established by GitHub user, TreltaSev
    - Component Originally Created by Amaan Dhanani
	- Remade component generated by SvelteForge🔥 by GitHub user TreltaSev
    - Subject to changes based on future updates by TreltaSev

    @file code-input.svelte
    @description
    A input designed for Verfication Code Input with separate boxes for each digit.

    @props
     ### Core Class Props:
    - `wrapperClass`: Base styling for the outermost wrapper element.
    - `containerClass`: Base styling for the inner container that holds each input.
    - `codeInputClass`: Default styling for each code input box.

    ### User-Overridable Class Props:
    These allow injecting *extra* styling on top of the defaults:
    - `classWrapper`: Optional user-defined classes to enhance or override the default `wrapperClass`.
    - `classContainer`: Optional user-defined classes to complement or replace `containerClass`.

	### Functional Props:
	- `name`: Identifier for the component (e.g., useful when used in forms or labeled contexts).
	- `length`:  Number of input boxes to render. The default is 6.
	- `placeholder`: Placeholder text shown inside each input box.

    @rendered
    Multiple HTML Inputs wrapped around a flex container with TypeScript functions to accompany the component.

    @usage
	 ```svelte
    <CodeInput classWrapper="pb-[3px]" name="code" length={8} placeholder="0" />
    ```
-->
