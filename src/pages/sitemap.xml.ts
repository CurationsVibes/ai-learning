// Generate dynamic sitemap for CURATOR HUB
// This runs at build time to create an up-to-date sitemap.xml
import { getCollection } from 'astro:content';
import type { APIRoute } from 'astro';

export const GET: APIRoute = async () => {
  const docs = await getCollection('docs');
  const baseUrl = 'https://hub.curations.org';

  // Priority mapping based on content type
  const getPriority = (slug: string): string => {
    if (slug === '' || slug === 'index') return '1.0';
    if (slug.startsWith('cookbooks/')) return '0.8';
    if (slug.includes('about-') || slug === 'get-involved') return '0.9';
    return '0.7';
  };

  // Change frequency based on content type
  const getChangeFreq = (slug: string): string => {
    if (slug === '' || slug === 'index') return 'weekly';
    if (slug.startsWith('cookbooks/')) return 'monthly';
    return 'monthly';
  };

  const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:news="http://www.google.com/schemas/sitemap-news/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"
        xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">
  
  <!-- Homepage -->
  <url>
    <loc>${baseUrl}/</loc>
    <lastmod>${new Date().toISOString()}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>

  ${docs.map(doc => `  <url>
    <loc>${baseUrl}/${doc.slug}/</loc>
    <lastmod>${new Date().toISOString()}</lastmod>
    <changefreq>${getChangeFreq(doc.slug)}</changefreq>
    <priority>${getPriority(doc.slug)}</priority>
  </url>`).join('\n')}

</urlset>`;

  // Return XML with proper content type
  return new Response(sitemap, {
    headers: {
      'Content-Type': 'application/xml; charset=utf-8',
      'Cache-Control': 'max-age=3600'
    }
  });
};
