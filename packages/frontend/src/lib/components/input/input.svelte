<script lang="ts">
	import { cn } from '@lib/utils';
	import type { Props } from '../..';

	let {
		type = '',
		children,
		class: className,
		inputClass = $bindable(
			'dark:bg-[#3E3E55] bg-[#F0F0F2] truncate dark:text-white dark:outline-0 outline box-border outline-[#e0e0e2] rounded-3 px-3 py-4 w-full text-[14px] rounded-[12px] px-4 py-3'
		),
		labelClass = $bindable('text-[#858597] text-[14px]'),
		classLabel = $bindable(''),
		label = $bindable(undefined),
		...rest
	}: Props = $props();

	const inputId = rest.id ?? 'hs-input-' + crypto.randomUUID();

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

{#if type === 'password'}
	<div class={cn("relative", inputCls)}>
		<input id={inputId} type={showPassword ? 'text' : 'password'} {...rest} />

		<button
			type="button"
			onclick={togglePassword}
			class="absolute inset-y-0 end-0 z-20 flex cursor-pointer items-center rounded-e-md px-3 text-gray-400 dark:text-white focus:text-blue-600 focus:outline-none dark:focus:text-blue-500"
			aria-label="Toggle password visibility"
		>
			<!-- eye / eye‑off icon -->
			{#if showPassword}
				<!-- eye‑off -->
				<svg
					xmlns="http://www.w3.org/2000/svg"
					class="h-5 w-5"
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor"
					><circle cx="12" cy="12" r="3" stroke-width="2" />
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.542-7a10.05 10.05 0 012.659-4.293M6.22 6.22A9.964 9.964 0 0112 5c4.478 0 8.268 2.943 9.542 7a10.052 10.052 0 01-4.195 5.144M3 3l18 18"
					/>
				</svg>
			{:else}
				<!-- eye -->
				<svg
					xmlns="http://www.w3.org/2000/svg"
					class="h-5 w-5"
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
					/>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
					/>
				</svg>
			{/if}
		</button>
	</div>
{:else}
	<!-- Plain input -->
	<input class={inputCls} id={inputId} {type} {...rest} />
{/if}
