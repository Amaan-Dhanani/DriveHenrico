<script lang="ts">

	export let text = '';
	export let paths = '';
	export let viewbox = '';
	export let center = 'false';
	export let stroke = '';
	export let fill = 'none';
	export let link = '';
</script>

{#if center == 'true'}
	<!-- svelte-ignore a11y_click_events_have_key_events -->
	<!-- svelte-ignore a11y_no_static_element_interactions -->
	<div on:click={() => location.replace(link)} class="flex h-[118px] w-[100px] flex-col items-center justify-center cursor-pointer rounded-t-[50%] bg-[#ccc] dark:bg-[#3E3E55]">
		<!-- SVG Icon -->
		<svg
			xmlns="http://www.w3.org/2000/svg"
			viewBox={viewbox}
			width="70"
			height="70"
			stroke={stroke}
			fill={fill}
			aria-label={text}
			role="img"
		>
			{@html paths}
		</svg>

		<!-- Label -->
		<p class="text-center text-[15px] dark:text-[#ccc]">{text}</p>
	</div>
{:else}
<!-- svelte-ignore a11y_click_events_have_key_events -->
<!-- svelte-ignore a11y_no_static_element_interactions -->
<div on:click={() => location.replace(link)} class="flex h-[95px] flex-col items-center justify-center cursor-pointer">
	<!-- SVG Icon -->
	<svg
		xmlns="http://www.w3.org/2000/svg"
		viewBox={viewbox}
		width="50"
		height="50"
		stroke={stroke}
		fill={fill}
		aria-label={text}
		role="img"
	>
		{@html paths}
	</svg>

	<!-- Label -->
	<p class="text-center text-[15px] dark:text-[#ccc]">{text}</p>
</div>
{/if}