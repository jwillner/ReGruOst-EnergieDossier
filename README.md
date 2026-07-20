# Greenpeace Energiedossier

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
- `Endfassung/` – druckfertiges PDF

---

## PDF neu bauen

Nach Änderungen an den Kapiteln:

```bash
pip install weasyprint markdown --break-system-packages
python3 build_pdf.py
```

Ergebnis: `Endfassung/Greenpeace_Energiedossier.pdf`

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

- [ ] Zahlen- und Quellenprüfung (Schlussdurchgang)
- [ ] Grafiken erstellen (Strommix, Monatsverlauf, PV-Zubau)
- [ ] Regionale Zahlen für den eigenen Kanton ergänzen
- [ ] Kurzfassung als A5-Flyer aus Kapitel 01 + 11

## Nächster Pflichttermin

**Voraussichtlich 28. Februar 2027** – Volksabstimmung zur Aufhebung des
AKW-Neubauverbots. Kapitel 09 und 11 vorher überarbeiten.
