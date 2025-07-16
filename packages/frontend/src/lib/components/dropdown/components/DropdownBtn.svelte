<script>
  import { cn } from '$lib/utils';

  export let type = 'link';
  export let link = '';
  export let className = '';        // rename from 'class'
</script>

{#if type === 'link'}
  <a
    href={link}
    class={cn("block text-sm text-gray-700 py-2 px-4", className)}
    role="menuitem"
  >
    <slot />
  </a>
{:else if type === 'divider'}
  <hr class={cn("border-gray-200 dark:border-gray-600 h-[1px]", className)} />
{/if}
