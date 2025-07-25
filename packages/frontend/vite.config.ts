import tailwindcss from '@tailwindcss/vite';
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import Icons from 'unplugin-icons/vite';

export default defineConfig({
	plugins: [sveltekit(), tailwindcss(), Icons({ autoInstall: true, compiler: 'svelte' })],
	server: {
		allowedHosts: true
	}
});
