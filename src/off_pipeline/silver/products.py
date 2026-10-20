"""Silver layer: cleaned, typed, deduplicated products.

TODO (à écrire toi-même) :
- Sélectionner les colonnes utiles (code, product_name, brands, categories_tags, countries_tags,
  nutriscore_grade, nova_group, energy-kcal_100g, sugars_100g, salt_100g, last_modified_t, ...).
- Typer : nombres en double, timestamps Unix en timestamp, grades en minuscules.
- Nettoyer : codes-barres invalides, valeurs nutritionnelles aberrantes (ex. sucre > 100 g/100 g).
- Dédupliquer sur ``code`` en gardant la version la plus récente (fenêtre + row_number).
- Historisation (SCD type 2) avec ``MERGE`` Delta : ``valid_from``, ``valid_to``, ``is_current``.
"""

from pyspark.sql import DataFrame


def clean_products(bronze_df: DataFrame) -> DataFrame:
    raise NotImplementedError("À toi de jouer : nettoyage et typage")


def deduplicate_latest(df: DataFrame) -> DataFrame:
    raise NotImplementedError("À toi de jouer : dédoublonnage")


def run() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    run()
