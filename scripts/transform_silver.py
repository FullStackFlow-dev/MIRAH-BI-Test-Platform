import logging

import pandas as pd

from configs.settings import (
    BRONZE_FILES,
    SILVER_FILES,
    LOG_LEVEL
)

# =========================================================
# LOGGING
# =========================================================

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

# =========================================================
# CLEANING
# =========================================================

def clean_dataframe(table_name, df):

    df = df.drop_duplicates()

    if table_name == "restaurants":

        df["restaurant_id"] = df["restaurant_id"].astype(int)

        if "rating" in df.columns:
            df["rating"] = df["rating"].astype(float)

        if "review_count" in df.columns:
            df["review_count"] = df["review_count"].astype(int)

    elif table_name == "clients":

        df["client_id"] = df["client_id"].astype(int)

        if "email" in df.columns:
            df["email"] = (
                df["email"]
                .str.strip()
                .str.lower()
            )

    elif table_name == "commandes":

        df["commande_id"] = df["commande_id"].astype(int)

        df["date_commande"] = pd.to_datetime(
            df["date_commande"],
            format="mixed",
            errors="coerce"
        )

    elif table_name == "paiements":

        df["paiement_id"] = df["paiement_id"].astype(int)

        df["date_paiement"] = pd.to_datetime(
            df["date_paiement"],
            format="mixed",
            errors="coerce"
        )

    elif table_name == "avis":

        df["avis_id"] = df["avis_id"].astype(int)

        df["date_avis"] = pd.to_datetime(
            df["date_avis"],
            format="mixed",
            errors="coerce"
        )

    return df


# =========================================================
# MAIN
# =========================================================

def main():

    logger.info("=" * 60)
    logger.info("TRANSFORMATION SILVER")
    logger.info("=" * 60)

    total = 0

    for table_name in BRONZE_FILES:

        bronze_file = BRONZE_FILES[table_name]
        silver_file = SILVER_FILES[table_name]

        logger.info(
            f"Lecture : {bronze_file}"
        )

        df = pd.read_json(
            bronze_file,
            lines=True
        )

        df = clean_dataframe(
            table_name,
            df
        )

        logger.info(
            f"Export : {silver_file}"
        )

        df.to_parquet(
            silver_file,
            index=False
        )

        total += len(df)

        logger.info(
            f"{table_name} : {len(df):,} lignes"
        )

    logger.info("=" * 60)
    logger.info(
        f"Total Silver : {total:,}"
    )
    logger.info("=" * 60)


if __name__ == "__main__":
    main()