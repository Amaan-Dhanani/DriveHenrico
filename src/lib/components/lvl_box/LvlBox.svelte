<script lang="ts">
  export let lock: string;
  export let number: number;
  export let new_lvl: string;
  import { goto } from "$app/navigation";
</script>

{#if lock === 'false'}
  {#if new_lvl=='yes'}
  <!-- svelte-ignore a11y_click_events_have_key_events -->
  <!-- svelte-ignore a11y_no_static_element_interactions -->
  <div class="flex justify-center items-center h-20 w-20 rounded bg-teal-700 text-white font-bold text-xl"  on:click={() => goto(`/create/levels/level${number}`)}>
    {number}
  </div>
  {:else}
  <!-- svelte-ignore a11y_click_events_have_key_events -->
  <!-- svelte-ignore a11y_no_static_element_interactions -->
  <div class="flex justify-center items-center h-20 w-20 rounded bg-indigo-700 text-white font-bold text-xl"  on:click={() => goto(`/create/levels/level${number}`)}>
    {number}
  </div>
  {/if}



{:else}
<div class="flex justify-center items-center h-20 w-20 rounded bg-[green] text-white font-bold text-xl">
    {number}
  </div>
{/if}
