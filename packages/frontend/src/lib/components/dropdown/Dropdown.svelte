<script>
  import DropdownBtn from './components/DropdownBtn.svelte';
  import { onMount } from 'svelte';

  let isOpen = false;

  function toggle() {
    isOpen = !isOpen;
  }

  function handleClickOutside(event) {
    if (!event.target.closest('.dropdown')) {
      isOpen = false;
    }
  }

  onMount(() => {
    document.addEventListener('click', handleClickOutside);
    return () => {
      document.removeEventListener('click', handleClickOutside);
    };
  });
</script>

<div class="flex items-center justify-center">
  <div class="relative inline-block text-left dropdown">
    <!-- Toggle button -->
    <button
      on:click={toggle}
      class="inline-flex justify-center w-full px-4 py-2 text-sm font-medium leading-5 text-gray-700 transition duration-150 ease-in-out bg-white border border-gray-300 rounded-md hover:text-gray-500 focus:outline-none"
      type="button"
      aria-haspopup="true"
      aria-expanded={isOpen}
    >
      <span>Options</span>
      <svg class="w-5 h-5 ml-2 -mr-1" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
        <path
          fill-rule="evenodd"
          d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
          clip-rule="evenodd"
        />
      </svg>
    </button>

    <!-- Dropdown menu -->
    <div
      class={`absolute w-56 mt-2 origin-top-right bg-white border border-gray-200 divide-y divide-gray-100 rounded-md shadow-lg outline-none transition-all duration-300 transform ${
        isOpen
          ? 'opacity-100 visible translate-y-0 scale-100'
          : 'opacity-0 invisible -translate-y-2 scale-95'
      }`}
      role="menu"
    >
    <slot/>
    </div>
  </div>
</div>
