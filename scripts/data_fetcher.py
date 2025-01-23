import os
import requests
from dotenv import load_dotenv

load_dotenv()

def fetch_data(endpoint):
    """
    Lädt Daten von der API und speichert sie lokal.
    """
    api_key = os.getenv('API_KEY')
    base_url = "https://21hlt372z1.execute-api.eu-central-1.amazonaws.com/prod"
    headers = {"X-API-Key": api_key}
    
    # Erster Request: Abrufen der JSON-Antwort
    response = requests.get(f"{base_url}/{endpoint}", headers=headers)
    response.raise_for_status()
    
    # Extrahieren der Download-URL
    download_url = response.json().get("downloadUrl")
    if not download_url:
        raise ValueError("Download-URL konnte nicht aus der API-Antwort extrahiert werden.")
    
    # Datei von der Download-URL herunterladen
    file_response = requests.get(download_url)
    file_response.raise_for_status()
    
    # Dynamischer Dateiname basierend auf dem Endpunkt
    filename = f"{endpoint}.xlsx"
    filepath = os.path.join("data", filename)
    
    # Sicherstellen, dass der Ordner existiert
    os.makedirs("data", exist_ok=True)
    
    # Datei speichern
    with open(filepath, "wb") as f:
        f.write(file_response.content)
    
    return filepath