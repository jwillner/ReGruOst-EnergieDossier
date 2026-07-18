# 10 – Modellrechnung: Eine Gemeinde mit 1000 Einwohnerinnen und Einwohnern

**Zweck:** Nationale Terawattstunden sind abstrakt. Eine Gemeinde, die man sich vorstellen kann, ist es nicht. Diese Rechnung zeigt, was technisch machbar ist – und wo die Grenzen liegen.

> Die vollständige Rechnung liegt als Skript in `Daten/modell_gemeinde.py`, die Ergebnisse als `Daten/modell_gemeinde.csv`. Alle Annahmen sind einzeln änderbar; wer andere Werte für plausibler hält, kann sie einsetzen und nachrechnen.

---

## 1. Die Gemeinde

| Merkmal | Wert |
|---|---|
| Einwohnerinnen und Einwohner | 1'000 |
| Haushalte | ~450 |
| Wohn- und Gewerbegebäude | ~320 |
| Charakter | ländlich bis vorstädtisch, etwas Landwirtschaft, kleines Gewerbe |

---

## 2. Der Strombedarf im Zielzustand

Nicht der heutige Bedarf – der Bedarf **nachdem** Öl, Gas und Benzin ersetzt sind.

| Position | MWh/Jahr | Annahme |
|---|---:|---|
| Klassischer Strombedarf | 6'450 | 6'450 kWh pro Kopf (CH-Durchschnitt 2025) |
| Wärmepumpen | 1'650 | nach Sanierung, JAZ 3,5 |
| Elektromobilität | 1'170 | 6'500 km/Kopf, 18 kWh/100 km |
| **Total** | **9'270** | |

**Das überraschendste Ergebnis:** Die vollständige Elektrifizierung von Heizung und Verkehr erhöht den Strombedarf nur um rund **44 Prozent** – nicht um das Doppelte oder Dreifache, wie oft vermutet.

Der Grund ist die Effizienz. Eine Wärmepumpe macht aus einer Kilowattstunde Strom 3,5 Kilowattstunden Wärme. Ein Elektroauto braucht für dieselbe Strecke rund ein Viertel der Energie eines Benziners. Der **Gesamtenergiebedarf der Gemeinde sinkt dabei deutlich** – nur verschiebt er sich vom Öltank zur Steckdose.

Das ist eines der stärksten Argumente an Infoständen, weil es der verbreiteten Intuition widerspricht.

---

## 3. Der Wärmebedarf

| Position | MWh/Jahr |
|---|---:|
| Wärmebedarf heute (Raumwärme + Warmwasser) | 11'000 |
| Nach Gebäudesanierung (−30 %) | 7'700 |
| – davon Wärmepumpen (75 %) | 5'775 |
| – davon Holz-Nahwärmeverbund (25 %) | 1'925 |

**Der Nahwärmeverbund** eignet sich für den verdichteten Dorfkern: Altbauten, denkmalgeschützte Gebäude, Mehrfamilienhäuser, wo einzelne Wärmepumpen aufwendig wären. Ein Holzschnitzelkessel mit lokalem Waldholz versorgt sie über ein Leitungsnetz.

**Die Sanierung ist der grösste Einzelposten.** 3'300 MWh eingesparter Wärmebedarf – mehr, als die Windbeteiligung an Strom liefert. Dämmung ist unspektakulär und wirkt.

---

## 4. Die Eigenproduktion

### Variante A – konservativ

| Anlage | Auslegung | MWh/Jahr |
|---|---|---:|
| Photovoltaik | 4,5 MWp (4,5 kWp pro Kopf), 950 kWh/kWp | 4'275 |
| Windenergie | 40 % Anteil an einer regionalen 4,5-MW-Anlage | 2'400 |
| Biogas | Hofdünger aus ortsansässigen Betrieben | 350 |
| **Total** | | **7'025** |

### Ergebnis Variante A

