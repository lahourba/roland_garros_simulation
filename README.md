# Simulation de Roland Garros

Ce projet Python simule le tournoi de Roland Garros pour estimer la probabilité qu'un joueur français remporte le tournoi. Il utilise des données hypothétiques basées sur les classements des joueurs et catégorise chaque joueur en fonction de sa position dans le classement mondial.

## Fonctionnalités

- **Catégorisation des joueurs** : Les joueurs sont classés en différentes catégories (Top 10, Top 20, Top 30, Non-Seeded, Qualifier) selon leur tête de série.
- **Simulation de matchs** : Les matchs sont simulés en tenant compte des probabilités de victoire basées sur les catégories des joueurs.
- **Simulation du tournoi** : Le tournoi entier est simulé pour déterminer le vainqueur.
- **Estimation de probabilité** : Calcule la probabilité qu'un joueur français gagne Roland Garros.

## Hypothèses de victoire

Les probabilités de victoire sont basées sur la catégorisation des joueurs :
- **Top 10** :
  - Contre Top 10 : 50%
  - Contre Top 20 : 60%
  - Contre Top 30 : 65%
  - Contre Non-Seeded : 70%
  - Contre Qualifier : 80%
- **Top 20** :
  - Contre Top 10 : 40%
  - Contre Top 20 : 50%
  - Contre Top 30 : 55%
  - Contre Non-Seeded : 60%
  - Contre Qualifier : 70%
- **Top 30** :
  - Contre Top 10 : 35%
  - Contre Top 20 : 45%
  - Contre Top 30 : 50%
  - Contre Non-Seeded : 55%
  - Contre Qualifier : 65%
- **Non-Seeded** :
  - Contre Top 10 : 20%
  - Contre Top 20 : 30%
  - Contre Top 30 : 40%
  - Contre Non-Seeded : 50%
  - Contre Qualifier : 65%
- **Qualifier** :
  - Contre Top 10 : 5%
  - Contre Top 20 : 10%
  - Contre Top 30 : 20%
  - Contre Non-Seeded : 40%
  - Contre Qualifier : 50%

## Prérequis

- Python 3.x
- Pandas
- NumPy

## Installation

Assurez-vous d'avoir Python installé sur votre machine. Vous pouvez installer les dépendances nécessaires avec pip :

```bash
pip install pandas numpy
```

## Contribution

Les contributions à ce projet sont les bienvenues. N'hésitez pas à forker le dépôt, apporter vos modifications et soumettre une pull request.

