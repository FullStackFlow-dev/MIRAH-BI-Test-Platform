import logging
from pathlib import Path
from urllib.parse import quote_plus

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

from configs.settings import (
    MYSQL_CONFIG,
    BRONZE_FILES,
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
    f"{MYSQL_CONFIG['database']}?"
    f"charset=utf8mb4"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600
)


# CONNECTION TEST

def test_connection():
    try:
        with engine.connect() as connection:
            connection.execute(
                text("SELECT 1")
            )

        logger.info("Connexion MySQL réussie.")
        return True

    except Exception as error:
        logger.error(
            f"Connexion MySQL impossible : {error}"
        )
        return False


# DATA CLEANING

def prepare_dataframe(df):
    date_columns = [
        "date_commande",
        "date_paiement",
        "date_avis"
    ]

    for column in date_columns:
        if column in df.columns:
            df[column] = pd.to_datetime(
                df[column],
                errors="coerce"
            )

    return df


# LOAD TABLE

def load_table(source_name, file_path):
    file_path = Path(file_path)
    table_name = f"bronze_{source_name}"

    try:
        if not file_path.exists():
            logger.error(
                f"Fichier absent : {file_path}"
            )
            return 0

        logger.info("=" * 60)
        logger.info(f"LECTURE : {file_path}")

        df = pd.read_json(
            file_path,
            lines=True
        )

        df = prepare_dataframe(df)

        logger.info(f"TABLE = {table_name}")
        logger.info(f"LIGNES = {len(df):,}")

        df.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace",
            index=False,
            chunksize=5000
        )

        logger.info(
            f"{table_name} chargé avec succès."
        )

        return len(df)

    except ValueError as error:
        logger.error(
            f"Erreur de lecture JSON pour {file_path} : {error}"
        )
        return 0

    except SQLAlchemyError as error:
        logger.error(
            f"Erreur SQLAlchemy pour {table_name} : {error}"
        )
        return 0

    except Exception as error:
        logger.error(
            f"Erreur inattendue pour {table_name} : {error}"
        )
        return 0


# MAIN

def main():
    logger.info("=" * 60)
    logger.info("CHARGEMENT BRONZE VERS MYSQL")
    logger.info("=" * 60)

    if not test_connection():
        engine.dispose()
        return

    total_loaded = 0

    for source_name, file_path in BRONZE_FILES.items():
        total_loaded += load_table(
            source_name,
            file_path
        )

    logger.info("=" * 60)
    logger.info("CHARGEMENT MYSQL BRONZE TERMINÉ")
    logger.info(
        f"TOTAL CHARGÉ = {total_loaded:,} lignes"
    )
    logger.info("=" * 60)

    engine.dispose()


if __name__ == "__main__":
    main()