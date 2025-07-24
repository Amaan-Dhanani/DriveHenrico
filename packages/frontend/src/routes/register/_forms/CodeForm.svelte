<script lang="ts">
	import { onMount } from 'svelte';
	import { getRegisterCtx } from '../ctx.svelte';
	import { CodeInput } from '@components';
	import { Button } from 'sk-clib';

	const { _state, _user_input, _verification_state } = getRegisterCtx();

	onMount(() => {
		const { email, password, account_type } = _user_input;
		_state.ws?.send('auth:signup:post', { email, password, account_type });
	});

	type CodeFormData = {
		code?: string;
	};

	async function onsubmit(event: Event) {
		event.preventDefault(); // Stop default behavior
		const formData: CodeFormData = Object.fromEntries(
			new FormData(event.target as HTMLFormElement)
		);
		const { code } = formData;

		if (!code) {
			throw new Error('Missing code');
		}

		_user_input.code = code;
        
        if (!_verification_state.id) {
            throw new Error('Missing Verification')
        }

        _state.ws?.send('auth:signup:confirm_code', {
            id: _verification_state.id,
            code
        })

	}
</script>

<form class="box-border flex size-full flex-col" {onsubmit}>
	<span>Haha this is the code form :)</span>

	<CodeInput classWrapper="pb-[3px]" name="code"/>

	<Button type="submit" class="mb-4 cursor-pointer rounded-xl text-white">Continue</Button>
</form>

