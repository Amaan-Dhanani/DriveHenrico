<script lang="ts">
  import { cn } from "$lib/utils";
  import type { Props } from "../..";

  let {
    type = "",
    children,
    class: className,
    inputClass = $bindable(
      "dark:bg-[#3E3E55] truncate dark:text-white dark:border-0 border border-[#e0e0e2] rounded-3 px-3 py-4 w-full text-[14px] rounded-[12px] px-4 py-3"
    ),
    labelClass = $bindable("text-[#858597] text-[14px]"),
    classLabel = $bindable(""),
    label = $bindable(undefined),
    ...rest
  }: Props = $props();

  const inputId = rest.id ?? "hs-input-" + crypto.randomUUID();

  // --- reactive classes
  let inputCls = $state(cn(inputClass, className));
  let labelCls = $state(cn(labelClass, classLabel));
  $effect(() => {
    inputCls = cn(inputClass, className);
    labelCls = cn(labelClass, classLabel);
  });

  // --- password toggling
  let showPassword = $state(false);
  function togglePassword() {
    showPassword = !showPassword;
  }
</script>

{#if label !== undefined}
  <label class={labelCls} for={inputId}>{label}</label>
{/if}

{#if type === "password"}
  <div class="relative">
    <input
      class={inputCls}
      id={inputId}
      type={showPassword ? "text" : "password"}
      {...rest}
    />

    <button
      type="button"
      on:click={togglePassword}
      class="absolute inset-y-0 end-0 flex items-center z-20 px-3 cursor-pointer text-gray-400 rounded-e-md focus:outline-none focus:text-blue-600 dark:text-neutral-600 dark:focus:text-blue-500"
      aria-label="Toggle password visibility"
    >
      <!-- eye / eye‑off icon -->
      {#if showPassword}
        <!-- eye‑off -->
        <svg class="shrink-0 size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M17.94 17.94A10.42 10.42 0 0 1 12 19c-7 0-10-7-10-7a13.43 13.43 0 0 1 4.06-5.94M1 1l22 22"/>
        </svg>
      {:else}
        <!-- eye -->
        <svg class="shrink-0 size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M1 12s3-7 11-7 11 7 11 7-3 7-11 7S1 12 1 12Z"/>
          <circle cx="12" cy="12" r="3"/>
        </svg>
      {/if}
    </button>
  </div>
{:else}
  <!-- Plain input -->
  <input
    class={inputCls}
    id={inputId}
    type={type}
    {...rest}
  />
{/if}
