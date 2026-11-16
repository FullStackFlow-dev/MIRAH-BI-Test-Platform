import logging
import pandas as pd
from urllib.parse import quote_plus

from sqlalchemy import create_engine

from configs.settings import (
    MSSQL_CONFIG,
    BRONZE_FILES,
    LOG_LEVEL
)

# LOGGING

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

# SQL SERVER CONNECTION

params = quote_plus(
    (
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={MSSQL_CONFIG['host']},{MSSQL_CONFIG['port']};"
        f"DATABASE={MSSQL_CONFIG['database']};"
        f"UID={MSSQL_CONFIG['user']};"
        f"PWD={MSSQL_CONFIG['password']};"
        f"Encrypt=yes;"
        f"TrustServerCertificate=yes;"
    )
)

DATABASE_URL = (
    f"mssql+pyodbc:///?odbc_connect={params}"
)

engine = create_engine(
    DATABASE_URL
)

# LOAD

def load_table(table_name, json_file):

    logger.info("=" * 60)
    logger.info(f"LECTURE : {json_file}")

    df = pd.read_json(
        json_file,
        lines=True
    )

    bronze_table = f"bronze_{table_name}"

    logger.info(
        f"TABLE = {bronze_table}"
    )

    logger.info(
        f"LIGNES = {len(df):,}"
    )

    df.to_sql(
        name=bronze_table,
        con=engine,
        if_exists="replace",
        index=False,
        chunksize=5000
    )

    logger.info(
        f"{bronze_table} chargé avec succès."
    )

# MAIN

def main():

    logger.info("=" * 60)
    logger.info("CHARGEMENT BRONZE SQL SERVER")
    logger.info("=" * 60)

    for table_name, file_path in BRONZE_FILES.items():

        load_table(
            table_name,
            file_path
        )

    logger.info("=" * 60)
    logger.info("BRONZE SQL SERVER TERMINÉ")
    logger.info("=" * 60)

if __name__ == "__main__":
    main()