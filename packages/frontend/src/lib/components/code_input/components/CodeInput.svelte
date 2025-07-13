<script lang="ts">
	import { onMount } from 'svelte';

	export let length = 6;
	export let value = '';
	export let placeholder = '•';
	export let name = 'code';
	export let inputWrapClass = '';
	export let inputClass = '';
	export let containerClass = '';
	export let onChange: (code: string) => void = () => {};

	let codeValues: string[] = Array(length).fill('');
	let inputRefs: (HTMLInputElement | null)[] = [];

	$: joinedcode = codeValues.join('');

	onMount(() => {
		if (value) {
			const init = value.slice(0, length).split('');
			codeValues = [...init, ...Array(length - init.length).fill('')];
		}
		onChange(joinedcode);
	});

	function handleInput(e: Event, idx: number) {
		const input = e.target as HTMLInputElement;
		let val = input.value;

		// Remove any non‑digit characters (optional)
		val = val.replace(/\D/g, '');

		/*
		 * --- New behaviour ---
		 * If the user types while a digit is already present, we just keep the
		 * *last* character they typed, so it *replaces* the previous one without
		 * forcing them to back‑space first.
		 */
		if (val.length > 1) {
			// Keep only the last character typed for this cell
			val = val.slice(-1);
		}

		codeValues[idx] = val;
		// Force the input box to show exactly that single character
		input.value = val;

		// Move focus if a digit was entered and we're not at the end
		if (val && idx < length - 1) {
			inputRefs[idx + 1]?.focus();
		}

		onChange(joinedcode);
	}

	function handleKeyDown(e: KeyboardEvent, idx: number) {
		if (e.key === 'Backspace') {
			if (codeValues[idx]) {
				// Clear current and stay
				codeValues[idx] = '';
			} else if (idx > 0) {
				// Move back and clear previous
				inputRefs[idx - 1]?.focus();
				codeValues[idx - 1] = '';
			}
			onChange(joinedcode);
			e.preventDefault();
		} else if (e.key === 'ArrowLeft' && idx > 0) {
			inputRefs[idx - 1]?.focus();
		} else if (e.key === 'ArrowRight' && idx < length - 1) {
			inputRefs[idx + 1]?.focus();
		} else if (e.key === 'ArrowLeft' && idx == 0) {
			inputRefs[idx]?.focus();
			snapCaretRight(e);
		}
	}

	function handlePaste(e: ClipboardEvent) {
		e.preventDefault();
		const data = e.clipboardData?.getData('text') ?? '';
		const chars = data.slice(0, length).replace(/\D/g, '').split('');
		codeValues = [...chars, ...Array(length - chars.length).fill('')];
		inputRefs[Math.min(chars.length, length - 1)]?.focus();
		onChange(joinedcode);
	}

	function snapCaretRight(event: Event) {
		const input = event.target as HTMLInputElement;

		// Snap caret to the end on next tick
		requestAnimationFrame(() => {
			const len = input.value.length;
			input.setSelectionRange(len, len);
		});
	}
</script>

<div class={`flex gap-2 ${containerClass}`}>
	{#each codeValues as val, idx}
		<div class={`flex-1 ${inputWrapClass}`}>
			<input
				bind:this={inputRefs[idx]}
				bind:value={codeValues[idx]}
				inputmode="numeric"
				maxlength="2"
				pattern="[0-9]"
				autocomplete="one-time-code"
				{placeholder}
				class={`w-full rounded border border-gray-300 text-center text-lg placeholder:opacity-40 focus:border-blue-600 focus:outline-none ${inputClass}`}
				oninput={(e) => handleInput(e, idx)}
				onkeydown={(e) => handleKeyDown(e, idx)}
				onpaste={handlePaste}
				onfocus={snapCaretRight}
				onmousedown={snapCaretRight}
				name={null}
			/>
		</div>
	{/each}

	<!-- Final joined input -->
	<input type="hidden" {name} bind:value={joinedcode} />
</div>
