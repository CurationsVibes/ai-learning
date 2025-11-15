import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	site: 'https://curationsla.github.io',
	base: '/ai-learning',
	integrations: [
		starlight({
			title: 'VibeHub',
			description: 'Open-source frameworks, guides, and resources for AI development, collaboration, and creativity',
			social: {
				github: 'https://github.com/CurationsLA/ai-learning',
			},
			sidebar: [
				{
					label: '🏠 Welcome to VibeHub',
					items: [
						{ label: 'About VibeHub', link: '/about-vibehub/' },
					],
				},
			],
			customCss: [
				'./src/styles/custom.css',
			],
		}),
	],
});
