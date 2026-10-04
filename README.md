# Customer Sales Analysis

## 📊 Présentation du projet

Ce projet a pour objectif d'analyser des données de ventes afin d'identifier les principales tendances commerciales et de produire des indicateurs utiles à la prise de décision.

L'analyse est réalisée avec Python et les bibliothèques Pandas, NumPy et Matplotlib.

## 🎯 Objectifs

- Explorer et comprendre les données de ventes
- Nettoyer et préparer les données
- Identifier les éventuelles valeurs manquantes ou anomalies
- Calculer les principaux indicateurs de performance (KPI)
- Analyser les ventes et le chiffre d'affaires
- Identifier les tendances commerciales
- Analyser les performances par produit, région et client
- Étudier l'évolution mensuelle du chiffre d'affaires
- Créer des visualisations permettant de mieux interpréter les résultats
- Produire des insights utiles pour l'analyse commerciale

## 🛠️ Technologies utilisées

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook / VS Code

## 📁 Données

Le projet utilise un fichier CSV contenant les données de ventes :

`raw_sales.csv`

Les données ont ensuite été nettoyées et préparées pour l'analyse.

## 📈 Analyses réalisées

### Analyse des ventes

L'analyse permet notamment d'étudier :

- Le chiffre d'affaires total
- Le nombre total de commandes
- Le nombre de clients
- Le nombre d'unités vendues
- Le chiffre d'affaires par produit
- Le chiffre d'affaires par région
- Le chiffre d'affaires par client
- L'évolution mensuelle du chiffre d'affaires

### 📊 Visualisations

Plusieurs graphiques ont été générés afin de faciliter l'interprétation des résultats :

- Revenue by Product
- Revenue by Region
- Top 10 Customers by Revenue
- Monthly Revenue Trend
- Sales Dashboard

## 🔎 Principaux résultats

L'analyse a permis d'identifier plusieurs indicateurs importants :

- 💰 **Chiffre d'affaires total :** $598,891.00
- 🛒 **Nombre total de commandes :** 500
- 👥 **Nombre de clients :** 143
- 📦 **Unités vendues :** 1,511
- 🏆 **Produit le plus rentable :** Laptop — $133,689.58
- 🏷️ **Catégorie la plus rentable :** Electronics — $362,114.55
- 🌍 **Région la plus performante :** North — $165,446.41
- 📅 **Meilleur mois :** September 2025 — $68,426.37

## 📂 Structure du projet

```text
customer-sales-analysis/
│
├── customer_sales_analysis.py
├── raw_sales.csv
├── clean_sales.csv
│
├── monthly_sales.png
├── sales_by_customer.png
├── sales_by_product.png
├── sales_by_region.png
├── sales_dashboard.png
│
└── README.md
