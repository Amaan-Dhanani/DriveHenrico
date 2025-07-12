<script lang="ts">
import { onMount } from "svelte";

export let length: number = 6;
export let placeholder: string = "\u2022";
export let value: string = "";
export let name: string = "";
export let inputWrapClass: string = "";
export let inputClass: string = "";
export let containerClass: string = "";
export let onChange: (otpValue: string) => void = () => {};

let otpValues: string[] = Array(length).fill("");
let inputRefs: HTMLInputElement[] = [];

onMount(() => {
  if (value && typeof value === "string") {
    const initialValues = value.slice(0, length).split("");
    otpValues = [
      ...initialValues,
      ...Array(length - initialValues.length).fill("")
    ];
  }
  updateOtpValue();
});

function handleInput(event: Event, index: number) {
  const input = event.target as HTMLInputElement;
  const inputValue = input.value;
  if (inputValue) {
    otpValues[index] = inputValue.slice(-1);
    if (index < length - 1) {
      inputRefs[index + 1]?.focus();
    }
  } else {
    otpValues[index] = "";
  }
  updateOtpValue();
}

function handleKeyDown(event: KeyboardEvent, index: number) {
  if (event.key === "Backspace" && otpValues[index] === "" && index > 0) {
    inputRefs[index - 1]?.focus();
  }
}

function handlePaste(event: ClipboardEvent) {
  event.preventDefault();
  const pastedData = event.clipboardData?.getData("text");
  if (pastedData) {
    const pastedChars = pastedData.slice(0, length).split("");
    otpValues = [
      ...pastedChars,
      ...Array(length - pastedChars.length).fill("")
    ];
    inputRefs[Math.min(pastedChars.length, length - 1)]?.focus();
    updateOtpValue();
  }
}

function updateOtpValue() {
  const otpValue = otpValues.join("");
  onChange(otpValue);
}
</script>

<!-- Container -->
<div class={`flex w-auto mx-[125px] gap-2 ${containerClass}`}>
  {#each otpValues as _, index}
    <!-- Wrapper to allow flexible width per input -->
    <div class={`flex-1 ${inputWrapClass}`}>
      <input
        name={name}
        inputmode="numeric"
        bind:this={inputRefs[index]}
        bind:value={otpValues[index]}
        on:input={(e) => handleInput(e, index)}
        on:keydown={(e) => handleKeyDown(e, index)}
        on:paste={handlePaste}
        maxlength="1"
        autocomplete="one-time-code"
        class={`w-full rounded border border-gray-300 text-center text-lg placeholder:opacity-40 focus:outline-none focus:border-blue-600 ${inputClass}`}
        {placeholder}
      />
    </div>
  {/each}
</div>
