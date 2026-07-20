# -*- coding: utf-8 -*-
"""Baut die druckfertige PDF-Endfassung aus den Kapitel-Markdown-Dateien."""
import glob, os, re
import markdown
from weasyprint import HTML, CSS

FILES = sorted(glob.glob("[0-9][0-9]_*.md"))

TITEL = {
    "00": "Projektplan", "01": "Warum erneuerbare Energien?",
    "02": "Die Ausgangslage der Schweiz", "03": "Solarenergie",
    "04": "Windenergie", "05": "Wasserkraft", "06": "Biomasse",
    "07": "Geothermie", "08": "Speicher, Netze und die Winterfrage",
    "09": "Brauchen wir neue Kernkraftwerke?",
    "10": "Modellrechnung: Gemeinde mit 1000 Einwohnern",
    "11": "Häufige Einwände", "12": "Quellen",
}

md = markdown.Markdown(extensions=["tables", "fenced_code", "attr_list", "sane_lists", "nl2br"])

# ---- Titelseite + Inhaltsverzeichnis
parts = ["""
<div class="cover">
  <div class="cover-eyebrow">Greenpeace Regionalgruppe</div>
  <h1 class="cover-title">Warum wir auf<br>erneuerbare Energien setzen</h1>
  <div class="cover-sub">Fakten, Zahlen und Argumente zur Schweizer Energiezukunft</div>
  <div class="cover-rule"></div>
  <div class="cover-meta">Energiedossier &middot; Stand Juli 2026<br>
  Argumentationshilfe für Infostände und Gespräche</div>
</div>
<div class="toc-page">
  <h1>Inhalt</h1>
  <ul class="toc">
"""]
for f in FILES:
    nr = f[:2]
    parts.append(f'<li><span class="toc-nr">{nr}</span>'
                 f'<span class="toc-t">{TITEL.get(nr, f)}</span>'
                 f'<span class="toc-p"></span></li>')
parts.append("</ul></div>")

# ---- Kapitel
for f in FILES:
    nr = f[:2]
    text = open(f, encoding="utf-8").read()
    # erste H1 entfernen, wir setzen einen eigenen Kapitelkopf
    text = re.sub(r"^#\s+.*\n", "", text, count=1)
    body = md.convert(text)
    md.reset()
    parts.append(
        f'<section class="chapter"><div class="chap-head">'
        f'<div class="chap-nr">Kapitel {nr}</div>'
        f'<h1>{TITEL.get(nr, f)}</h1></div>{body}</section>'
    )

CSSTEXT = """
@page {
  size: A4; margin: 22mm 20mm 20mm 20mm;
  @bottom-center { content: counter(page); font-family: "DejaVu Sans", sans-serif;
                   font-size: 8.5pt; color: #7a7a7a; }
  @top-right { content: "Greenpeace Energiedossier"; font-family: "DejaVu Sans", sans-serif;
               font-size: 7.5pt; color: #a5a5a5; letter-spacing: .06em; }
}
@page :first { @bottom-center { content: ""; } @top-right { content: ""; } }

html { font-family: "DejaVu Serif", Georgia, serif; font-size: 10pt;
       line-height: 1.52; color: #1c1c1c; }
body { margin: 0; }

/* ---------- Titelseite ---------- */
.cover { page-break-after: always; padding-top: 55mm; }
.cover-eyebrow { font-family: "DejaVu Sans", sans-serif; font-size: 9pt;
  letter-spacing: .22em; text-transform: uppercase; color: #00874a; margin-bottom: 14mm; }
.cover-title { font-family: "DejaVu Sans", sans-serif; font-size: 27pt; line-height: 1.22;
  font-weight: 700; color: #10331f; margin: 0 0 8mm 0; border: none; padding: 0; }
.cover-sub { font-size: 12.5pt; color: #3d5a49; line-height: 1.5; max-width: 118mm; }
.cover-rule { width: 34mm; height: 3.5pt; background: #00874a; margin: 14mm 0 8mm 0; }
.cover-meta { font-family: "DejaVu Sans", sans-serif; font-size: 9pt; color: #6d6d6d; line-height: 1.7; }

/* ---------- Inhaltsverzeichnis ---------- */
.toc-page { page-break-after: always; }
ul.toc { list-style: none; padding: 0; margin-top: 8mm; }
ul.toc li { font-family: "DejaVu Sans", sans-serif; font-size: 10.5pt;
  padding: 2.6mm 0; border-bottom: .4pt solid #e2e6e3; }
.toc-nr { display: inline-block; width: 13mm; color: #00874a; font-weight: 700; }
.toc-t { color: #22332a; }

/* ---------- Kapitel ---------- */
.chapter { page-break-before: always; }
.chap-head { border-bottom: 2.4pt solid #00874a; margin-bottom: 7mm; padding-bottom: 3mm; }
.chap-nr { font-family: "DejaVu Sans", sans-serif; font-size: 8.5pt; letter-spacing: .2em;
  text-transform: uppercase; color: #00874a; margin-bottom: 2mm; }
.chap-head h1 { font-family: "DejaVu Sans", sans-serif; font-size: 19pt; line-height: 1.24;
  color: #10331f; margin: 0; border: none; padding: 0; }

h2 { font-family: "DejaVu Sans", sans-serif; font-size: 12.5pt; color: #10331f;
  margin: 7mm 0 2.5mm 0; page-break-after: avoid; }
h3 { font-family: "DejaVu Sans", sans-serif; font-size: 10.5pt; color: #2c4a38;
  margin: 5mm 0 1.5mm 0; page-break-after: avoid; }
p { margin: 0 0 2.6mm 0; text-align: justify; hyphens: auto; }
strong { color: #10331f; }

ul, ol { margin: 0 0 3mm 0; padding-left: 5.5mm; }
li { margin-bottom: 1.1mm; }

/* ---------- Tabellen ---------- */
table { border-collapse: collapse; width: 100%; margin: 3.5mm 0 5mm 0;
  font-family: "DejaVu Sans", sans-serif; font-size: 8.6pt; page-break-inside: avoid; }
th { background: #10331f; color: #fff; text-align: left; padding: 2mm 2.4mm;
  font-weight: 600; }
td { padding: 1.7mm 2.4mm; border-bottom: .4pt solid #dfe4e0; vertical-align: top; }
tbody tr:nth-child(even) td { background: #f5f8f6; }

/* ---------- Zitate / Hinweise ---------- */
blockquote { margin: 4mm 0; padding: 3mm 4.5mm; background: #eef5f0;
  border-left: 3pt solid #00874a; font-size: 9.6pt; }
blockquote p { margin: 0 0 1.5mm 0; text-align: left; }
blockquote p:last-child { margin-bottom: 0; }

code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.4pt;
  background: #f0f3f1; padding: .3mm 1mm; border-radius: 1.5pt; }
pre { background: #f5f8f6; border-left: 2.5pt solid #b9ccc0; padding: 3mm 4mm;
  font-size: 8pt; line-height: 1.4; page-break-inside: avoid; overflow-wrap: break-word; }
pre code { background: none; padding: 0; }

hr { border: none; border-top: .5pt solid #dde3df; margin: 6mm 0; }
a { color: #1c1c1c; text-decoration: none; word-break: break-all; }
"""

html = "<html><head><meta charset='utf-8'></head><body>" + "".join(parts) + "</body></html>"
os.makedirs("Endfassung", exist_ok=True)
HTML(string=html, base_url=".").write_pdf("Endfassung/Greenpeace_Energiedossier.pdf",
                                          stylesheets=[CSS(string=CSSTEXT)])
print("PDF erstellt.")
