from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


PROJECT_DIR = "/opt/airflow/dags/MIRAH-BI Test Platform"


with DAG(
    dag_id="mirah_bi_restaurant_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=[
        "mirah-bi",
        "restaurant",
        "bronze",
        "postgresql",
        "silver",
        "gold",
        "kpi"
    ],
    description="Pipeline complet Restaurant MIRAH-BI"
) as dag:

    generate_data = BashOperator(
        task_id="generate_bronze_data",
        bash_command=f"""
        cd "{PROJECT_DIR}" &&
        python -m scripts.generate_data
        """
    )

    load_postgres = BashOperator(
        task_id="load_postgres",
        bash_command=f"""
        cd "{PROJECT_DIR}" &&
        python -m scripts.load_postgres
        """
    )

    transform_silver = BashOperator(
        task_id="transform_silver",
        bash_command=f"""
        cd "{PROJECT_DIR}" &&
        python -m scripts.transform_silver
        """
    )

    build_gold = BashOperator(
        task_id="build_gold",
        bash_command=f"""
        cd "{PROJECT_DIR}" &&
        python -m scripts.build_gold
        """
    )

    compute_kpi = BashOperator(
        task_id="compute_kpi",
        bash_command=f"""
        cd "{PROJECT_DIR}" &&
        python -m scripts.compute_kpi
        """
    )

    (
        generate_data
        >> load_postgres
        >> transform_silver
        >> build_gold
        >> compute_kpi
    )