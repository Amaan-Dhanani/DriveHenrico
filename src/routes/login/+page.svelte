<script lang="ts">
	import { enhance } from '$app/forms';
	import type { ActionData } from './$types';
	import '$lib/css/app.css';
	import { Input } from '$lib/components';
	import type { PageData } from '../$types';
	export let form: ActionData;
	export let data: PageData;
	import { Logo } from '$lib/components';
</script>

<!-- Full screen container -->
<div class="fixed inset-0 -z-[100] overflow-hidden w-screen h-[300vh] bg-[#F0F0F2] dark:bg-[#1F1F39] mt-[100vh]"></div>
<div class="flex flex-col min-h-screen bg-[#F0F0F2] dark:bg-[#1F1F39] ml-[1rem] mr-[1rem]">

	<!-- Header -->
	 <Logo/>
	<h1 class="text-[32px] pt-[86px] font-bold ml-[5px] mb-0 dark:text-white">Sign In</h1>
	<p class="mt-0 ml-[5px] mb-[10px] text-[12px] text-[#B8B8D2]">
		Welcome back to QuestOwl!
	</p>

	<!-- Form Section -->
	<form
		method="POST"
		autocomplete="off"
		use:enhance
		class="flex flex-col flex-grow rounded-t-2xl py-8 px-6 box-border gap-4 bg-white dark:bg-[#2F2F42]"
	>
		<div>
			<Input type="email"
			id="email_input"
			name="email"
			label="Email"
			value={form?.email ?? ""} />
		</div>
		<div>
			<Input type="password" class="mb-[12px]" id="password_input" label="Password" name="password" />
		</div>
		

		<!-- Submit Button -->
		<button class="h-12 w-full rounded-xl bg-[#3d5cff] text-center text-white hover:cursor-pointer">
			Sign In
		</button>

		<!-- Sign In Link -->
		<p class="text-center text-[#858597] text-[14px]">
			Don't have an account? <a class="text-[#3D5CFF] font-bold underline" href="/register">Get Started</a>
		</p>

<div class="mt-10 flex flex-col text-center justify-center items-center">
			<!-- Optional messages -->
			{#if form?.error}
				<div
					id="toast-danger"
					class="mb-4 flex w-full max-w-xs items-center rounded-lg bg-[#F0F0F2] p-4 text-gray-500 shadow-sm dark:bg-gray-800 dark:text-gray-400"
					role="alert"
				>
					<div
						class="inline-flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-red-100 text-red-500 dark:bg-red-800 dark:text-red-200"
					>
						<svg
							class="h-5 w-5"
							aria-hidden="true"
							xmlns="http://www.w3.org/2000/svg"
							fill="currentColor"
							viewBox="0 0 20 20"
						>
							<path
								d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 11.793a1 1 0 1 1-1.414 1.414L10 11.414l-2.293 2.293a1 1 0 0 1-1.414-1.414L8.586 10 6.293 7.707a1 1 0 0 1 1.414-1.414L10 8.586l2.293-2.293a1 1 0 0 1 1.414 1.414L11.414 10l2.293 2.293Z"
							/>
						</svg>
						<span class="sr-only">Error icon</span>
					</div>
					<div class="ms-3 text-sm">{form.error}</div>
				</div>
			{/if}
		</div>
	</form>
</div>
