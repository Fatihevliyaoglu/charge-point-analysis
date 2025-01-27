# Analyse von Ladevorgängen an E-Ladestationen

## Projektbeschreibung
Dieses Projekt analysiert Ladevorgänge an Elektro-Ladestationen basierend auf zwei Datensätzen:
- Ladestationsdaten (cs.xlsx)
- Ladevorgangsdaten (cdrs.xlsx)

## Funktionen
- Sicherer API-Datenabruf
- Analyse der Ladevorgänge pro Station
- Berechnung von:
 - Anzahl Ladevorgänge pro Jahr
 - Geladene Energiemenge (kWh) pro Jahr
 - Gesamte Ladedauer in Stunden pro Jahr

## Projektstruktur
```
chargepoint-analysis/
├── data/                # Heruntergeladene Datensätze
├── notebooks/          # Jupyter Notebooks zur Analyse
├── scripts/            # Python-Skripte
├── results/            # Analyseergebnisse
├── .gitignore         # Git-Ignore Konfiguration
├── requirements.txt    # Projektabhängigkeiten
└── .env.example       # Beispiel für Umgebungsvariablen
```

## Installation
1. Repository klonen:
git clone https://github.com/Fatihevliyaoglu/charge-point-analysis.git

2. Virtuelle Umgebung erstellen und aktivieren:
python -m venv venv
source venv/bin/activate  # Unix/Mac
.\venv\Scripts\activate  # Windows

3. Abhängigkeiten installieren:
pip install -r requirements.txt

4. Umgebungsvariablen konfigurieren:
.env Datei erstellen und API Key hinzufügen (API_KEY=<API KEY hier einfügen>)
API-Key eintragen

## Verwendung

1. Daten abrufen:
```
from scripts.data_fetcher import fetch_data
```
2. Analyse ausführen:
Jupyter Notebook in notebooks/ öffnen
Analyse-Code ausführen