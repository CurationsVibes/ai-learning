import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

/**
 * Capitalize directory names for sidebar display
 * Transforms: "advanced-prompting" → "Advanced Prompting"
 */
function capitalizeSidebarLabel(label) {
	return label
		.split('-')
		.map(word => word.charAt(0).toUpperCase() + word.slice(1))
		.join(' ');
}

// https://astro.build/config
export default defineConfig({
	site: 'https://hub.curations.org',
	base: '/',
	integrations: [
		starlight({
			title: 'HUB',
			description: 'A comprehensive knowledge wiki and AI learning resource by CURATIONS — a Human × AI Creative Agency in Los Angeles. Explore frameworks, guides, and open-source resources for AI development, collaboration, and creativity.',
			tagline: 'BY CURATIONS',
			social: [
				{ icon: 'github', label: 'GitHub', href: 'https://github.com/CurationsLA/ai-learning' },
			],
			pagefind: true,
			components: {
				PageFrame: './src/overrides/PageFrame.astro',
				Header: './src/overrides/Header.astro',
			},
			head: [
				{
					tag: 'meta',
					attrs: { property: 'og:type', content: 'website' },
				},
				{
					tag: 'meta',
					attrs: { property: 'og:site_name', content: 'HUB by CURATIONS' },
				},
				{
					tag: 'meta',
					attrs: { name: 'twitter:card', content: 'summary_large_image' },
				},
				{
					tag: 'meta',
					attrs: { name: 'keywords', content: 'AI learning, AI frameworks, Human AI collaboration, AI development, creative AI, CURATIONS, knowledge wiki, AI resources' },
				},
				{
					tag: 'link',
					attrs: { rel: 'canonical', href: 'https://hub.curations.org/' },
				},
				{
					tag: 'script',
					attrs: { type: 'application/ld+json' },
					content: JSON.stringify({
						'@context': 'https://schema.org',
						'@type': 'WebSite',
						name: 'HUB',
						alternateName: 'HUB by CURATIONS',
						url: 'https://hub.curations.org/',
						description: 'A comprehensive knowledge wiki and AI learning resource by CURATIONS',
						publisher: {
							'@type': 'Organization',
							name: 'CURATIONS',
							url: 'https://curations.org',
							description: 'A Human × AI Creative Agency in Los Angeles',
							address: {
								'@type': 'PostalAddress',
								addressLocality: 'Los Angeles',
								addressRegion: 'CA',
								addressCountry: 'US'
							}
						},
						inLanguage: 'en-US',
						potentialAction: {
							'@type': 'SearchAction',
							target: 'https://hub.curations.org/?search={search_term_string}',
							'query-input': 'required name=search_term_string'
						}
					})
				},
			],
			sidebar: [
				{
					label: '🏠 Welcome',
					items: [
						{ label: 'About HUB', link: '/about-hub/' },
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
					items: [
						{
							label: 'Advanced',
							collapsed: true,
							autogenerate: { directory: 'cookbooks/advanced' },
						},
						{
							label: 'Advanced Prompting',
							collapsed: true,
							autogenerate: { directory: 'cookbooks/advanced-prompting' },
						},
						{
							label: 'Agents',
							collapsed: true,
							autogenerate: { directory: 'cookbooks/agents' },
						},
						{
							label: 'Beginners',
							collapsed: true,
							autogenerate: { directory: 'cookbooks/beginners' },
						},
						{
							label: 'Business',
							collapsed: true,
							autogenerate: { directory: 'cookbooks/business' },
						},
						{
							label: 'Foundations',
							collapsed: true,
							autogenerate: { directory: 'cookbooks/foundations' },
						},
						{
							label: 'Intermediate',
							collapsed: true,
							autogenerate: { directory: 'cookbooks/intermediate' },
						},
						{
							label: 'Legendary',
							collapsed: true,
							autogenerate: { directory: 'cookbooks/legendary' },
						},
						{
							label: 'Personal Use',
							collapsed: true,
							autogenerate: { directory: 'cookbooks/personal-use' },
						},
						{
							label: 'RAG',
							collapsed: true,
							autogenerate: { directory: 'cookbooks/rag' },
						},
						{ label: '🧠 The AI × Human Cookbook', link: '/cookbooks/readme/' },
						{
							label: 'Tools',
							collapsed: true,
							autogenerate: { directory: 'cookbooks/tools' },
						},
					],
				},
			],
			customCss: [
				'./src/styles/curations-brand.css',
				'./src/styles/custom.css',
			],
		}),
	],
});
