from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "start_date": datetime(2024, 1, 1),
    "catchup": False
}

with DAG(
    dag_id="upload_csv_to_s3",
    schedule_interval=None,
    default_args=default_args,
    description="Upload local CSV file to AWS S3",
    tags=["s3", "upload"]
) as dag:

    upload_task = BashOperator(
        task_id="upload_to_s3",
        bash_command="python /opt/airflow/scripts/upload_to_s3.py"
    )

    upload_task
