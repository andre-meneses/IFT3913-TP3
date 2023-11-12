# TP3 - Qualité de Logiciel et Métriques

## Membres de l'équipe
- André Meneses
- Paul Godbert

## Résumé
Cette analyse statistique s'appuie sur deux scripts Python : `plot_data.py` et `stats.py`. Le premier, `plot_data.py`, est dédié à la génération de graphiques tels que les boîtes à moustaches et les nuages de points. Les informations clés pour les boîtes à moustaches sont enregistrées dans `output/statistiques_metriques.csv`. Quant à `stats.py`, il effectue des tests de normalité sur les données et calcule les coefficients de corrélation, en fonction des résultats de ces tests. Un seuil de signification de 5% est adopté. Ce script génère également les lignes de régression linéaire entre les variables "TASSERT", "TLOC" et "TASSERT", "WMC". Tous les graphiques produits sont sauvegardés dans le dossier `figures`, tandis que les fichiers CSV sont stockés dans `output`.

## Utilisation
Pour commencer, installez les packages nécessaires avec la commande suivante :
```sh
pip install -r requirements.txt
```
Ensuite, exécutez les scripts comme suit :
```sh
python3 scripts/plot_data.py
python3 scripts/stats.py
```
Il est important d'exécuter ces scripts depuis la racine du projet et non depuis le dossier 'scripts/', afin de conserver la validité des chemins relatifs définis dans les scripts.
