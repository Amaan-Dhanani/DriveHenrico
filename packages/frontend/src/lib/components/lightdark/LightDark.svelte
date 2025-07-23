<script lang="ts">
	import Dark from '~icons/ic/round-dark-mode';
	import Light from '~icons/ic/round-light-mode';
	import { Flex } from 'sk-clib';
	import { Dropdown } from '@components';
	import { global_mode$ } from './mode';
	import { type Writable } from 'svelte/store';
	import DropdownDivider from '../dropdown/components/dropdown-divider.svelte';

	let mode$: Writable<'dark' | 'light' | string> = global_mode$.mode$;

	const setMode = (mode: 'dark' | 'light') => {
		if (localStorage.getItem("mode") !== mode) global_mode$.toggle();
	};
</script>

<Dropdown.Menu class="pt-2">
	<Dropdown.Trigger>
		<Dropdown.Button class="w-fit">Theme</Dropdown.Button>
	</Dropdown.Trigger>

	<Dropdown.Content class="w-36">
		<Dropdown.Button onclick={() => setMode('light')}>
			<Flex class="items-center pl-6 gap-1">
				<Light />
                Light
			</Flex>
		</Dropdown.Button>

		<DropdownDivider border=""/>

		<Dropdown.Button onclick={() => setMode('dark')}>
			<Flex class="items-center pl-6 gap-1">
				<Dark/>
                Dark
			</Flex>
		</Dropdown.Button>
	</Dropdown.Content>
</Dropdown.Menu>
