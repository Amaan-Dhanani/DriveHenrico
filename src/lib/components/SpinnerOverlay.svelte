<script>
	import Spinner from "./Spinner.svelte";
	import { onMount } from "svelte";

	let showSpinner = true;

	onMount(() => {
		// Hide the spinner after 500ms (half a second)
		setTimeout(() => {
			showSpinner = false;
		}, 500);
	});
</script>

{#if showSpinner}
	<div class="overlay">
        <br><br><br><br><br><br><br><br><br><br><br><br><br>
		<Spinner/>
	</div>
{/if}

<style>
	.overlay {
        transform: translateX(-16px);
		z-index: 9999;
		background-color: #131317;
        display: block;
        margin-right: auto;
        margin-left: auto;
        width: 101%;
        height: 200%;
		position: fixed; /* Ensure the overlay is on top */
	}
</style>
