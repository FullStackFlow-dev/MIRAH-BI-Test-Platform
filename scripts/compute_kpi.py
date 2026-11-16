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
    logger.info("CALCUL KPI")
    logger.info("=" * 60)

    commandes = pd.read_parquet(
        SILVER_FILES["commandes"]
    )

    paiements = pd.read_parquet(
        SILVER_FILES["paiements"]
    )

    avis = pd.read_parquet(
        SILVER_FILES["avis"]
    )


# KPI PAIEMENTS

    kpi_paiements = (
        paiements
        .groupby(
            "mode_paiement",
            as_index=False
        )
        .agg(
            montant_total=(
                "montant",
                "sum"
            ),
            nb_paiements=(
                "paiement_id",
                "count"
            )
        )
    )

    kpi_paiements["part_pct"] = round(
        (
            kpi_paiements["montant_total"]
            /
            kpi_paiements["montant_total"].sum()
        ) * 100,
        2
    )

    kpi_paiements.to_parquet(
        GOLD_FILES["kpi_paiements"],
        index=False
    )

    logger.info(
        "kpi_paiements.parquet généré"
    )


# KPI SATISFACTION

    kpi_satisfaction = (
        avis
        .groupby(
            "note",
            as_index=False
        )
        .agg(
            nb_avis=(
                "avis_id",
                "count"
            )
        )
        .sort_values("note")
    )

    kpi_satisfaction.to_parquet(
        GOLD_FILES["kpi_satisfaction"],
        index=False
    )

    logger.info(
        "kpi_satisfaction.parquet généré"
    )


# KPI COMMANDES

    kpi_commandes = (
        commandes
        .groupby(
            "canal_commande",
            as_index=False
        )
        .agg(
            chiffre_affaires=(
                "montant",
                "sum"
            ),
            nb_commandes=(
                "commande_id",
                "count"
            ),
            ticket_moyen=(
                "montant",
                "mean"
            )
        )
    )

    kpi_commandes.to_parquet(
        GOLD_FILES["kpi_commandes"],
        index=False
    )

    logger.info(
        "kpi_commandes.parquet généré"
    )

    logger.info("=" * 60)
    logger.info("KPI TERMINÉS")
    logger.info("=" * 60)

if __name__ == "__main__":
    main()