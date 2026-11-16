from pathlib import Path
from dotenv import load_dotenv
import os


# ENVIRONMENT

load_dotenv()


# PROJECT

PROJECT_NAME = "MIRAH-BI Test Platform"

PIPELINE_NAME = os.getenv(
    "PIPELINE_NAME",
    "mirah-bi-test-platform"
)

ENVIRONMENT = os.getenv(
    "ENVIRONMENT",
    "development"
)


# PATHS

BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG_DIR = BASE_DIR / "configs"

DATA_DIR = BASE_DIR / "data"

BRONZE_DIR = DATA_DIR / "bronze"
SILVER_DIR = DATA_DIR / "silver"
GOLD_DIR = DATA_DIR / "gold"

SQL_DIR = BASE_DIR / "sql"

LOG_DIR = BASE_DIR / "logs"

DAGS_DIR = BASE_DIR / "dags"

NOTEBOOKS_DIR = BASE_DIR / "notebooks"


# CREATE PROJECT FOLDERS

for folder in [
    DATA_DIR,
    BRONZE_DIR,
    SILVER_DIR,
    GOLD_DIR,
    SQL_DIR,
    LOG_DIR,
    DAGS_DIR,
    NOTEBOOKS_DIR
]:
    folder.mkdir(
        parents=True,
        exist_ok=True
    )


# LOGGING

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
)


# DATABASES

DATABASES = {

    "postgres": {

        "host": os.getenv(
            "POSTGRES_HOST",
            "localhost"
        ),

        "port": os.getenv(
            "POSTGRES_PORT",
            "5434"
        ),

        "database": os.getenv(
            "POSTGRES_DB",
            "restaurant_bi"
        ),

        "user": os.getenv(
            "POSTGRES_USER",
            "database_engineer"
        ),

        "password": os.getenv(
            "POSTGRES_PASSWORD",
            ""
        )
    },

    "mysql": {

        "host": os.getenv(
            "MYSQL_HOST",
            "localhost"
        ),

        "port": os.getenv(
            "MYSQL_PORT",
            "3306"
        ),

        "database": os.getenv(
            "MYSQL_DB",
            "restaurant_bi"
        ),

        "user": os.getenv(
            "MYSQL_USER",
            "database_engineer"
        ),

        "password": os.getenv(
            "MYSQL_PASSWORD",
            ""
        )
    },

    "mssql": {

        "host": os.getenv(
            "MSSQL_HOST",
            "localhost"
        ),

        "port": os.getenv(
            "MSSQL_PORT",
            "1433"
        ),

        "database": os.getenv(
            "MSSQL_DB",
            "restaurant_bi"
        ),

        "user": os.getenv(
            "MSSQL_USER",
            "database_engineer"
        ),

        "password": os.getenv(
            "MSSQL_PASSWORD",
            ""
        )
    },

    "snowflake": {

        "account": os.getenv(
            "SNOWFLAKE_ACCOUNT",
            ""
        ),

        "user": os.getenv(
            "SNOWFLAKE_USER",
            ""
        ),

        "password": os.getenv(
            "SNOWFLAKE_PASSWORD",
            ""
        ),

        "warehouse": os.getenv(
            "SNOWFLAKE_WAREHOUSE",
            ""
        ),

        "database": os.getenv(
            "SNOWFLAKE_DATABASE",
            ""
        ),

        "schema": os.getenv(
            "SNOWFLAKE_SCHEMA",
            "PUBLIC"
        )
    }
}


# BACKWARD COMPATIBILITY

POSTGRES_CONFIG = DATABASES["postgres"]

MYSQL_CONFIG = DATABASES["mysql"]

MSSQL_CONFIG = DATABASES["mssql"]

SNOWFLAKE_CONFIG = DATABASES["snowflake"]


# DATA GENERATION

NB_RESTAURANTS = int(
    os.getenv(
        "NB_RESTAURANTS",
        "1000"
    )
)

NB_CLIENTS = int(
    os.getenv(
        "NB_CLIENTS",
        "50000"
    )
)

NB_COMMANDES = int(
    os.getenv(
        "NB_COMMANDES",
        "200000"
    )
)

NB_AVIS = int(
    os.getenv(
        "NB_AVIS",
        "30000"
    )
)

NB_PAIEMENTS = int(
    os.getenv(
        "NB_PAIEMENTS",
        "200000"
    )
)


# BRONZE FILES

BRONZE_FILES = {

    "restaurants":
        BRONZE_DIR / "restaurants.json",

    "clients":
        BRONZE_DIR / "clients.json",

    "commandes":
        BRONZE_DIR / "commandes.json",

    "paiements":
        BRONZE_DIR / "paiements.json",

    "avis":
        BRONZE_DIR / "avis.json"
}


# SILVER FILES

SILVER_FILES = {

    "restaurants":
        SILVER_DIR / "restaurants_clean.parquet",

    "clients":
        SILVER_DIR / "clients_clean.parquet",

    "commandes":
        SILVER_DIR / "commandes_clean.parquet",

    "paiements":
        SILVER_DIR / "paiements_clean.parquet",

    "avis":
        SILVER_DIR / "avis_clean.parquet"
}


# GOLD FILES

GOLD_FILES = {

    "ca_restaurant":
        GOLD_DIR / "ca_par_restaurant.parquet",

    "ca_quartier":
        GOLD_DIR / "ca_par_quartier.parquet",

    "top_restaurants":
        GOLD_DIR / "top_restaurants.parquet",

    "kpi_global":
        GOLD_DIR / "kpi_global.parquet",

    "kpi_paiements":
        GOLD_DIR / "kpi_paiements.parquet",

    "kpi_satisfaction":
        GOLD_DIR / "kpi_satisfaction.parquet",

    "kpi_commandes":
        GOLD_DIR / "kpi_commandes.parquet"
}


# TEST CONFIG

if __name__ == "__main__":

    print("CONFIG POSTGRES")
    print(POSTGRES_CONFIG)

    print()
    print("HOST =", POSTGRES_CONFIG["host"])
    print("USER =", POSTGRES_CONFIG["user"])
