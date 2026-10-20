"""Gold layer: star schema for analytics.

Modèle cible :
- ``fact_nutrition``  (grain : un produit courant) -> clés vers les dimensions + mesures /100 g
- ``dim_product``, ``dim_brand``, ``dim_category``, ``dim_country``

TODO (à écrire toi-même) : construire dimensions (avec clés de substitution) puis la table de
faits, à partir de la table silver (``is_current = true``).
"""


def run() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    run()
