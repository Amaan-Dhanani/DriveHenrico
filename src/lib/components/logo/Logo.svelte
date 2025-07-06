<script>
  import QuestOwl from '$lib/images/QuestOwl.png';
  import QuestOwlAlt from '$lib/images/QuestOwlAlt.png'; // make sure this path is correct
  import '$lib/css/app.css';
  export let alt = false;
</script>

<img 
  src={alt ? QuestOwlAlt : QuestOwl} 
  alt="QuestOwl Logo"
  class="w-[100px] fixed top-4 right-4 z-[9999]"
/>
