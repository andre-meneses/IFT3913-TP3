# TP3 - Qualité de Logiciel et Métriques

## Membres de l'équipe
- André Meneses
- Paul Godbert

## Résumé
Cette analyse statistique s'appuie sur trois scripts Python : `plot_data.py`, `stats.py` et `experience.py`. Le premier, `plot_data.py`, est dédié à la génération de graphiques tels que les boîtes à moustaches et les nuages de points. Les informations clés pour les boîtes à moustaches sont enregistrées dans `output/statistiques_metriques.csv`. Quant à `stats.py`, il effectue des tests de normalité sur les données et calcule les coefficients de corrélation, en fonction des résultats de ces tests. Un seuil de signification de 5% est adopté. Ce script génère également les lignes de régression linéaire entre les variables "TASSERT", "TLOC" et "TASSERT", "WMC". Tous les graphiques produits sont sauvegardés dans le dossier `figures`, tandis que les fichiers CSV sont stockés dans `output`. Finalement, le script `experience.py` se charge de réaliser la quasi-experience permettant de valider l'hypotèse données dans la partie 3. Ce script s'occupe de diviser le jeu de données en deux parties (toutes les classes dont TASSERT < 20 d'un côté et celles avec TASSERT > 20 de l'autre). il calcule ensuite toutes les variables (médianne, quartiles, longueur, limites et points extrêmes) sur chacune des métriques, pour chacun des deux groupes. Ces données sont stockée dans `output/quasi-experience/`. Le script réalise aussi deux boxplot permettant de visualiser ces données. Ces boxplots peuvent êtres trouvés dans `figures/quasi-experience/`.

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
