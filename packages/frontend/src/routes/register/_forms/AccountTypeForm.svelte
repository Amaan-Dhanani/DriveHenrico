<script lang="ts">
	import { Button } from 'sk-clib';
	import { getRegisterCtx } from '../ctx.svelte';

	let { _state, _user_input } = getRegisterCtx();

	type AccountTypeFormData = {
		account_type?: string;
	};

	async function onsubmit(event: Event) {
		event.preventDefault(); // Stop default behavior
		const formData: AccountTypeFormData = Object.fromEntries(
			new FormData(event.target as HTMLFormElement)
		);
		const { account_type } = formData;

		if (!account_type) {
			throw new Error('Missing account_type');
		}
        
        _user_input.account_type = account_type;

		// Prompt Step Change
		_state.step = 'code';
	}
</script>

<form class="box-border flex size-full flex-col" {onsubmit}>
	<select name="account_type">
		<option value="admin">Admin</option>
		<option value="teacher">Teacher</option>
		<option value="parent">Parent</option>
		<option value="student">student</option>
	</select>

    <Button type="submit" class="mb-4 cursor-pointer rounded-xl text-white">Continue</Button>
</form>
