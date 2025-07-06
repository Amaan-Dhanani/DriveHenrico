<script lang="ts">
	import Icon from './components/Icon.svelte';
	export let number;
	//START AREAS TO CHANGE
	let paths1 = '<path fill="" d="M5.216 11.998a2.608 2.608 0 1 1-5.217 0a2.608 2.608 0 0 1 5.217 0m0-9.39a2.608 2.608 0 1 1-5.217 0a2.608 2.608 0 0 1 5.217 0m0 18.781a2.608 2.608 0 1 1-5.217 0a2.608 2.608 0 0 1 5.217 0M9.794 0h15.247a2.61 2.61 0 1 1 0 5.22H9.794a2.61 2.61 0 1 1 0-5.22m0 9.39h15.247a2.61 2.61 0 1 1 0 5.22H9.794a2.61 2.61 0 1 1 0-5.22m0 9.391h15.247a2.61 2.61 0 1 1 0 5.22H9.794a2.61 2.61 0 1 1 0-5.22"/>';
	let paths2 = '<path d="M32 20a8 8 0 1 1-16 0a8 8 0 0 1 16 0"/><path d="M23.184 43.984C12.517 43.556 4 34.772 4 24C4 12.954 12.954 4 24 4s20 8.954 20 20s-8.954 20-20 20h-.274q-.272 0-.542-.016M11.166 36.62a3.028 3.028 0 0 1 2.523-4.005c7.796-.863 12.874-.785 20.632.018a2.99 2.99 0 0 1 2.498 4.002A17.94 17.94 0 0 0 42 24c0-9.941-8.059-18-18-18S6 14.059 6 24c0 4.916 1.971 9.373 5.166 12.621"/>';
	let paths3 = '<path fill="transparent" d="m12.593 23.258l-.011.002l-.071.035l-.02.004l-.014-.004l-.071-.035q-.016-.005-.024.005l-.004.01l-.017.428l.005.02l.01.013l.104.074l.015.004l.012-.004l.104-.074l.012-.016l.004-.017l-.017-.427q-.004-.016-.017-.018m.265-.113l-.013.002l-.185.093l-.01.01l-.003.011l.018.43l.005.012l.008.007l.201.093q.019.005.029-.008l.004-.014l-.034-.614q-.005-.018-.02-.022m-.715.002a.02.02 0 0 0-.027.006l-.006.014l-.034.614q.001.018.017.024l.015-.002l.201-.093l.01-.008l.004-.011l.017-.43l-.003-.012l-.01-.01z"/><path fill="" d="M21.546 5.111a1.5 1.5 0 0 1 0 2.121L10.303 18.475a1.6 1.6 0 0 1-2.263 0L2.454 12.89a1.5 1.5 0 1 1 2.121-2.121l4.596 4.596L19.424 5.111a1.5 1.5 0 0 1 2.122 0"/>';
	let paths4 = '<path fill="" fill-rule="evenodd" d="M2.146 11.146a.5.5 0 0 0 .708.708l4-4a.5.5 0 0 0 0-.708l-4-4a.5.5 0 1 0-.708.708L5.793 7.5zm6 0a.5.5 0 0 0 .708.708l4-4a.5.5 0 0 0 0-.708l-4-4a.5.5 0 1 0-.708.708L11.793 7.5z" clip-rule="evenodd"/>';
	//END AREAS TO CHANGE
</script>
<div class="fixed left-0 right-0 -bottom-0 z-10 w-full">
	<div class="flex h-[118px] w-full flex-row items-end justify-around">
		<div class="absolute -z-100 h-[95px] w-full rounded-t-[30px] bg-[#ccc] dark:bg-[#3E3E55]"></div>
		<!-- START AREAS TO CHANGE -->
		{#if number || number!=0}
		<Icon text="Navigate" viewbox="0 0 28 24" paths={paths1} fill="#c026d3" link="/create/navigate"/>
		{/if}
		<Icon text="Home" link="/dashboard" viewbox="0 0 48 48" paths={paths2} fill="#c026d3"/>
		{#if number || number!=0}
		<Icon text="Submit" viewbox="0 0 24 24" link="/create/submit" paths={paths3} fill="#c026d3"/>
		{/if}
		{#if number!=10}
		<Icon text="Question {number + 1}" viewbox="0 0 15 15" paths={paths4} link="/create/question{number +1}" fill="#c026d3"/>
		{/if}
		<!-- END AREAS TO CHANGE -->
	</div>
</div>
