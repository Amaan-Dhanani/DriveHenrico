<script lang="ts">
	// --- Logic ---
	import { cn } from '@lib/utils';
	import type { Props } from '..';
	import { Flex, Frame } from 'sk-clib';

	let {
		class: className,
		classWrapper = $bindable(''), // User Defined
		wrapperClass = $bindable(`
            gap-2
        `), // User Over-writable
		classContainer = $bindable(''), // User Defined
		containerClass = $bindable(`
            flex-1
        `), // User Over-writable
		codeInputClass = $bindable(`
            w-full
            rounded
            border border-gray-300 focus:border-blue-600 focus:outline-none
            text-center text-lg placeholder:opacity-40
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
		console.log('Changed', joined);
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
    Generated by SvelteForge🔥
-->
