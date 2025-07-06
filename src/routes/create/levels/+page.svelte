<script lang="ts">
  import { LvlBox } from "$lib/components";
  export let data: { real_lvl: number | null };

  const levels = Array.from({ length: 50 }, (_, i) => i + 1);

  // Split levels into chunks of 3
  function chunk(arr: number[], size: number): number[][] {
    const result = [];
    for (let i = 0; i < arr.length; i += size) {
      result.push(arr.slice(i, i + size));
    }
    return result;
  }

  const levelRows = chunk(levels, 3);
</script>
<br>
<div class="flex flex-col items-center space-y-4">
  {#each levelRows as row}
    <div class="flex gap-x-4" class:justify-center={row.length < 3}>
      {#each row as level}
        <LvlBox
          new_lvl={level === ((data.real_lvl ?? 0) + 1) ? "yes" : ""}
          number={level}
          lock={data.real_lvl !== null && level <= (data.real_lvl + 1) ? "false" : "true"}
        />
      {/each}
    </div>
  {/each}
</div>
