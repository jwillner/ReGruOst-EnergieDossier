# Greenpeace Regionalgruppe Ost – Energiedossier

**Warum wir auf erneuerbare Energien setzen** – Fakten, Zahlen und Argumente zur Schweizer Energiezukunft.

Argumentationshilfe für Infostände und Gespräche der Regionalgruppe.
Stand: Juli 2026.

---

## Inhalt

| Datei | Kapitel |
|---|---|
| `00_Projektplan.md` | Zweck, Redaktionsregeln, Aktualisierungszyklus |
| `01_Einleitung.md` | Acht Argumente für erneuerbare Energien |
| `02_Ausgangslage_Schweiz.md` | Zahlen zum Schweizer Strom- und Energiesystem |
| `03_Solarenergie.md` | Photovoltaik: Stand, Potenzial, Kosten |
| `04_Windenergie.md` | Windkraft, Winterstrom, Akzeptanz |
| `05_Wasserkraft.md` | Rückgrat des Systems, Ausbaugrenzen |
| `06_Biomasse.md` | Holz, Biogas, KVA |
| `07_Geothermie.md` | Wärme ja, Strom noch offen |
| `08_Speicher_und_Netze.md` | Winterlücke, Dunkelflaute, Batterien, Netze |
| `09_Kernenergie.md` | Sachliche Pro-/Contra-Auslegeordnung |
| `10_Gemeinde_1000_Einwohner.md` | Durchgerechnetes Gemeindemodell |
| `11_Haeufige_Einwaende.md` | Behauptung – Faktenlage – Kurzantwort |
| `12_Quellen.md` | Alle Quellen gebündelt |

### Ordner

- `Daten/` – Rechenskript und Ergebnisse der Gemeinde-Modellrechnung
- `Tabellen/` – Kennzahlen-Kurzreferenz für den Infostand
- `Grafiken/` – Diagramme (noch zu erstellen)
- `Endfassung/` – druckfertiges PDF (Gesamtdokument und `Kapitel/` einzeln)

---

## PDF neu bauen

Einmalig eine virtuelle Umgebung anlegen und die Abhängigkeiten installieren:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install weasyprint markdown
```

Nach Änderungen an den Kapiteln:

```bash
source .venv/bin/activate
python3 build_pdf.py
```

Ergebnis: `Endfassung/Greenpeace_Regionalgruppe_Ost_Energiedossier.pdf` (Gesamtdokument) sowie je eine
Einzel-PDF pro Kapitel in `Endfassung/Kapitel/` – praktisch zum gezielten
Weitergeben eines einzelnen Themas.

**Apple-Silicon-Mac mit Intel-Homebrew (`/usr/local`, per Rosetta):** Falls beim
Build `OSError: cannot load library 'libgobject-2.0-0'` erscheint, liegt eine
Architektur-Inkompatibilität zwischen nativer arm64-venv und x86_64-Homebrew-
Bibliotheken vor. Dann die venv unter Rosetta anlegen und immer darüber
aufrufen:

```bash
arch -x86_64 /usr/bin/python3 -m venv .venv
arch -x86_64 .venv/bin/python3 -m pip install weasyprint markdown
arch -x86_64 .venv/bin/python3 build_pdf.py
```

## Modellrechnung neu rechnen

```bash
python3 Daten/modell_gemeinde.py
```

Alle Annahmen stehen als benannte Variablen zuoberst im Skript und lassen sich
einzeln anpassen. Ausgabe: Konsole plus `Daten/modell_gemeinde.csv`.

---

## Redaktionsregeln

1. Jede Zahl bekommt eine Quelle.
2. Jahreszahl immer dazu.
3. Provisorische Werte kennzeichnen.
4. Gegenargumente ernst nehmen – erst die Behauptung, dann die Faktenlage.
5. Greenpeace-Position und amtliche Statistik sauber trennen.
6. Zielkonflikte benennen statt ausblenden.

Ausführlich in `00_Projektplan.md`.

---

## Offene Punkte

- [x] Zahlen- und Quellenprüfung Kapitel 02 (Schlussdurchgang, inkl. PDF-Rendering
      Zeile für Zeile geprüft: Abschnitte 9+10, fossile Importe vs.
      EE-Investitionen CH/DE, 10-Jahres-Zeitreihe 2015–2024)
- [ ] Zahlen- und Quellenprüfung übrige Kapitel (bisher nur überflogen, nicht im
      gleichen Detailgrad wie Kapitel 02)
- [ ] Grafiken erstellen (Strommix, Monatsverlauf, PV-Zubau)
- [ ] Regionale Zahlen für den eigenen Kanton ergänzen
- [ ] Kurzfassung als A5-Flyer aus Kapitel 01 + 11

## Nächster Pflichttermin

**Voraussichtlich 28. Februar 2027** – Volksabstimmung zur Aufhebung des
AKW-Neubauverbots. Kapitel 09 und 11 vorher überarbeiten.
