<script lang="ts">
	import { onMount } from 'svelte';
	import { getRegisterCtx } from '../ctx.svelte';
	import { CodeInput } from '@components';
	import { Button } from 'sk-clib';
	import { TextRedactor } from '@components';
	import { Text } from '@lib/ui';

	const { _state, _user_input, _verification_state } = getRegisterCtx();

	onMount(() => {
		const { email, password, account_type, name } = _user_input;
		_state.ws?.send('auth:signup:post', { email, password, account_type, name });
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

<form class="box-border flex size-full flex-col gap-4" {onsubmit}>
	<span class="text-center dark:text-white">Verify Code</span>

	<Text class="text-center text-sm">We just emailed a code to <TextRedactor text={_user_input.email} class="text-primary"/>. Please check your inbox. If it isn't found, it could be in your spam.</Text>
	<CodeInput classWrapper="pb-[3px]" name="code"/>

	<Button type="submit" class="mb-4 cursor-pointer rounded-xl text-white">Continue</Button>
</form>

