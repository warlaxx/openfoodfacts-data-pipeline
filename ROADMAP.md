# Roadmap

Statut détaillé du projet : jalons, décisions, avancement. Le détail des tickets vit dans
Linear (projet **openfoodfacts-data-pipeline**, équipe ABD) ; la documentation dans Notion
(page **Open Food Facts Pipeline**).

## Pourquoi ce projet

Projet portfolio pour passer de développeur intégrateur Java (flux Databricks → Fabric en
Spring Boot chez Prosol, via Amiltone) à **data platform engineer**. Le marché lyonnais attend
PySpark et SQL : ce dépôt les prouve sur un cas réel, avec les réflexes plateforme
(CI/CD, tests, infra as code) que le poste actuel apporte déjà.

## Règle d'or

L'infrastructure, la CI et le tableau de bord peuvent être générés par une IA.
**Les transformations (bronze, silver, gold) et les contrôles qualité sont écrits à la main.**
Un agent ou un assistant ne doit jamais implémenter les fonctions marquées « À toi de jouer » :
il peut expliquer, relire, poser des questions, proposer des tests.

## Décisions

| Date       | Décision | Raison |
|------------|----------|--------|
| 2026-10-21 | PySpark 4.0.1 + Delta 4.0.0, Python 3.12, Java 21 | Versions alignées (Delta 4 exige Spark 4) ; Java 21 déjà installé |
| 2026-10-21 | Démarrage en local sur un échantillon du CSV (50k lignes) | Itérer vite, sans coût cloud ; le cloud vient après |
| 2026-10-21 | `PYSPARK_PYTHON` forcé sur l'interpréteur du venv | Sinon les workers prennent le `python3` système (3.10) → PYTHON_VERSION_MISMATCH |
| 2026-10-21 | Bronze tout en string, append-only | Le bronze reflète la source ; le typage se fait en silver |
| 2026-10-21 | Nom du dépôt : `openfoodfacts-data-pipeline` (au lieu de `openfoodfacts-lakehouse`) | Dépôt déjà créé sous ce nom |

## Jalons

### Jalon 0 — Squelette ✅ (21 octobre 2026)
- [x] Arborescence `src/off_pipeline/{bronze,silver,gold,quality}`
- [x] SparkSession Delta (`spark.py`), chemins centralisés (`config.py`)
- [x] Script d'échantillon `scripts/download_sample.py`
- [x] pytest + test de fumée Delta (écriture, lecture, time travel) au vert
- [x] ruff, Makefile, CI GitHub Actions

### Semaine 1 — Python (→ 28 octobre)
- [ ] Bases Python : types, compréhensions, fonctions, modules, `pathlib`, exceptions
- [ ] `make install` et `make test` au vert sur ta machine
- [ ] Premiers tests pytest sur des fonctions Python pures

### Semaine 2 — Exploration (→ 4 novembre)
- [ ] `make sample`, notebook d'exploration dans `notebooks/`
- [ ] API DataFrame : `select`, `filter`, `withColumn`, `groupBy`, `agg`, `join`
- [ ] Inventaire des problèmes de qualité (nulls, doublons de `code`, valeurs aberrantes)

### Semaine 3 — Bronze (→ 11 novembre)
- [ ] `bronze/ingest.py` : lecture brute + colonnes techniques + écriture Delta
- [ ] Tests unitaires de `add_ingestion_metadata`
- [ ] Historique Delta (`DESCRIBE HISTORY`, time travel)

### Semaine 4 — Début du silver (→ 18 novembre)
- [ ] `silver/products.py` : sélection, typage, nettoyage
- [ ] Dédoublonnage par fenêtre (`row_number` sur `code`, tri par `last_modified_t`)
- [ ] Tests unitaires avec chispa

### Ensuite
- [ ] Chargement incrémental du bronze
- [ ] Historisation SCD2 avec `MERGE`
- [ ] Modèle en étoile gold
- [ ] Contrôles qualité bloquants
- [ ] Tableau de bord
- [ ] Déploiement cloud (Databricks ou Fabric) avec Terraform et OIDC dans la CI

## Objectifs carrière (hors code, suivis dans Linear)

- Certification : Databricks Data Engineer Associate ou DP-700
- Aligner CV, LinkedIn et Malt (Malt affiche encore « Full-stack Java »)
- Critères de sortie de mission (18–24 mois) : pipelines de transformation, Terraform maîtrisé,
  certification, Python, réalisations chiffrées
