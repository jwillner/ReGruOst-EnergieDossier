# -*- coding: utf-8 -*-
"""Baut ein PDF im persoenlichen JoWi-Dokumentformat (einspaltig) aus einer
Markdown-Datei mit Frontmatter. Vorlage/Referenzlayout: Templates/JoWi-Formatbeispiel-*.

Aufruf: python3 build_jowi_dokument.py <pfad/zur/datei.md>
Ausgabe: PDF mit gleichem Basisnamen, im gleichen Ordner wie die Quelldatei.
"""
import os
import re
import sys

import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

MONATE = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli",
          "August", "September", "Oktober", "November", "Dezember"]


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError("Keine Frontmatter (--- ... ---) am Dateianfang gefunden.")
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, m.group(2)


def datum_ausgeschrieben(ttmmjjjj):
    tag, monat, jahr = ttmmjjjj.split(".")
    return f"{int(tag)}. {MONATE[int(monat) - 1]} {jahr}"


def nummeriere_ueberschriften(text):
    zaehler = [0, 0, 0]

    def ersetze(m):
        level = len(m.group(1))
        if level > 3:
            return m.group(0)
        zaehler[level - 1] += 1
        for i in range(level, 3):
            zaehler[i] = 0
        nummer = ".".join(str(z) for z in zaehler[:level])
        if level == 1:
            nummer += "."
        return f"{m.group(1)} {nummer} {m.group(2)}"

    return re.sub(r"^(#{1,3})\s+(.*)$", ersetze, text, flags=re.M)


def main():
    if len(sys.argv) != 2:
        sys.exit("Aufruf: python3 build_jowi_dokument.py <pfad/zur/datei.md>")
    md_path = sys.argv[1]
    meta, body = parse_frontmatter(open(md_path, encoding="utf-8").read())

    organisation = meta["organisation"]
    titel = meta["titel"]
    kategorie = meta.get("kategorie", "Notiz")
    autor = meta.get("autor", "")
    version = meta["version"]
    datum = datum_ausgeschrieben(meta["datum"])

    dateiname = os.path.splitext(os.path.basename(md_path))[0]
    out_path = os.path.join(os.path.dirname(md_path), f"{dateiname}.pdf")

    body = nummeriere_ueberschriften(body)
    md = markdown.Markdown(extensions=["tables", "sane_lists", "nl2br"])
    html_body = md.convert(body)

    meta_text = f"Version{version} &middot; {datum}"
    if autor:
        meta_text = f"&copy; {autor} &middot; {meta_text}"

    html = f"""<html><head><meta charset="utf-8"></head><body>
<div class="head">
  <div class="eyebrow">{organisation} &middot; {kategorie}</div>
  <h1>{titel}</h1>
  <div class="meta">{meta_text}</div>
</div>
<div class="content">{html_body}</div>
</body></html>"""

    css_text = f"""
@font-face {{
  font-family: "Nunito";
  src: url("Fonts/Nunito-Variable.ttf");
  font-weight: 200 900;
}}

@page {{
  size: A4; margin: 20mm 20mm 18mm 20mm;
  @bottom-left {{ content: "{dateiname}"; width: 140mm; border-top: 1pt solid #00874a;
                  padding-top: 2mm; font-family: "Nunito", sans-serif; font-size: 7.5pt; color: #8a8a8a; }}
  @bottom-right {{ content: "Seite " counter(page) "/" counter(pages); width: 30mm; text-align: right;
                   border-top: 1pt solid #00874a;
                   padding-top: 2mm; font-family: "Nunito", sans-serif; font-size: 7.5pt; color: #8a8a8a; }}
}}

html {{ font-family: "Nunito", sans-serif; font-size: 10pt; line-height: 1.5; color: #1c1c1c; }}
body {{ margin: 0; }}

.head {{ margin-bottom: 6mm; }}
.eyebrow {{ font-size: 8pt; letter-spacing: .16em; text-transform: uppercase;
  color: #00874a; font-weight: 700; margin-bottom: 2mm; }}
.head h1 {{ font-size: 21pt; font-weight: 800; color: #10331f; margin: 0 0 2mm 0; line-height: 1.25; }}
.meta {{ font-size: 8.5pt; color: #6b6b6b; margin: 0 0 4mm 0;
  border-bottom: 1.6pt solid #00874a; padding-bottom: 3.5mm; }}

h1 {{ font-size: 13.5pt; font-weight: 800; color: #10331f; margin: 7mm 0 3mm 0; page-break-after: avoid; }}
h2 {{ font-size: 11.5pt; font-weight: 700; color: #10331f; margin: 5mm 0 2.5mm 0; page-break-after: avoid; }}
h3 {{ font-size: 10.5pt; font-weight: 700; color: #2c4a38; margin: 4mm 0 2mm 0; page-break-after: avoid; }}
p {{ margin: 0 0 2.8mm 0; text-align: justify; hyphens: auto; orphans: 3; widows: 3; }}
strong {{ color: #10331f; font-weight: 700; }}

ul, ol {{ margin: 0 0 2.8mm 0; padding-left: 5mm; }}
li {{ margin-bottom: 1.2mm; }}

table {{ border-collapse: collapse; width: 100%; margin: 2.5mm 0 5mm 0;
  font-size: 8.8pt; page-break-inside: avoid; }}
tr {{ page-break-inside: avoid; }}
th {{ background: #10331f; color: #fff; text-align: left; padding: 1.6mm 2.2mm; font-weight: 700; }}
td {{ padding: 1.6mm 2.2mm; border-bottom: .3pt solid #dfe4e0; vertical-align: top; word-break: break-all; }}
tbody tr:nth-child(even) td {{ background: #f5f8f6; }}

blockquote {{ margin: 3.5mm 0; padding: 3mm 4.2mm; background: #eef5f0;
  border-left: 2.5pt solid #00874a; font-size: 9.5pt; page-break-inside: avoid; }}
blockquote p {{ margin: 0; text-align: left; }}

hr {{ border: none; border-top: .5pt solid #dde3df; margin: 6mm 0; }}
a {{ color: #1c1c1c; text-decoration: none; word-break: break-all; }}
"""

    font_config = FontConfiguration()
    stylesheet = CSS(string=css_text, base_url=".", font_config=font_config)
    HTML(string=html, base_url=".").write_pdf(out_path, stylesheets=[stylesheet], font_config=font_config)
    print(f"Dokument erstellt: {out_path}")


if __name__ == "__main__":
    main()
