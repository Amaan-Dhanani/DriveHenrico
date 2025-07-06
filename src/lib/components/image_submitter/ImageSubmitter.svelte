<script lang="ts">
  export let id = '';
  export let name = '';
  export let placeholder = 'Click above me to upload an image!';
  export let dataURI: string = ''; // bindable
  import Input from "../input/components/input.svelte";
  let inputPlaceholder = placeholder;

  function handleFileChange(event: Event) {
  const input = event.target as HTMLInputElement;
  const file = input?.files?.[0];

  if (!file) {
    dataURI = '';
    inputPlaceholder = placeholder;
    return;
  }

  if (/^image\//.test(file.type)) {
    const reader = new FileReader();
    reader.onload = () => {
      dataURI = reader.result as string;
    };
    reader.readAsDataURL(file);
  } else {
    input.value = '';
    inputPlaceholder = "Only image files are accepted.";
    dataURI = '';
  }
}

</script>

  <label for={id} class="mb-2 inline-block text-neutral-500 dark:text-neutral-400 invisible"></label>
  <input
    class="rounded-b-[0px] file:text-left dark:bg-[#3E3E55] bg-gray-200 file:w-full rounded-t-[10px] flex-auto cursor-pointer border border-secondary-500 px-3 py-[0.32rem] file:text-black dark:file:text-white file:-my-[0.32rem] file:me-3 file:cursor-pointer file:overflow-hidden file:border-0 file:border-solid file:border-inherit file:px-3 file:py-[0.32rem] dark:border-white file:dark:text-white"
    type="file"
    id={id}
    accept="image/*"
    on:change={handleFileChange}
  />

<Input
  class="select-none border border-black bg-gray-200 rounded-t-[0px] dark:border-white dark:border"
  type="text"
  {id}
  {name}
  placeholder={inputPlaceholder}
  value={dataURI}
  readonly
/>

