import logging

import pandas as pd

from configs.settings import (
    SILVER_FILES,
    GOLD_FILES,
    LOG_LEVEL
)


# LOGGING

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# MAIN

def main():

    logger.info("=" * 60)
    logger.info("CONSTRUCTION GOLD")
    logger.info("=" * 60)

    # LOAD SILVER

    restaurants = pd.read_parquet(
        SILVER_FILES["restaurants"]
    )

    commandes = pd.read_parquet(
        SILVER_FILES["commandes"]
    )

    avis = pd.read_parquet(
        SILVER_FILES["avis"]
    )

    # CA PAR RESTAURANT

    ca_restaurant = (
        commandes
        .groupby("restaurant_id", as_index=False)
        .agg(
            chiffre_affaires=(
                "montant",
                "sum"
            ),
            nb_commandes=(
                "commande_id",
                "count"
            )
        )
    )

    ca_restaurant = (
        ca_restaurant
        .merge(
            restaurants[
                [
                    "restaurant_id",
                    "name",
                    "quartier"
                ]
            ],
            on="restaurant_id",
            how="left"
        )
    )

    ca_restaurant.to_parquet(
        GOLD_FILES["ca_restaurant"],
        index=False
    )

    logger.info(
        "ca_par_restaurant.parquet généré"
    )

    # CA PAR QUARTIER

    ca_quartier = (
        ca_restaurant
        .groupby(
            "quartier",
            as_index=False
        )
        .agg(
            chiffre_affaires=(
                "chiffre_affaires",
                "sum"
            ),
            nb_commandes=(
                "nb_commandes",
                "sum"
            )
        )
    )

    ca_quartier.to_parquet(
        GOLD_FILES["ca_quartier"],
        index=False
    )

    logger.info(
        "ca_par_quartier.parquet généré"
    )

    # TOP RESTAURANTS

    top_restaurants = (
        ca_restaurant
        .sort_values(
            "chiffre_affaires",
            ascending=False
        )
        .head(20)
    )

    top_restaurants.to_parquet(
        GOLD_FILES["top_restaurants"],
        index=False
    )

    logger.info(
        "top_restaurants.parquet généré"
    )

    # KPI GLOBAL

    note_moyenne = avis["note"].mean()

    kpi_global = pd.DataFrame(
        [
            {
                "ca_global":
                    commandes["montant"].sum(),

                "nb_commandes":
                    len(commandes),

                "nb_restaurants":
                    len(restaurants),

                "ticket_moyen":
                    commandes["montant"].mean(),

                "note_moyenne":
                    round(
                        note_moyenne,
                        2
                    )
            }
        ]
    )

    kpi_global.to_parquet(
        GOLD_FILES["kpi_global"],
        index=False
    )

    logger.info(
        "kpi_global.parquet généré"
    )

    logger.info("=" * 60)
    logger.info("GOLD TERMINÉ")
    logger.info("=" * 60)

# ENTRYPOINT

if __name__ == "__main__":
    main()