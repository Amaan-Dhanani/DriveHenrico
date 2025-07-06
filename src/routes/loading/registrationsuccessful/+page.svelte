<script lang="ts">
  import '$lib/css/app.css';
	import Spinner from "$lib/components/Spinner.svelte";

  //   setTimeout(() => {
  //     window.location.href = '/login';  // Redirect to the desired URL
  //   }, 1000);  // 1000 milliseconds = 1 second
</script>
<Spinner/>
<div class="rounded-[12px] bg-black w-[290px]">
<svg class="ml-auto mr-auto block" xmlns="http://www.w3.org/2000/svg" width="65" height="65" viewBox="0 0 65 65" fill="none">
  <path d="M64.5 32.5C64.5 14.8269 50.1731 0.5 32.5 0.5C14.8269 0.5 0.5 14.8269 0.5 32.5C0.5 50.1731 14.8269 64.5 32.5 64.5C50.1731 64.5 64.5 50.1731 64.5 32.5Z" fill="#3D5CFF"/>
  <path d="M18.4512 32.7724L27.6882 42.0094L46.5512 23.1504" stroke="white" stroke-width="4.401" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
<p class="text-center text-white text-bold mt-[10px]">Success!</p>

</div>