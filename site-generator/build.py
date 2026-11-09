"""
Dynamic page generator (static HTML, GitHub Pages friendly).

- Rows come from Airtable (set AIRTABLE_TOKEN and BASE_ID env vars) or from data/*.json for offline builds.
- Each row with Publish = true becomes one page.
- A row with a Parent Slug becomes a child page; the parent page gets a list of its children.
- Placeholders in templates: {{field}} (e.g. {{h1}}, {{seo_title}}, {{children_nav}}).
"""
import json, os, re, sys, pathlib, html, urllib.request, urllib.parse

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "output"

def load_rows():
    token, base = os.environ.get("AIRTABLE_TOKEN"), os.environ.get("BASE_ID")
    tables = [p.stem for p in (ROOT / "data").glob("*.json")]
    if token and base:
        rows = []
        for table in os.environ.get("TABLES", "Pages").split(","):
            url = f"https://api.airtable.com/v0/{base}/{urllib.parse.quote(table)}"
            req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
            data = json.load(urllib.request.urlopen(req))
            rows += [r["fields"] for r in data.get("records", [])]
        return rows
    rows = []
    for f in sorted((ROOT / "data").glob("*.json")):
        rows += json.loads(f.read_text(encoding="utf8"))
    return rows

def slug_path(row):
    parent = (row.get("Parent Slug") or "").strip("/")
    slug = row["Slug"].strip("/")
    return f"{parent}/{slug}".strip("/") if parent else slug

def render(template, values):
    def sub(m):
        return values.get(m.group(1).strip(), "")
    return re.sub(r"\{\{\s*([\w\-]+)\s*\}\}", sub, template)

def main():
    rows = [r for r in load_rows() if r.get("Publish")]
    by_parent = {}
    for r in rows:
        by_parent.setdefault((r.get("Parent Slug") or "").strip("/"), []).append(r)

    for r in rows:
        tpl_name = r.get("Template", "services") 
        tpl = (ROOT / "templates" / f"{tpl_name}.html").read_text(encoding="utf8")
        path = slug_path(r)
        children = by_parent.get(r["Slug"].strip("/"), [])
        nav = "".join(
            f'<li><a href="/{slug_path(c)}/">{html.escape(c.get("H1", c["Slug"]))}</a></li>'
            for c in children
        )
        values = {k.lower().replace(" ", "_"): str(v) for k, v in r.items()}
        values["children_nav"] = f"<ul class='child-pages'>{nav}</ul>" if children else ""
        values["seo_title"] = html.escape(r.get("SEO Title", r.get("H1", "")))
        page = render(tpl, values)
        target = OUT / path / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page, encoding="utf8")
        print("built", "/" + path + "/")

if __name__ == "__main__":
    main()
