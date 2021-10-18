import os
import pandas as pd
import datetime
import json
import csv
import requests
from airflow.models import Variable
from sqlalchemy import create_engine, insert

folder = os.path.expanduser('~')+'/data_dags/'
json_name_file = 'data_json.json'
csv_name_file = 'data_csv.csv'
key_api = Variable.get("KEY_API")
сity = 'Ulyanovsk'
moscow_timezone = 3


def extract_data():
    response = requests.get(
        'http://api.worldweatheronline.com/premium/v1/weather.ashx',
        params={
            'q': '{}'.format(сity),
            'format': 'json',
            'FX': 'no',
            'num_of_days': 1,
            'key': key_api,
            'includelocation': 'no'
        },
        headers={
            'Authorization': key_api
        }
    )

    if response.status_code == 200:
        json_data = response.json()
        print(json.dumps(json_data, indent=2))

        with open(folder + json_name_file, 'w') as f:
            json.dump(json_data, f, indent=2)
            f.close()


def transform_data():
    with open(folder + json_name_file, 'r') as jd:
        json_data = json.load(jd)
        print(json_data)
        jd.close()

    value_list = []

    start_utc = datetime.datetime.utcnow()
    start_moscow = start_utc + datetime.timedelta(hours=moscow_timezone)
    city = json_data['data']['request'][0]['query']
    observation_time = json_data['data']['current_condition'][0]['observation_time']
    temp = json_data['data']['current_condition'][0]['temp_C']
    humidity = json_data['data']['current_condition'][0]['humidity']

    # Время наблюдения из json'а
    value_list.append(pd.to_datetime(observation_time).strftime('%Y-%m-%d %H:%M:%S'))
    res_df = pd.DataFrame(value_list, columns=['observation_time'])

    # Время запроса (по Москве)
    res_df["date_from_msk"] = start_moscow
    res_df["date_from_msk"] = pd.to_datetime(res_df["date_from_msk"]).dt.strftime('%Y-%m-%d %H:%M:%S')
    # Время запроса (по UTC)
    res_df["date_from_utc"] = start_utc
    res_df["date_from_utc"] = pd.to_datetime(res_df["date_from_utc"]).dt.strftime('%Y-%m-%d %H:%M:%S')

    # Город наблюдения
    res_df["city_observation"] = city

    # Температура
    res_df["city_temp_c"] = temp

    # Влажность
    res_df["city_humidity"] = humidity

    # Убрал формирование csv файла во втором task’е(transform_data)
    return res_df.to_json()


def load_data(**kwargs):
    engine = create_engine('postgresql://airflow:air@localhost:5432/data_warehouse')
    ti = kwargs['ti']

    # Передал в load_data данные полученные на предыдущем шаге с помощью XCom
    weather_json = ti.xcom_pull(key=None, task_ids='transform_data')
    weather_df = pd.read_json(weather_json)
    schema = ['observation_time', 'date_from_msk', 'date_from_utc',
              'city_observation', 'city_temp_c', 'city_humidity']

    # Изменить задачу load_data на insert в созданную таблицу.
    weather_df.to_sql('weather_worldweatheronline', engine, if_exists='append', index=False)

