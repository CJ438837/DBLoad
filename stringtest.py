import requests

# ------------------------------
# Fonction STRING PPI
# ------------------------------
def fetch_string_interactions(protein_id: str, species=9606):
    """
    Récupère les interactions protéine-protéine depuis STRING
    """
    url = "https://string-db.org/api/json/network"
    params = {
        "identifiers": protein_id,
        "species": species
    }
    response = requests.get(url, params=params)
    response.raise_for_status()  # lève une exception si erreur HTTP
    return response.json()


# ------------------------------
# Script test
# ------------------------------
if __name__ == "__main__":
    test_proteins = [
        "P53_HUMAN",  # TP53
        "BRCA1_HUMAN",
        "INVALID_ID"  # ID invalide pour tester l'erreur
    ]

    for pid in test_proteins:
        try:
            interactions = fetch_string_interactions(pid)
            if interactions:
                print(f"✅ {len(interactions)} interactions trouvées pour {pid}")
                # Afficher un aperçu
                for inter in interactions[:5]:
                    print(f"  {inter['preferredName_A']} - {inter['preferredName_B']} | score: {inter['score']:.2f}")
            else:
                print(f"⚠️ Aucune interaction trouvée pour {pid}")
        except requests.RequestException as e:
            print(f"❌ Erreur réseau pour {pid}: {e}")
        except Exception as e:
            print(f"❌ Erreur pour {pid}: {e}")
