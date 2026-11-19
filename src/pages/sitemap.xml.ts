import type { APIRoute } from 'astro';
import { FAQS_DATA } from '../data/faqs';
import { AIRPORTS_DATA } from '../data/airports';
import { TUTORIALS_DATA } from '../data/tutorials';

export const GET: APIRoute = async () => {
  const baseUrl = 'https://jichangxuanze.lat';
  const currentDate = new Date().toISOString().split('T')[0];

  const staticPages = [
    { url: '/', priority: '1.0', changefreq: 'daily' },
    { url: '/rankings/', priority: '0.9', changefreq: 'weekly' },
    { url: '/reviews/', priority: '0.9', changefreq: 'weekly' },
    { url: '/faq/', priority: '0.9', changefreq: 'daily' },
    { url: '/tutorials/', priority: '0.8', changefreq: 'monthly' },
    { url: '/promotions/', priority: '0.8', changefreq: 'daily' },
    { url: '/about/', priority: '0.6', changefreq: 'monthly' },
  ];

  // 14 airports reviews
  const airportPages = AIRPORTS_DATA.map((airport) => ({
    url: `/reviews/${airport.reviewSlug || airport.slug}/`,
    priority: '0.85',
    changefreq: 'weekly',
  }));

  // 4 tutorials
  const tutorialPages = TUTORIALS_DATA.map((tut) => ({
    url: `/tutorials/${tut.slug}/`,
    priority: '0.8',
    changefreq: 'monthly',
  }));

  // 150 FAQs
  const faqPages = FAQS_DATA.map((faq) => ({
    url: `/faq/${faq.slug}/`,
    priority: '0.8',
    changefreq: 'weekly',
  }));

  const allUrls = [...staticPages, ...airportPages, ...tutorialPages, ...faqPages];

  const sitemapXml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${allUrls
  .map(
    (item) => `  <url>
    <loc>${baseUrl}${item.url}</loc>
    <lastmod>${currentDate}</lastmod>
    <changefreq>${item.changefreq}</changefreq>
    <priority>${item.priority}</priority>
  </url>`
  )
  .join('\n')}
</urlset>`;

  return new Response(sitemapXml, {
    status: 200,
    headers: {
      'Content-Type': 'application/xml; charset=utf-8',
      'Cache-Control': 'public, max-age=86400',
    },
  });
};
