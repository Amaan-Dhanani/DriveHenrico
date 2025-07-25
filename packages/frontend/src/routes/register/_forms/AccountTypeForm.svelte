<script lang="ts">
	import { Button } from 'sk-clib';
	import { Input } from '@lib/components';
	import { getRegisterCtx } from '../ctx.svelte';

	let { _state, _user_input } = getRegisterCtx();

	type AccountTypeFormData = {
		account_type?: string;
		name?: string;
	};

	async function onsubmit(event: Event) {
		event.preventDefault(); // Stop default behavior
		const formData: AccountTypeFormData = Object.fromEntries(
			new FormData(event.target as HTMLFormElement)
		);
		const { account_type, name } = formData;

		if (!account_type) {
			throw new Error('Missing account_type');
		}
		if (!name) {
			throw new Error('Missing name');
		}
        
        _user_input.account_type = account_type;
		_user_input.name = name;

		// Prompt Step Change
		_state.step = 'code';
	}
</script>

<form class="box-border flex size-full flex-col" {onsubmit}>
	<Input class="mb-4" type="text" id="name_input" name="name" label="Full Name" />
	<select name="account_type">
		<option value="admin">Admin</option>
		<option value="teacher">Teacher</option>
		<option value="parent">Parent</option>
		<option value="student">student</option>
	</select>

    <Button type="submit" class="mb-4 cursor-pointer rounded-xl text-white">Continue</Button>
</form>
