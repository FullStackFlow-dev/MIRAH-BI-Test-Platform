import logging

import pandas as pd

from urllib.parse import quote_plus

from sqlalchemy import create_engine

from configs.settings import (
    MYSQL_CONFIG,
    GOLD_FILES,
    LOG_LEVEL
)


# LOGGING

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# MYSQL CONNECTION

password = quote_plus(
    MYSQL_CONFIG["password"]
)

DATABASE_URL = (
    f"mysql+pymysql://"
    f"{MYSQL_CONFIG['user']}:"
    f"{password}@"
    f"{MYSQL_CONFIG['host']}:"
    f"{MYSQL_CONFIG['port']}/"
    f"{MYSQL_CONFIG['database']}"
)

engine = create_engine(
    DATABASE_URL
)


# LOAD

def load_table(table_name, parquet_file):

    logger.info(
        f"Lecture : {parquet_file}"
    )

    df = pd.read_parquet(
        parquet_file
    )

    logger.info(
        f"Chargement MySQL : {table_name}"
    )

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    logger.info(
        f"{table_name} chargé."
    )



# MAIN

def main():

    logger.info("=" * 60)
    logger.info("CHARGEMENT MYSQL")
    logger.info("=" * 60)

    load_table(
        "gold_ca_restaurant",
        GOLD_FILES["ca_restaurant"]
    )

    load_table(
        "gold_ca_quartier",
        GOLD_FILES["ca_quartier"]
    )

    load_table(
        "gold_top_restaurants",
        GOLD_FILES["top_restaurants"]
    )

    load_table(
        "gold_kpi_global",
        GOLD_FILES["kpi_global"]
    )

    load_table(
        "gold_kpi_paiements",
        GOLD_FILES["kpi_paiements"]
    )

    load_table(
        "gold_kpi_satisfaction",
        GOLD_FILES["kpi_satisfaction"]
    )

    load_table(
        "gold_kpi_commandes",
        GOLD_FILES["kpi_commandes"]
    )

    logger.info("=" * 60)
    logger.info("MYSQL TERMINÉ")
    logger.info("=" * 60)

    engine.dispose()


if __name__ == "__main__":
    main()
