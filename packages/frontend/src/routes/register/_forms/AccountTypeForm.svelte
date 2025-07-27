<script lang="ts">
	import { Button } from 'sk-clib';
	import { Input } from '@components';
	import { getStepsCtx } from '@components/steps/ctx.svelte';

	let { _helpers } = getStepsCtx();
</script>

<form class="box-border flex size-full flex-col" onsubmit={_helpers.next}>
	<Input class="mb-4" type="text" id="name_input" name="name" label="Full Name" />
	<select name="account_type">
		<option value="admin">Admin</option>
		<option value="teacher">Teacher</option>
		<option value="parent">Parent</option>
		<option value="student">student</option>
	</select>

	<Button type="submit" class="mb-4 cursor-pointer rounded-xl text-white">Continue</Button>
</form>
