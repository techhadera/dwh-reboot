import pandas as pd
from sqlalchemy import create_engine
from airflow.models import Variable


def get_titanic_dataset():
    url = 'https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv'
    df = pd.read_csv(url)
    return df.to_json()


def pivot_dataset(**kwargs) -> dict:
    ti =  kwargs['ti']
    titanic_json = ti.xcom_pull(key=None, task_ids='get_titanic_dataset')
    titanic_df = pd.read_json(titanic_json)
    titanic_pivot_df = titanic_df.pivot_table(index=['Sex'],
                                              columns=['Pclass'],
                                              values='Name',
                                              aggfunc='count').reset_index()

    return titanic_pivot_df.to_json()

    
def mean_fare_per_class(**kwargs) -> dict:
    ti = kwargs['ti']
    titanic_json = ti.xcom_pull(key=None, task_ids='get_titanic_dataset')
    titanic_df = pd.read_json(titanic_json)
    titanic_mean_fares_df = titanic_df.pivot_table(index=['Pclass'],
                                                   values='Fare',
                                                   aggfunc='mean').reset_index().rename(columns={'Fare': 'MeanFare'})
    return titanic_mean_fares_df.to_json()


def dump_to_db(**kwargs):
    engine = create_engine('postgresql://airflow:air@localhost:5432/data_warehouse')
    ti = kwargs['ti']

    titanic_mean_fares_df = pd.read_json(ti.xcom_pull(task_ids='mean_fares_dataset'))
    mean_fares_tbl_name = Variable.get('mean_fares_tbl')
    titanic_mean_fares_df.to_sql(mean_fares_tbl_name, con=engine)

    titanic_pivot_df = pd.read_json(ti.xcom_pull(task_ids='pivot_dataset'))
    pivot_tbl_name = Variable.get('pivot_tbl')
    titanic_pivot_df.to_sql(pivot_tbl_name, con=engine)
