import os
import sys
import datetime as dt
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from utils_2 import get_titanic_dataset, pivot_dataset, mean_fare_per_class, dump_to_db


path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, path)

args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2021, 10, 15),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1),
    'depends_on_past': False,
}

with DAG(
        dag_id='titanic_xcom',
        schedule_interval=None,
        default_args=args,
) as dag:

    first_task = BashOperator(
        task_id='first_task',
        bash_command='echo "Here we start! Info: run_id={{ run_id }} | dag_run={{ dag_run }}"',
        dag=dag,
    )

    create_titanic_dataset = PythonOperator(
        task_id='get_titanic_dataset',
        python_callable=get_titanic_dataset,
        dag=dag,
    )

    pivot_titanic_dataset = PythonOperator(
        task_id='pivot_dataset',
        provide_context=True,
        python_callable=pivot_dataset,
        dag=dag,
    )

    mean_fares_titanic_dataset = PythonOperator(
        task_id='mean_fares_dataset',
        provide_context=True,
        python_callable=mean_fare_per_class,
        dag=dag,
    )

    dump_to_db = PythonOperator(
        task_id='dump_to_db',
        provide_context=True,
        python_callable=dump_to_db,
        dag=dag,
    )

    last_task = BashOperator(
        task_id='last_task',
        bash_command='echo "Pipeline finished! Execution date is {{ ds }}"',
        dag=dag,
    )
    
    first_task >> create_titanic_dataset >> [pivot_titanic_dataset, mean_fares_titanic_dataset]\
        >> dump_to_db >> last_task
