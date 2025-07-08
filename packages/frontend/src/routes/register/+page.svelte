<script lang="ts">
	import { enhance } from '$app/forms';
	import { Input } from '$lib';
	import { RadioHorizontal } from '$lib';
    let selected = '';


    //No error system set up yet
    let error = 'No error detection system set up yet. Sample error. Other things to note: it works perfectly on a mobile device but but need work on computer. Make sure to check components and edit any code as needed. Need to make deafult font Poppins.';
</script>

<!-- Full screen container -->
<div
	class="fixed inset-0 -z-[100] mt-[100vh] h-[300vh] w-screen overflow-hidden bg-[#F0F0F2] dark:bg-[#1F1F39]"
></div>
<div class="mr-[1rem] ml-[1rem] flex min-h-screen flex-col bg-[#F0F0F2] dark:bg-[#1F1F39]">
	<!-- Header -->
	<h1 class="mb-0 ml-[5px] pt-[86px] text-[32px] font-bold dark:text-white">Get Started</h1>
	<p class="mt-0 mb-[10px] ml-[5px] text-[12px] text-[#B8B8D2]">
		Enter your details below to start your journey!
	</p>

	<!-- Form Section -->
	<form
		method="POST"
		autocomplete="off"
		use:enhance
		class="box-border flex flex-grow flex-col gap-4 rounded-t-2xl bg-white px-6 py-8 dark:bg-[#2F2F42]"
	>
		<div>
			<Input
				type="text"
				id="name_input"
				name="name"
				label="Name"
				class=""
			/>
		</div>
		<div>
			<Input
				type="email"
				id="email_input"
				name="email"
				label="Email"
			/>
		</div>
		<div>
			<Input
				type="password"
				class="mb-[12px]"
				id="password_input"
				label="Password"
				name="password"
			/>
		</div>
		<div>
			<RadioHorizontal
			label="Account Type"
				name="access"
				bind:selected={selected}
				options={[
					{ value: 'Student' },
					{ value: 'Parent' },
                    { value: 'Teacher' }
				]}
			/>
		</div>

		<!-- Submit Button -->
		<button class="h-12 w-full rounded-xl bg-[#3d5cff] text-center text-white hover:cursor-pointer">
			Register
		</button>

		<!-- Sign In Link -->
		<p class="text-center text-[14px] text-[#858597]">
			Already have an account? <a class="font-bold text-[#3D5CFF] underline" href="/login"
				>Sign In</a
			>
		</p>
		<div class="mt-10 flex flex-col items-center justify-center text-center">
			<!-- Optional messages -->
			{#if error}
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
					<div class="ms-3 text-sm">{error}</div>
				</div>
			{/if}
		</div>
	</form>
</div>
