# Agent-Alertes

Projet transverse ING4 à l’ESIEE-IT, réalisé par Asma Icil, Ilies Tabyaoui et Othman Latyaoui.

L’objectif est d’estimer le risque de canicule à J+3 pour une zone donnée. Le projet prévoit une interface pour consulter les prévisions et afficher des messages d’alerte simplifiés et traduits.

## État du projet

Le script `source/main.py` lit les 1 000 premières lignes du fichier météo de 2022. Il affiche les cinq premières dans le terminal et exporte les colonnes sélectionnées dans `source/apercu_2022.xlsx`.

Les prochaines étapes sont de préparer les données d’une maille météo, de construire la cible `canicule` à partir d’une règle documentée, puis de comparer trois modèles de classification (régression logistique, Random Forest et XGBoost).

## Installation

Depuis la racine du dépôt `agent-alertes`, dans le terminal PowerShell de VS Code, créez un environnement virtuel et installez les dépendances.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Si votre environnement virtuel est déjà activé, utilisez `python -m pip install -r requirements.txt`.

## Données

Nous utilisons les données SIM quotidiennes de Météo-France. Les fichiers bruts sont conservés localement et le dossier qui les contient est ignoré par Git.

Après avoir cloné le dépôt, créez le dossier `data/fichiers csv/data/` **à l’intérieur de `agent-alertes`** et placez-y `QUOT_SIM2_2022.csv.gz`. Le script accepte également la version décompressée `QUOT_SIM2_2022.csv`.

| Colonnes | Description |
|---|---|
| `DATE` | Date de la mesure |
| `LAMBX`, `LAMBY` | Coordonnées de la maille météo |
| `TINF_H`, `TSUP_H` | Températures minimale et maximale |
| `T` | Température moyenne quotidienne |
| `HU` | Humidité relative moyenne |
| `SSWI_10J` | Indice de sécheresse du sol sur dix jours |

[Source des données SIM quotidiennes sur data.gouv.fr](https://www.data.gouv.fr/datasets/donnees-changement-climatique-sim-quotidienne)

## Lancer le script

Depuis la racine du dépôt, avec l’environnement virtuel activé :

```powershell
python .\source\main.py
```

Si vous avez créé `.venv` sans l’activer, utilisez `.\.venv\Scripts\python.exe .\source\main.py`.

Pour ouvrir l’aperçu dans Excel :

```powershell
Invoke-Item .\source\apercu_2022.xlsx
```

Fermez le classeur avant de relancer le script pour que Python puisse le remplacer.