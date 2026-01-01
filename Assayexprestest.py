import requests

def fetch_arrayexpress_experiment(accession: str):
    """
    Récupère les métadonnées d’un experiment ArrayExpress via l’API JSON.

    Args:
        accession: ID de l’expérience (ex: E-MTAB-513)

    Returns:
        dict : JSON des métadonnées
    """
    url = f"https://www.ebi.ac.uk/biostudies/api/v1/studies/{accession}"
    
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()  # lève une exception si code != 200
    except requests.HTTPError as e:
        raise ValueError(f"ArrayExpress query failed for {accession}: {e}")
    except requests.RequestException as e:
        raise ConnectionError(f"Erreur réseau pour {accession}: {e}")
    
    data = r.json()
    return data


if __name__ == "__main__":
    test_accessions = [
        "E-MTAB-513",
        "E-GEOD-2034",
        "INVALID_ID"
    ]

    for acc in test_accessions:
        try:
            data = fetch_arrayexpress_experiment(acc)

            title = "Pas de titre"
            for attr in data.get("section", {}).get("attributes", []):
                if attr.get("name") == "Title":
                    title = attr.get("value")
                    break

            print(f"✅ {acc} — titre : {title}")

        except ValueError as e:
            print(f"❌ {e}")
        except requests.RequestException as e:
            print(f"❌ Erreur réseau pour {acc}: {e}")
