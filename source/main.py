from pathlib import Path

import pandas as pd

# Retrouve le dossier des données à partir de l'emplacement de main.py.
dossier_script = Path(__file__).resolve().parent
racine = dossier_script.parent.parent
dossier_donnees = dossier_script.parent / "data" / "fichiers csv" / "data"

# Cherche le CSV, puis sa version compressée si besoin.
annee = 2022
fichier = dossier_donnees / f"QUOT_SIM2_{annee}.csv"

if not fichier.is_file():
    fichier = dossier_donnees / f"QUOT_SIM2_{annee}.csv.gz"

if not fichier.is_file():
    raise FileNotFoundError(f"Fichier météo de {annee} introuvable dans {dossier_donnees}")

# Garde la date, la maille et les températures utiles au projet.
# On conserve aussi T, HU et SSWI_10J pour pouvoir les tester plus tard.
colonnes = [
    "DATE", "LAMBX", "LAMBY",
    "TINF_H", "TSUP_H", "T", "HU", "SSWI_10J",
]

apercu = pd.read_csv(fichier, sep=";", usecols=colonnes, nrows=1000)
apercu = apercu[colonnes]

# Affiche les cinq premières lignes sans les numéros de ligne de Pandas.
print(apercu.head().to_string(index=False))

# Enregistre l'aperçu Excel dans le même dossier que main.py.
sortie = dossier_script / f"apercu_{annee}.xlsx"
apercu.to_excel(sortie, index=False)
print(f"\nFichier Excel créé dans {sortie}")