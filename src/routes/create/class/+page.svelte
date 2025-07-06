<script lang="ts">
	import { Input } from '$lib/components';
	import { enhance } from '$app/forms';
	import '$lib/css/app.css';
	import { goto } from '$app/navigation';
	export let form;
	import { Logo } from '$lib/components';
	let submit = false;
	let id_input: HTMLInputElement;

	async function copyText() {
		let textToCopy = "";
		const inputElement = document.getElementById("id_input") as HTMLInputElement | null;

		if (inputElement) {
			textToCopy = inputElement.value || "";
		}

        await navigator.clipboard.writeText(textToCopy);
	}
</script>

<!-- Full screen container -->
<div
	class="fixed inset-0 -z-[100] mt-[100vh] h-[300vh] w-screen overflow-hidden bg-[#4c4c61] dark:bg-[#1F1F39]"
></div>
<div class="mr-[1rem] ml-[1rem] flex min-h-screen flex-col bg-[#4c4c61] dark:bg-[#1F1F39]">
	<!-- Header -->
	 <Logo/>
	<h1 class="mb-0 ml-[5px] pt-[86px] text-[32px] font-bold text-white">Create a Class</h1>
	<p class="mt-0 mb-[10px] ml-[5px] text-[12px] text-[#B8B8D2]"></p>
	<!-- Form Section -->
	<div
		class="mb-[95px] box-border flex flex-grow flex-col gap-4 rounded-t-2xl bg-white px-6 py-8 dark:bg-[#2F2F42]"
	>
		{#if submit == false}
			<div class="gap-0 dark:text-white">
				<h2 class="mt-0 text-[16px]">
					Alright! All you have to do is press that button!
				</h2>
				<form
					method="POST"
					autocomplete="off"
					use:enhance
					on:submit|preventDefault={() => (submit = true)}
					class="box-border flex flex-grow flex-col rounded-t-2xl bg-white px-6 dark:bg-[#2F2F42]"
				>
					<Input
						id="fake"
						name="fake"
						value="Random Value"
						readonly
						required
						class="invisible h-[0px] p-0 readonly"
					/>
					<button
						type="submit"
						class="mt-[20px] h-12 w-full rounded-xl bg-[#3d5cff] text-center text-white hover:cursor-pointer"
					>
						Create a Class
					</button>
					
				</form>
				<button
			class="h-12 w-full mb-[10px] mt-[20px] rounded-xl bg-red-600 text-white transition hover:bg-red-700"
			aria-label="back" on:click={() => goto('/dashboard')}
		>
			Back
		</button>

				<hr class="dark:border-white" />
			</div>
			{:else}
			<h2 class="mt-0 text-[16px] dark:text-white">
				Great Job! This is your ID that you can use to to other people so they can join your class!
				<div class="flex flex-row items-end gap-4 rounded-t-xl bg-white p-6 pb-0 dark:bg-[#2F2F42]">
					<div class="flex-1">
						<Input
							type="text"
							label="QuestID"
							id="id_input"
							name="id_input"
							value={form?.classID}
							readonly
						/>
					</div>
					<button
						on:click={copyText}
						class="h-10 rounded-md bg-[#3d5cff] px-4 text-sm whitespace-nowrap text-white hover:bg-[#2d4cf5]"
						aria-label="copy"
					>
						Copy
					</button>
				</div>
			</h2>
			<hr class="dark:border-white" />
			<button
						class="h-10 rounded-md w-full bg-[red] px-4 text-sm whitespace-nowrap text-white hover:bg-[#2d4cf5]"
						aria-label="back to home" on:click={() => goto('/dashboard')}
					>
						Back to Home
					</button>
		{/if}
	</div>
</div>
