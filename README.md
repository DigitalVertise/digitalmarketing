# Digital Vertise website rebuild

Reconstruction source for the Digital Vertise website, using the publicly accessible Duda preview and existing Airtable page content. No Duda subscription or paid infrastructure is required for the source/build workflow.

## What is in this repository

- `index.html` — responsive rebuilt homepage.
- `assets/site.css` — responsive visual system and layout.
- `assets/site.js` — small client-side enhancement.
- `build.mjs` — static page generator.
- `data/services.json` — 54 Airtable WebsiteServices records.
- `data/sectors.json` — 23 Airtable sector records.
- `data/industries.json` — 148 Airtable industry records.
- `data/countries.json` — 225 Airtable country records.
- `migration/duda-preview-pages.json` — extracted preview homepage and migration inventory.

## Build

Requires Node.js 18+; no npm dependencies.

```sh
node build.mjs
```

The build creates `dist/`, copies the source/data assets and generates static SEO pages from the Airtable records, plus `sitemap.xml` and `robots.txt`.

## Free hosting target

Use **Cloudflare Pages Free** for the commercial website. Connect this GitHub repository and configure:

- Build command: `node build.mjs`
- Build output directory: `dist`
- Root directory: `/`

GitHub Pages is not the production target because GitHub's terms restrict using its free Pages hosting to run an online business. Cloudflare Pages offers a free static-hosting tier; review current plan limits before deployment.

## Migration status

- Rebuilt homepage and shared page template committed.
- All 450 records from the four identified Airtable website tables exported into the repository.
- 499 preview URL entries were discovered in the site map.
- The homepage was extracted successfully. Other page extraction was intermittent, so full parity with every original Duda page is not yet verified.
- This is a reconstruction, not an original Duda source export. Original Duda editor settings, CMS configuration, forms/integrations and binary assets not publicly exposed by the preview are not included.

## Next verification

Run the build, inspect generated routes against the original URL inventory, then connect Cloudflare Pages. Confirm custom-domain DNS before switching `digitalvertise.com`.
