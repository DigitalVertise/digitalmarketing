# DV dynamic page generator

- templates/: HTML exported from the Duda templates. Put {{h1}}, {{seo_title}}, {{children_nav}} etc. in place of the text you want filled.
- data/*.json: offline rows (Slug, Parent Slug, Template, Publish, H1, SEO Title...).
- build.py: reads Airtable rows (AIRTABLE_TOKEN, BASE_ID, TABLES=Pages) or data/*.json, skips Publish=false, builds child pages under their parent, and writes output/<parent>/<child>/index.html.

Run: python3 build.py
Deploy: push output/ to GitHub Pages (free).

Status: generator tested with sample data. Templates still need {{placeholders}} inserted for each text block.
