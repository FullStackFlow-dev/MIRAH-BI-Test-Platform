import logging
from urllib.parse import quote_plus

import pandas as pd
from sqlalchemy import create_engine

from configs.settings import (
    MSSQL_CONFIG,
    SILVER_FILES,
    LOG_LEVEL
)


# LOGGING

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# SQL SERVER CONNECTION

connection_string = (
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={MSSQL_CONFIG['host']},{MSSQL_CONFIG['port']};"
    f"DATABASE={MSSQL_CONFIG['database']};"
    f"UID={MSSQL_CONFIG['user']};"
    f"PWD={MSSQL_CONFIG['password']};"
    f"TrustServerCertificate=yes;"
)

params = quote_plus(connection_string)

DATABASE_URL = (
    f"mssql+pyodbc:///?odbc_connect={params}"
)

engine = create_engine(
    DATABASE_URL,
    fast_executemany=True
)


# LOAD TABLE

def load_table(
    table_name: str,
    parquet_file
):

    logger.info("=" * 60)
    logger.info(f"LECTURE : {parquet_file}")

    df = pd.read_parquet(
        parquet_file
    )

    logger.info(
        f"TABLE = {table_name}"
    )

    logger.info(
        f"LIGNES = {len(df):,}"
    )

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="append",
        index=False,
        chunksize=5000
    )

    logger.info(
        f"{table_name} chargé avec succès."
    )


# MAIN

def main():

    logger.info("=" * 60)
    logger.info("CHARGEMENT SQL SERVER")
    logger.info("=" * 60)

    load_table(
        "restaurants",
        SILVER_FILES["restaurants"]
    )

    load_table(
        "clients",
        SILVER_FILES["clients"]
    )

    load_table(
        "commandes",
        SILVER_FILES["commandes"]
    )

    load_table(
        "paiements",
        SILVER_FILES["paiements"]
    )

    load_table(
        "avis",
        SILVER_FILES["avis"]
    )

    logger.info("=" * 60)
    logger.info("SQL SERVER TERMINÉ")
    logger.info("=" * 60)

    engine.dispose()


if __name__ == "__main__":
    main()