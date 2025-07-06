<script lang="ts">
	import '$lib/css/app.css';
	import { enhance } from '$app/forms';
	import type { ActionData, PageData } from './$types';
	import Input from '$lib/components/input/components/input.svelte';
	export let form: ActionData;
	export let data: PageData;
	import { Navigation } from '$lib/components';
	import { Logo } from '$lib/components';
</script>

<!-- Full screen background -->
<div
	class="fixed inset-0 -z-[100] mt-[100vh] h-[300vh] w-screen overflow-hidden bg-[#F0F0F2] dark:bg-[#1F1F39]"
></div>

<!-- Page Container -->
<div class="mx-4 flex min-h-screen flex-col bg-[#F0F0F2] dark:bg-[#1F1F39]">
	<!-- Header -->
	 <Logo/>
	<h1 class="pt-[86px] text-[32px] font-bold dark:text-white">Settings</h1>
	<p class="mb-4 text-sm text-[#B8B8D2]">Subheading unknown</p>

	<!-- Forms Container -->
	<div class="flex flex-col">
		<!-- Name Form -->
		<form
			action="?/name"
			method="POST"
			autocomplete="off"
			use:enhance
			class="flex flex-row items-end gap-4 rounded-t-xl bg-white p-6 pb-0 dark:bg-[#2F2F42]"
		>
			<div class="flex-1">
				<Input type="text" id="name_input" name="name" label="Name" value={data.name} />
			</div>
			<button
				class="h-10 rounded-md bg-[#3d5cff] px-4 text-sm whitespace-nowrap text-white hover:bg-[#2d4cf5]"
				aria-label="update name"
			>
				Update
			</button>
		</form>

		<!-- Email Form -->
		<form
			action="?/email"
			method="POST"
			autocomplete="off"
			use:enhance
			class="flex flex-row items-end gap-4 bg-white p-6 pt-5 pb-0 dark:bg-[#2F2F42]"
		>
			<div class="flex-1">
				<Input type="email" id="email_input" name="email" label="Email" value={data.email} />
			</div>
			<button
				class="h-10 rounded-md bg-[#3d5cff] px-4 text-sm whitespace-nowrap text-white hover:bg-[#2d4cf5]"
				aria-label="update email"
			>
				Update
			</button>
		</form>
	</div>
	<div class="bg-white dark:bg-[#2F2F42] pt-[24px] rounded-b-xl ">
		<div class="mr-auto ml-auto block justify-center items-center flex">
			<!-- Error Message -->
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
					<div class="ms-3 w-screen text-sm">{form.error}</div>
				</div>
			{/if}
			{#if form?.message}
				<div
					id="toast-success"
					class="mb-4 flex w-full max-w-xs items-center rounded-lg bg-[#F0F0F2] p-4 text-gray-500 shadow-sm dark:bg-gray-800 dark:text-gray-400"
					role="alert"
				>
					<div
						class="inline-flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-green-100 text-green-500 dark:bg-green-800 dark:text-green-200"
					>
						<svg
							class="h-5 w-5"
							aria-hidden="true"
							xmlns="http://www.w3.org/2000/svg"
							fill="currentColor"
							viewBox="0 0 20 20"
						>
							<path
								d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z"
							/>
						</svg>
						<span class="sr-only">Success icon</span>
					</div>
					<div class="ms-3 w-screen truncate text-sm">{form.message}</div>
				</div>
			{/if}
		</div>
	</div>
	<!-- Logout Button -->
	<form action="/logout" method="POST" class="mt-10 w-full">
		<button
			class="h-12 w-full rounded-xl bg-red-600 text-white transition hover:bg-red-700"
			aria-label="logout"
		>
			Logout
		</button>
	</form>
</div>
<Navigation/>
