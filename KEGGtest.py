from bioservices import KEGG

# ------------------------------
# Fonction à tester
# ------------------------------
def fetch_kegg_pathway(pathway_id: str):
    
    k = KEGG()
    return k.get(pathway_id)


# ------------------------------
# Test
# ------------------------------
if __name__ == "__main__":
    test_pathways = [
        "hsa00010",  # Glycolysis / Gluconeogenesis (humain)
        "hsa04110",  # Cell cycle (humain)
        "INVALID_ID"  # ID invalide pour tester l'erreur
    ]

    for pid in test_pathways:
        try:
            result = fetch_kegg_pathway(pid)
            if result:
                print(f"✅ KEGG pathway {pid} récupéré avec succès (longueur {len(result)} caractères)")
                print(result[:500], "...")  # Affiche seulement les 500 premiers caractères
            else:
                print(f"❌ KEGG pathway {pid} retourné vide")
        except Exception as e:
            print(f"❌ Erreur pour {pid}: {e}")
