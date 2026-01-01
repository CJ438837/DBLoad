import os
import GEOparse

BASE_DIR = outdir

def fetch_geo_series(geo_id: str, output_dir=BASE_DIR):
   
    os.makedirs(output_dir, exist_ok=True)

    try:
        gse = GEOparse.get_GEO(geo=geo_id, destdir=output_dir, silent=False)
        print(f"✅ GEO Series {geo_id} téléchargé dans {output_dir}")
        return gse
    except Exception as e:
        print(f"❌ Erreur pour {geo_id}: {e}")
        return None


if __name__ == "__main__":
    # Exemple d’un GSE connu
    test_geo_ids = ["GSE10072", "GSE62944", "INVALID_GSE"]

    for geo_id in test_geo_ids:
        gse_obj = fetch_geo_series(geo_id)
        if gse_obj:
            print(f"Nombre de samples dans {geo_id}: {len(gse_obj.gsms)}")
            # Exemple d’accès à un sample
            for gsm_id, gsm in list(gse_obj.gsms.items())[:2]:  # afficher 2 samples seulement
                print(f"{gsm_id}: {gsm.metadata['title']}")
