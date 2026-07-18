# -*- coding: utf-8 -*-
"""Modellrechnung Gemeinde mit 1000 Einwohnerinnen und Einwohnern.
Alle Werte in MWh/Jahr, sofern nicht anders vermerkt.
Annahmen sind im Kapitel 10 dokumentiert und einzeln nachvollziehbar.
"""
import csv

EW = 1000
HAUSHALTE = 450          # 2,2 Personen pro Haushalt (BFS-Durchschnitt, gerundet)
GEBAEUDE = 320           # Wohn- und Gewerbegebaeude

# ---------------------------------------------------------------- VERBRAUCH
# 1) Klassischer Strombedarf
#    CH-Endverbrauch 58,1 TWh (2025) / 9,0 Mio EW = ca. 6'450 kWh pro Kopf
strom_heute = 6.45 * EW                    # MWh

# 2) Waerme: Raumwaerme + Warmwasser
#    CH-Gebaeudebereich rund 11'000 kWh Endenergie pro Kopf
waerme_heute = 11.0 * EW                   # MWh Endenergie, heute ueberwiegend fossil
sanierungsgewinn = 0.30                    # 30 % weniger Bedarf durch Gebaeudehuelle
waerme_saniert = waerme_heute * (1 - sanierungsgewinn)
JAZ_WP = 3.5                               # Jahresarbeitszahl Waermepumpe
anteil_nahwaerme = 0.25                    # 25 % der Waerme ueber Holz-Nahwaermeverbund
waerme_wp = waerme_saniert * (1 - anteil_nahwaerme)
waerme_holz = waerme_saniert * anteil_nahwaerme
strom_waermepumpen = waerme_wp / JAZ_WP

# 3) Verkehr
#    ca. 6'500 Fahrzeugkilometer pro Kopf und Jahr, E-Auto 18 kWh/100 km
km_pro_kopf = 6500
verbrauch_ev = 0.18                        # kWh/km
strom_mobilitaet = km_pro_kopf * verbrauch_ev * EW / 1000   # MWh

verbrauch_total = strom_heute + strom_waermepumpen + strom_mobilitaet

# ---------------------------------------------------------------- PRODUKTION
# 4) Photovoltaik auf Daechern und Fassaden
#    Realistisch erschliessbar: 4,5 kWp pro Kopf; Ertrag 950 kWh/kWp (Mittelland)
pv_kwp = 4.5 * EW                          # 4'500 kWp = 4,5 MWp
pv_ertrag_spez = 950                       # kWh/kWp/a
pv_produktion = pv_kwp * pv_ertrag_spez / 1000              # MWh
pv_winteranteil = 0.30

# 5) Windenergie: Beteiligung an einer regionalen Anlage
#    Moderne Anlage 4,5 MW, ca. 6'000 MWh/a; Gemeindeanteil 40 %
wind_anlage = 6000                         # MWh/a
wind_anteil = 0.40
wind_produktion = wind_anlage * wind_anteil
wind_winteranteil = 0.65

# 6) Biogas aus Hofduenger (landwirtschaftlich gepraegte Gemeinde)
biogas_produktion = 350                    # MWh Strom/a
biogas_winteranteil = 0.50

produktion_total = pv_produktion + wind_produktion + biogas_produktion

# ---------------------------------------------------------------- SPEICHER
# 7) Batterien: 5 kWh pro Kopf (Heimspeicher + Quartierspeicher)
batterie_kapazitaet = 5.0 * EW / 1000      # MWh Kapazitaet
# 8) Bidirektionale E-Autos: 300 Fahrzeuge, 60 kWh, 30 % nutzbar
ev_anzahl = 300
ev_batterie = 60                           # kWh
ev_nutzbar = 0.30
ev_speicher = ev_anzahl * ev_batterie * ev_nutzbar / 1000   # MWh

# ---------------------------------------------------------------- SAISONAL
winterproduktion = (pv_produktion * pv_winteranteil
                    + wind_produktion * wind_winteranteil
                    + biogas_produktion * biogas_winteranteil)
winterverbrauch = verbrauch_total * 0.55   # 55 % des Verbrauchs im Winterhalbjahr
sommerproduktion = produktion_total - winterproduktion
sommerverbrauch = verbrauch_total * 0.45

# ---------------------------------------------------------------- AUSGABE
def p(label, wert, einheit="MWh/a"):
    print(f"{label:<52}{wert:>10,.0f} {einheit}".replace(",", "'"))

