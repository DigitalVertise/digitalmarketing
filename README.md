# Digital Vertise — Revenue Launch

A static, SEO-focused digital marketing and AI solutions website for Digital Vertise.

## Included
- Conversion-led homepage and service positioning
- Ready-to-start product packages with starting prices
- Lead enquiry form using the visitor's email app (no paid form service/API)
- Mobile-responsive design, accessible navigation and metadata
- Existing Airtable JSON content preserved and generated into static SEO pages
- Sitemap, robots.txt, canonical URLs and basic ProfessionalService schema

## Build
Requires Node.js 18+. No npm dependencies.

```sh
node build.mjs
```

Output: `dist/`

## Commercial notes
Prices are indicative starting prices in USD for standard scopes. The final written proposal confirms deliverables, timeline and any third-party costs. Advertising spend and external software/messaging charges are not included unless explicitly stated.

## Deployment
Recommended zero-cost static hosting. Connect this repository and configure:
- Branch: `revenue-launch` (preview) or `main` (production)
- Build command: `node build.mjs`
- Publish directory: `dist`

Do not switch the production domain until the generated routes, forms, mobile layout and DNS are verified.