| Kennzahl | Wert |
|---|---:|
| Jahresproduktion | 7'025 MWh |
| Jahresverbrauch | 9'270 MWh |
| **Deckungsgrad übers Jahr** | **76 %** |
| Winterproduktion | 3'018 MWh |
| Winterverbrauch | 5'098 MWh |
| **Winterdeckungsgrad** | **59 %** |

### Variante B – ambitioniert

Wenn die Gemeinde das Dach- und Fassadenpotenzial weitgehend ausschöpft (7 kWp pro Kopf) und die Windanlage vollständig ihr gehört:

| Anlage | MWh/Jahr |
|---|---:|
| Photovoltaik (7 MWp) | 6'650 |
| Windenergie (ganze Anlage) | 6'000 |
| Biogas | 350 |
| **Total** | **13'000** |

| Kennzahl | Wert |
|---|---:|
| **Deckungsgrad übers Jahr** | **140 %** |
| **Winterdeckungsgrad** | **119 %** |

---

## 5. Was diese Zahlen bedeuten

**Variante A ist die realistischere.** Sie zeigt: Eine typische Gemeinde kann drei Viertel ihres Bedarfs selbst produzieren, aber nicht alles – und im Winter fehlt mehr als im Sommer.

**Variante B zeigt:** Vollständige rechnerische Selbstversorgung ist möglich, wenn eine eigene Windanlage dazukommt. Ohne Wind wird es schwierig, mit Wind wird es plötzlich einfach. Das ist der stärkste Beleg dafür, wie wichtig die Windkraft für die Schweiz ist.

**Und die wichtigste Einordnung:** *Autarkie ist nicht das Ziel.* Eine Gemeinde, die 76 Prozent selbst produziert und den Rest aus dem Netz bezieht, ist kein Scheitern – sie ist ein Erfolg. Der Austausch mit dem Netz ist billiger und ressourcenschonender als der Versuch, jede Stunde des Jahres autark zu decken. Wer Autarkie zum Massstab macht, setzt sich einen Standard, den auch kein Kernkraftwerk erfüllt.

---

## 6. Speicher – und ihre ehrlichen Grenzen

| Speicher | Kapazität |
|---|---:|
| Stationäre Batterien (5 kWh pro Kopf) | 5 MWh |
| E-Auto-Batterien bidirektional (300 Fahrzeuge, 60 kWh, 30 % nutzbar) | 5,4 MWh |
| **Total** | **~10 MWh** |

Das entspricht rund **0,4 Tagen** Winterverbrauch.

**Was Batterien leisten:** Solarstrom vom Mittag in den Abend verschieben, Lastspitzen brechen, das Verteilnetz entlasten, Netzdienstleistungen erbringen.

**Was sie nicht leisten:** Sommerstrom in den Winter verschieben. Dafür wären mehrere Tausend MWh nötig – technisch und wirtschaftlich absurd.

Die saisonale Verschiebung übernehmen in der Schweiz die Speicherseen und der Handel. Diese Unterscheidung sollte man im Gespräch sauber machen; sie ist der häufigste Denkfehler in beide Richtungen.

---

## 7. Investitionsrahmen

Grobe Grössenordnung für Variante A, ohne Anspruch auf Genauigkeit:

| Massnahme | Grössenordnung |
|---|---|
| PV-Anlagen 4,5 MWp | 5–7 Mio. CHF |
| Windbeteiligung (40 % einer Anlage) | 3–4 Mio. CHF |
| Nahwärmeverbund inkl. Netz | 4–6 Mio. CHF |
| Wärmepumpen (Einzelanlagen) | 8–12 Mio. CHF |
| Gebäudesanierungen | 20–40 Mio. CHF |
| Batteriespeicher | 1–2 Mio. CHF |

Diese Summen wirken hoch. Zwei Einordnungen dazu:

