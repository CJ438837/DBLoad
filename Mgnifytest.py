# =========================================================
#1️⃣2️⃣ MGnify
# =========================================================
import requests

MGNIFY_BASE_URL = "https://www.ebi.ac.uk/metagenomics/api/v1/"

def fetch_mgnify_data(resource: str):
    
    # Construire l'URL finale
    url = f"{MGNIFY_BASE_URL}{resource}"

    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(f"MGnify query failed for resource '{resource}'")

    return response.json()


# Fonction test
if __name__ == "__main__":
    test_resources = [
        "studies",
        "samples",
        "runs",
        "invalid_resource"
    ]

    for res in test_resources:
        try:
            data = fetch_mgnify_data(res)
            # Pour l'affichage, on prend juste la clé "data" si elle existe
            content = data.get("data", "Pas de données")
            print(f"✅ {res} — données récupérées: {list(content.keys()) if isinstance(content, dict) else content}")
        except ValueError as e:
            print(f"❌ {e}")
        except requests.RequestException as e:
            print(f"❌ Erreur réseau pour {res}: {e}")
