import logging

from pathlib import Path

import pandas as pd

from urllib.parse import quote_plus

from sqlalchemy import (
    create_engine,
    text
)

from sqlalchemy.exc import SQLAlchemyError

from configs.settings import (
    POSTGRES_CONFIG,
    BRONZE_FILES,
    LOG_LEVEL
)


# LOGGING

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# DATABASE URL

password = quote_plus(
    POSTGRES_CONFIG["password"]
)

DATABASE_URL = (
    f"postgresql+psycopg://"
    f"{POSTGRES_CONFIG['user']}:"
    f"{password}@"
    f"{POSTGRES_CONFIG['host']}:"
    f"{POSTGRES_CONFIG['port']}/"
    f"{POSTGRES_CONFIG['database']}"
)


# ENGINE

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)


# CONNECTION TEST

def test_connection():

    try:

        with engine.connect() as connection:

            connection.execute(
                text("SELECT 1")
            )

        logger.info(
            "âœ… Connexion PostgreSQL rÃ©ussie."
        )

        return True

    except Exception as error:

        logger.error(
            f"Connexion PostgreSQL impossible : {error}"
        )

        return False


# LOAD TABLE

def load_table(table_name, file_path):

    try:

        if not Path(file_path).exists():

            logger.error(
                f"Fichier absent : {file_path}"
            )

            return 0

        logger.info(
            f"Lecture : {file_path}"
        )

        df = pd.read_json(
            file_path,
            lines=True
        )


# CONVERSION DES DATES

        if "date_commande" in df.columns:
            df["date_commande"] = pd.to_datetime(
                df["date_commande"],
                errors="coerce"
            )

        if "date_paiement" in df.columns:
            df["date_paiement"] = pd.to_datetime(
                df["date_paiement"],
                errors="coerce"
            )

        if "date_avis" in df.columns:
            df["date_avis"] = pd.to_datetime(
                df["date_avis"],
                errors="coerce"
            )

        logger.info(
            f"{len(df):,} lignes trouvÃ©es."
        )

        df.to_sql(
            name=table_name,
            con=engine,
            if_exists="append",
            index=False,
            chunksize=500
        )

        logger.info(
            f"Table '{table_name}' chargÃ©e."
        )

        return len(df)

    except FileNotFoundError:

        logger.error(
            f"Fichier introuvable : {file_path}"
        )

        return 0

    except SQLAlchemyError as error:

        logger.error(
            f"Erreur SQLAlchemy : {error}"
        )

        return 0

    except Exception as error:

        logger.error(
            f"Erreur inattendue : {error}"
        )

        return 0

# MAIN

def main():

    logger.info(
        "=" * 60
    )

    logger.info(
        "DÃ©marrage du chargement Bronze â†’ PostgreSQL"
    )

    logger.info(
        "=" * 60
    )

    if not test_connection():

        return

    total_loaded = 0

    for table_name, file_path in BRONZE_FILES.items():

        total_loaded += load_table(
            table_name,
            file_path
        )

    logger.info(
        "=" * 60
    )

    logger.info(
        f"Chargement terminÃ©."
    )

    logger.info(
        f"Total des enregistrements chargÃ©s : {total_loaded:,}"
    )

    logger.info(
        "=" * 60
    )

    engine.dispose()


# ENTRYPOINT

if __name__ == "__main__":

    main()
