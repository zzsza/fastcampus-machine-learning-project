from datetime import datetime, timedelta
from airflow import models
from airflow.operators.bash_operator import BashOperator


default_args = {
    'owner': 'seongyun',
    'depends_on_past': False,
    'start_date': datetime(2019, 11, 22),
    'email': ['zzsza@naver.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
    'project_id': 'geultto'
}

bash_command = """
    python3 /home/airflow/gcs/data/taxi-demand-prediction/main.py --mode predict --dev_env production
"""

with models.DAG(
        dag_id='Predict-taxi_demand_every_1hours',
        description='Predict taxi demand',
        schedule_interval='0 * * * *',  # Every 0 minute
        default_args=default_args) as dag:

    predict_operator = BashOperator(
        dag=dag,
        task_id='predict_demand',
        bash_command=bash_command
    )

    predict_operator
