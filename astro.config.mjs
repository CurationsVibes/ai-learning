import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	site: 'https://curationsla.github.io',
	base: '/ai-learning',
	integrations: [
		starlight({
			title: 'Curator Hub',
			description: 'Open-source frameworks, guides, and resources for AI development, collaboration, and creativity',
			social: {
				github: 'https://github.com/CurationsLA/ai-learning',
			},
			sidebar: [
				{
					label: '🏠 Welcome',
					items: [
						{ label: 'About Curator Hub', link: '/about-curator-hub/' },
						{ label: 'Get Involved', link: '/get-involved/' },
						{ label: 'Design Systems', link: '/design-systems/' },
						{ label: 'Technical Architecture', link: '/technical-architecture/' },
						{ label: 'The Curators', link: '/the-curators/' },
					],
				},
				{
					label: '🌱 Community',
					items: [
						{ label: 'About CurationsLA', link: '/about-curationsla/' },
						{ label: 'Youth Curator Movement', link: '/youth-curator-movement/' },
					],
				},
				{
					label: '📚 Cookbooks',
					collapsed: true,
					autogenerate: { directory: 'cookbooks' },
				},
			],
			customCss: [
				'./src/styles/custom.css',
			],
		}),
	],
});