print("=" * 74)
print("MODELLGEMEINDE - 1000 EINWOHNERINNEN UND EINWOHNER")
print("=" * 74)
print("\nSTROMBEDARF IM ZIELZUSTAND")
p("Klassischer Strombedarf (Haushalte, Gewerbe)", strom_heute)
p("Waermepumpen (nach Sanierung)", strom_waermepumpen)
p("Elektromobilitaet", strom_mobilitaet)
p("TOTAL Strombedarf", verbrauch_total)

print("\nWAERMEBEDARF")
p("Waermebedarf heute", waerme_heute)
p("Waermebedarf nach Sanierung (-30 %)", waerme_saniert)
p("  davon Waermepumpen", waerme_wp)
p("  davon Holz-Nahwaermeverbund", waerme_holz)

print("\nEIGENPRODUKTION STROM")
p(f"Photovoltaik ({pv_kwp/1000:.1f} MWp)", pv_produktion)
p("Windenergie (40 % einer 4,5-MW-Anlage)", wind_produktion)
p("Biogas aus Hofduenger", biogas_produktion)
p("TOTAL Eigenproduktion", produktion_total)

print("\nBILANZ")
p("Produktion minus Verbrauch", produktion_total - verbrauch_total)
print(f"{'Deckungsgrad uebers Jahr':<52}{produktion_total/verbrauch_total*100:>10.0f} %")

print("\nSAISONALE BILANZ")
p("Winterhalbjahr: Produktion", winterproduktion)
p("Winterhalbjahr: Verbrauch", winterverbrauch)
p("Winterhalbjahr: Saldo", winterproduktion - winterverbrauch)
print(f"{'Winterdeckungsgrad':<52}{winterproduktion/winterverbrauch*100:>10.0f} %")
p("Sommerhalbjahr: Produktion", sommerproduktion)
p("Sommerhalbjahr: Verbrauch", sommerverbrauch)
p("Sommerhalbjahr: Saldo (Export)", sommerproduktion - sommerverbrauch)

print("\nSPEICHER")
p("Stationaere Batterien", batterie_kapazitaet, "MWh")
p("Nutzbare E-Auto-Batterien (bidirektional)", ev_speicher, "MWh")
p("Speicher total", batterie_kapazitaet + ev_speicher, "MWh")
print(f"{'entspricht Tagesverbrauch im Winter von':<52}"
      f"{(batterie_kapazitaet+ev_speicher)/(winterverbrauch/182):>10.1f} Tagen")
print("=" * 74)

# CSV schreiben
rows = [
    ["Kategorie", "Position", "Wert", "Einheit"],
    ["Verbrauch", "Klassischer Strombedarf", round(strom_heute), "MWh/a"],
    ["Verbrauch", "Waermepumpen", round(strom_waermepumpen), "MWh/a"],
    ["Verbrauch", "Elektromobilitaet", round(strom_mobilitaet), "MWh/a"],
    ["Verbrauch", "Total Strombedarf", round(verbrauch_total), "MWh/a"],
    ["Waerme", "Bedarf heute", round(waerme_heute), "MWh/a"],
    ["Waerme", "Bedarf nach Sanierung", round(waerme_saniert), "MWh/a"],
    ["Waerme", "davon Waermepumpen", round(waerme_wp), "MWh/a"],
    ["Waerme", "davon Holz-Nahwaerme", round(waerme_holz), "MWh/a"],
    ["Produktion", "Photovoltaik", round(pv_produktion), "MWh/a"],
    ["Produktion", "Windenergie (Anteil)", round(wind_produktion), "MWh/a"],
    ["Produktion", "Biogas", round(biogas_produktion), "MWh/a"],
    ["Produktion", "Total", round(produktion_total), "MWh/a"],
    ["Bilanz", "Saldo Jahr", round(produktion_total - verbrauch_total), "MWh/a"],
    ["Bilanz", "Deckungsgrad Jahr", round(produktion_total/verbrauch_total*100), "%"],
    ["Bilanz", "Winterproduktion", round(winterproduktion), "MWh/a"],
    ["Bilanz", "Winterverbrauch", round(winterverbrauch), "MWh/a"],
    ["Bilanz", "Winterdeckungsgrad", round(winterproduktion/winterverbrauch*100), "%"],
    ["Speicher", "Stationaere Batterien", round(batterie_kapazitaet, 1), "MWh"],
    ["Speicher", "E-Auto bidirektional", round(ev_speicher, 1), "MWh"],
]
with open("Daten/modell_gemeinde.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter=";").writerows(rows)
