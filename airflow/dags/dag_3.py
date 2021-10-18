import os
import sys
import datetime as dt
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from utils_3 import extract_data, transform_data, load_data

path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, path)

args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2021, 10, 18),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1),
    'depends_on_past': False,
    'provide_context': True,
}

with DAG(
    dag_id='weather_worldweatheronline_api',
    # Изменил периодичность запуска DAG’а на значение “Запуск каждый час”
    schedule_interval='@hourly',
    default_args=args,

) as dag:
    extract_data = PythonOperator(task_id='extract_data', python_callable=extract_data)
    transform_data = PythonOperator(task_id='transform_data', python_callable=transform_data)
    load_data = PythonOperator(task_id='load_data', python_callable=load_data)

    extract_data >> transform_data >> load_data
