# -*- coding: utf-8 -*-
"""Baut die druckfertige PDF-Endfassung aus den Kapitel-Markdown-Dateien."""
import glob, os, re
import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

# ---- Metadaten (hier anpassen bei neuer Version) ----
GRUPPE       = "Greenpeace Regionalgruppe Ost"
VERSION      = "1.0"
DATUM        = "20. Juli 2026"
VERANTWORTL  = "Greenpeace Regionalgruppe Ost / Joachim Willner"

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


def chapter_html(f):
    nr = f[:2]
    text = open(f, encoding="utf-8").read()
    # erste H1 entfernen, wir setzen einen eigenen Kapitelkopf
    text = re.sub(r"^#\s+.*\n", "", text, count=1)
    body = md.convert(text)
    md.reset()
    return (
        f'<section class="chapter"><div class="chap-head">'
        f'<div class="chap-nr">Kapitel {nr}</div>'
        f'<h1>{TITEL.get(nr, f)}</h1></div>{body}</section>'
    )


# ---- Titelseite + Inhaltsverzeichnis
parts = [f"""
<div class="cover">
  <div class="cover-eyebrow">{GRUPPE}</div>
  <h1 class="cover-title">Warum wir auf<br>erneuerbare Energien setzen</h1>
  <div class="cover-sub">Fakten, Zahlen und Argumente zur Schweizer Energiezukunft</div>
  <div class="cover-rule"></div>
  <div class="cover-meta">Energiedossier &middot; Version {VERSION} &middot; {DATUM}<br>
  Argumentationshilfe für Infostände und Gespräche</div>
  <div class="cover-resp">Verantwortlich: {VERANTWORTL}</div>
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
    parts.append(chapter_html(f))

CSSTEXT = """
@font-face {
  font-family: "Nunito";
  src: url("Fonts/Nunito-Variable.ttf");
  font-weight: 200 900;
}

@page {
  size: A4; margin: 22mm 20mm 20mm 20mm;
  @bottom-center { content: "Seite " counter(page) "/" counter(pages);
                   font-family: "Nunito", sans-serif;
                   font-size: 8.5pt; color: #7a7a7a; }
  @top-right { content: "GRUPPE_PLATZHALTER Energiedossier"; font-family: "Nunito", sans-serif;
               font-size: 7.5pt; color: #a5a5a5; letter-spacing: .06em; }
  @top-left { content: "Version VERSION_PLATZHALTER · DATUM_PLATZHALTER"; font-family: "Nunito", sans-serif;
              font-size: 7.5pt; color: #a5a5a5; letter-spacing: .06em; }
}
@page :first { @bottom-center { content: ""; } @top-right { content: ""; } @top-left { content: ""; } }

/* Kapitelinhalt (.chapter) haelt sich an genau 3 Schriftgroessen:
   --gross fuer den Kapiteltitel, --mittel fuer h2/h3 (per Gewicht/Farbe
   unterschieden), --basis fuer Fliesstext, Tabellen, Zitate, Code, Listen
   und das Kapitel-Label. Cover und Kopf-/Fusszeile liegen ausserhalb davon. */
.chapter {
  --gross: 15pt; --mittel: 11.5pt; --basis: 9.5pt;
}

html { font-family: "Nunito", sans-serif; font-size: 10pt;
       line-height: 1.52; color: #1c1c1c; }
body { margin: 0; }

/* ---------- Titelseite ---------- */
.cover { page-break-after: always; padding-top: 55mm; }
.cover-eyebrow { font-size: 9pt;
  letter-spacing: .22em; text-transform: uppercase; color: #00874a; margin-bottom: 14mm; }
.cover-title { font-size: 27pt; line-height: 1.22;
  font-weight: 800; color: #10331f; margin: 0 0 8mm 0; border: none; padding: 0; }
.cover-sub { font-size: 12.5pt; color: #3d5a49; line-height: 1.5; max-width: 118mm; }
.cover-rule { width: 34mm; height: 3.5pt; background: #00874a; margin: 14mm 0 8mm 0; }
.cover-meta { font-size: 9pt; color: #6d6d6d; line-height: 1.7; }
.cover-resp { font-size: 9pt; color: #10331f;
  margin-top: 10mm; padding-top: 3mm; border-top: .5pt solid #d5ddd8; }

/* ---------- Inhaltsverzeichnis ---------- */
.toc-page { page-break-after: always; }
ul.toc { list-style: none; padding: 0; margin-top: 8mm; }
ul.toc li { font-size: 10.5pt;
  padding: 2.6mm 0; border-bottom: .4pt solid #e2e6e3; }
.toc-nr { display: inline-block; width: 13mm; color: #00874a; font-weight: 700; }
.toc-t { color: #22332a; }

/* ---------- Kapitel ---------- */
.chapter { page-break-before: always; }
.chap-head { border-bottom: 2.4pt solid #00874a; margin-bottom: 7mm; padding-bottom: 3mm; }
.chap-nr { font-size: var(--basis); font-weight: 700; letter-spacing: .2em;
  text-transform: uppercase; color: #00874a; margin-bottom: 2mm; }
.chap-head h1 { font-size: var(--gross); font-weight: 800; line-height: 1.24;
  color: #10331f; margin: 0; border: none; padding: 0; }

h2 { font-size: var(--mittel); font-weight: 800; color: #10331f;
  margin: 7mm 0 2.5mm 0; page-break-after: avoid; }
h3 { font-size: var(--mittel); font-weight: 600; color: #2c4a38;
  margin: 5mm 0 1.5mm 0; page-break-after: avoid; }
p { font-size: var(--basis); margin: 0 0 2.6mm 0; text-align: justify; hyphens: auto; }
strong { color: #10331f; font-weight: 700; }

ul, ol { font-size: var(--basis); margin: 0 0 3mm 0; padding-left: 5.5mm; }
li { margin-bottom: 1.1mm; }

/* ---------- Tabellen ---------- */
table { border-collapse: collapse; width: 100%; margin: 3.5mm 0 5mm 0;
  font-size: var(--basis); page-break-inside: avoid; }
tr { page-break-inside: avoid; }
th { background: #10331f; color: #fff; text-align: left; padding: 2mm 2.4mm;
  font-weight: 700; }
td { padding: 1.7mm 2.4mm; border-bottom: .4pt solid #dfe4e0; vertical-align: top; }
tbody tr:nth-child(even) td { background: #f5f8f6; }

/* ---------- Zitate / Hinweise ---------- */
blockquote { margin: 4mm 0; padding: 3mm 4.5mm; background: #eef5f0;
  border-left: 3pt solid #00874a; font-size: var(--basis); }
blockquote p { font-size: inherit; margin: 0 0 1.5mm 0; text-align: left; }
blockquote p:last-child { margin-bottom: 0; }

code { font-family: "Nunito", sans-serif; font-size: var(--basis);
  background: #f0f3f1; padding: .3mm 1mm; border-radius: 1.5pt; }
pre { font-family: "Nunito", sans-serif;
  background: #f5f8f6; border-left: 2.5pt solid #b9ccc0; padding: 3mm 4mm;
  font-size: var(--basis); line-height: 1.4; page-break-inside: avoid; overflow-wrap: break-word; }
pre code { background: none; padding: 0; }

hr { border: none; border-top: .5pt solid #dde3df; margin: 6mm 0; }
a { color: #1c1c1c; text-decoration: none; word-break: break-all; }
"""

os.makedirs("Endfassung", exist_ok=True)
CSSTEXT = (CSSTEXT.replace("GRUPPE_PLATZHALTER", GRUPPE)
                  .replace("VERSION_PLATZHALTER", VERSION)
                  .replace("DATUM_PLATZHALTER", DATUM))
FONT_CONFIG = FontConfiguration()
STYLESHEET = CSS(string=CSSTEXT, base_url=".", font_config=FONT_CONFIG)


def write_pdf(body_parts, out_path):
    html = "<html><head><meta charset='utf-8'></head><body>" + "".join(body_parts) + "</body></html>"
    HTML(string=html, base_url=".").write_pdf(
        out_path, stylesheets=[STYLESHEET], font_config=FONT_CONFIG)


# ---- Gesamt-PDF
write_pdf(parts, "Endfassung/Greenpeace_Regionalgruppe_Ost_Energiedossier.pdf")
print("Gesamt-PDF erstellt.")

# ---- Einzel-PDFs je Kapitel
EINZELVERZ = "Endfassung/Kapitel"
os.makedirs(EINZELVERZ, exist_ok=True)
for f in FILES:
    out_name = os.path.splitext(f)[0] + ".pdf"
    write_pdf([chapter_html(f)], os.path.join(EINZELVERZ, out_name))
print(f"{len(FILES)} Einzel-PDFs erstellt in {EINZELVERZ}/.")
