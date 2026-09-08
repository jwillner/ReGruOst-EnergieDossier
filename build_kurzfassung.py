# -*- coding: utf-8 -*-
"""Baut die 2-seitige Kurzfassung aus Kurzfassung.md. Referenziert die
Endfassung (siehe VERSION/DATUM), ersetzt sie nicht."""
import re
import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

GRUPPE  = "Greenpeace Regionalgruppe Ost"
VERSION = "1.1"
DATUM   = "8. September 2026"

md = markdown.Markdown(extensions=["tables", "sane_lists", "nl2br"])

text = open("Kurzfassung.md", encoding="utf-8").read()
text = text.replace("{{VERSION}}", VERSION).replace("{{DATUM}}", DATUM)
# erste H1 entfernen, eigener Kopf wird gesetzt
title_match = re.match(r"^#\s+(.*)\n", text)
TITLE = title_match.group(1) if title_match else ""
text = re.sub(r"^#\s+.*\n", "", text, count=1)
body = md.convert(text)

html = f"""<html><head><meta charset="utf-8"></head><body>
<div class="head">
  <div class="eyebrow">{GRUPPE} &middot; Energiedossier</div>
  <h1>{TITLE}</h1>
</div>
<div class="content">{body}</div>
</body></html>"""

CSS_TEXT = """
@font-face {
  font-family: "Nunito";
  src: url("Fonts/Nunito-Variable.ttf");
  font-weight: 200 900;
}

@page {
  size: A4; margin: 14mm 15mm 13mm 15mm;
  @bottom-center { content: "Kurzfassung \\2014 Vollst\\00e4ndige Fassung mit Quellen: Endfassung, Greenpeace Regionalgruppe Ost \\2014 Seite " counter(page) "/" counter(pages);
                   font-family: "Nunito", sans-serif; font-size: 7pt; color: #8a8a8a; }
}

html { font-family: "Nunito", sans-serif; font-size: 9.3pt; line-height: 1.48; color: #1c1c1c; }
body { margin: 0; }

.head { margin-bottom: 4mm; }
.eyebrow { font-size: 8pt; letter-spacing: .16em; text-transform: uppercase;
  color: #00874a; font-weight: 700; margin-bottom: 2mm; }
.head h1 { font-size: 16.5pt; font-weight: 800; color: #10331f; margin: 0 0 3.5mm 0;
  border-bottom: 1.8pt solid #00874a; padding-bottom: 3mm; line-height: 1.2; }

.content { column-count: 2; column-gap: 9mm; column-rule: .4pt solid #dde3df; }

blockquote { margin: 0 0 3.5mm 0; padding: 2.8mm 3.6mm; background: #eef5f0;
  border-left: 2.5pt solid #00874a; font-size: 9.3pt; font-style: italic;
  break-inside: avoid; }
blockquote p { margin: 0; }

h2 { font-size: 10.6pt; font-weight: 800; color: #10331f;
  margin: 5mm 0 2mm 0; break-after: avoid; break-inside: avoid; }
p { margin: 0 0 2.4mm 0; text-align: justify; hyphens: auto; orphans: 3; widows: 3; }
strong { color: #10331f; font-weight: 700; }

ul, ol { margin: 0 0 2.6mm 0; padding-left: 4.2mm; }
li { margin-bottom: 1.3mm; }
li strong { color: #10331f; }

table { border-collapse: collapse; width: 100%; margin: 2.2mm 0 4mm 0;
  font-size: 8.3pt; break-inside: avoid; }
tr { break-inside: avoid; }
th { background: #10331f; color: #fff; text-align: left; padding: 1.4mm 2mm; font-weight: 700; }
td { padding: 1.4mm 2mm; border-bottom: .3pt solid #dfe4e0; vertical-align: top; }
tbody tr:nth-child(even) td { background: #f5f8f6; }

hr { display: none; }
em { color: #4a4a4a; }
"""

FONT_CONFIG = FontConfiguration()
STYLESHEET = CSS(string=CSS_TEXT, base_url=".", font_config=FONT_CONFIG)

out_path = "Endfassung/Greenpeace_Regionalgruppe_Ost_Energiedossier_Kurzfassung.pdf"
HTML(string=html, base_url=".").write_pdf(out_path, stylesheets=[STYLESHEET], font_config=FONT_CONFIG)
print(f"Kurzfassung erstellt: {out_path}")
