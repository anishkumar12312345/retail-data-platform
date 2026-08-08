from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="retail_pipeline",
    start_date=datetime(2026, 8, 1),
    schedule="@daily",
    catchup=False,
    default_args={
        "retries": 2,
        "retry_delay": timedelta(minutes=1),
    },

) as dag:

    transform_data = BashOperator(
        task_id="transform_data",
        bash_command="cd /mnt/c/retail-data-platform && python transform.py",
    )

    run_analytics = BashOperator(
        task_id="run_analytics",
        bash_command="cd /mnt/c/retail-data-platform && python analytics.py",
    )

    transform_data >> run_analytics