1. Sie verteilen sich auf **20 bis 30 Jahre** und fallen ohnehin an – Heizungen und Fenster müssen irgendwann ersetzt werden. Die Frage ist nicht, ob investiert wird, sondern in was.
2. Ihnen stehen **eingesparte Energiekosten** gegenüber. Eine Gemeinde mit 1'000 Einwohnern gibt heute grob eine Million Franken pro Jahr für importiertes Öl, Gas und Benzin aus. Dieses Geld verlässt die Region vollständig. Investitionen in Anlagen bleiben zu einem erheblichen Teil in der Region – als Handwerkerlöhne, Pachtzinse und Steuersubstrat.

---

## 8. Realistischer Umsetzungspfad

**Phase 1 – Jahr 1 bis 3: Grundlagen**

- Energieplanung der Gemeinde erstellen lassen
- Dachkataster auswerten, Eigentümer aktiv ansprechen
- PV auf allen kommunalen Gebäuden – Vorbildfunktion und lernende Verwaltung
- Energiegenossenschaft gründen; ermöglicht Beteiligung auch für Mietende

**Phase 2 – Jahr 3 bis 8: Aufbau**

- Nahwärmeverbund im Dorfkern planen und bauen
- Förderprogramm für Heizungsersatz und Sanierungen
- Windprojekt in der Region prüfen und Beteiligung sichern (langer Vorlauf – früh beginnen)
- Ladeinfrastruktur, E-Carsharing

**Phase 3 – Jahr 8 bis 20: Vollendung**

- Sanierungsrate hochhalten – der zäheste, aber wirksamste Teil
- Quartierspeicher und Lastmanagement
- Bidirektionales Laden, sobald marktreif

---

## 9. Was jede Gemeinde sofort tun kann

Ohne grosses Budget, ohne Volksabstimmung:

1. **PV auf allen eigenen Gebäuden** – Schulhaus, Werkhof, Turnhalle, Kläranlage
2. **Energieplanung** als Grundlage für alles Weitere
3. **Baubewilligungen für PV zügig behandeln** – kostet nichts, wirkt sofort
4. **Beratungsangebot für Hauseigentümer** – die grösste Hürde ist Unsicherheit, nicht Geld
5. **Energiegenossenschaft** – ermöglicht Beteiligung ohne eigenes Dach
6. **Kommunale Fahrzeugflotte elektrifizieren**
7. **Beitritt zum Label «Energiestadt»** – strukturiert den Prozess
8. **Wärmeplanung** – wo lohnt sich ein Verbund, wo einzelne Wärmepumpen?

---

## 10. Für das Gespräch am Infostand

**«Das kann doch nie funktionieren.»**
→ «Wir haben es durchgerechnet. Eine Gemeinde mit 1'000 Einwohnern kann mit Solaranlagen auf den Dächern, einer Beteiligung an einem Windrad und einem Holz-Nahwärmeverbund rund drei Viertel ihres Strombedarfs selbst decken. Mit einem eigenen Windrad sogar mehr als hundert Prozent.»

**«Wenn alle elektrisch heizen und fahren, bricht das Netz zusammen.»**
→ «Der Strombedarf steigt tatsächlich – aber nur um rund 44 Prozent, nicht um das Doppelte. Weil eine Wärmepumpe aus einer Kilowattstunde Strom dreieinhalb Kilowattstunden Wärme macht und ein Elektroauto viermal effizienter ist als ein Benziner. Der Gesamtenergiebedarf sinkt sogar.»

**«Und das soll bezahlbar sein?»**
→ «Unsere Gemeinde gibt heute rund eine Million Franken pro Jahr für Öl, Gas und Benzin aus – Geld, das komplett ins Ausland geht. Dieselben Investitionen in Dächer und Heizungen bleiben grösstenteils bei lokalen Handwerkern.»

---

**Quellen der Annahmen:** BFE Elektrizitätsbilanz 2025 (Pro-Kopf-Verbrauch) · BFS Gebäude- und Wohnungsstatistik · FWS (Wärmepumpen-Kennzahlen) · Swissolar (spezifische PV-Erträge) · Suisse Eole (Anlagenerträge und Winteranteil). Rechenweg vollständig offengelegt in `Daten/modell_gemeinde.py`.
