# Практическое задание 1 по теме Airflow 2 урока

1. Выполнить установку Linux.

    * В качестве Linux системы выступает Ubuntu server 20.04, запущенная при помощи WSL.  
    ![sample text](img/hw_1/linux.PNG)  

1. Установить Apache Airflow и инициализировать его на базе данных Postgresql.

    * Создадим виртуальное окружение .air и выполним следущие команды:  
    `pip install apache-airflow`  
    `sudo apt install postgresql postgresql-contrib`  
    Далее устанавливаем psycopg2 и редактируем файл airflow.cfg  
    `sql_alchemy_conn = postgresql+psycopg2://airflow:air@localhost/airflow_metadata`  
    `load_examples = False`  
    Инициализируем базу даннных  
    `airflow db init`  

1. Запустить пример DAG'а из лекции на локальном компьютере и убедиться в успешном расчете пайплайна.

    * Скриншот из airflow web ui  
    ![sample text](img/hw_1/test_dag.PNG) 

1. Написать функцию mean_fare_per_class(), которая считывает файл titanic.csv и расчитывает среднюю арифметическую цену билета (Fare) для каждого класса (Pclass) и сохраняет результирующий датафрейм в файл titanic_mean_fares.csv

    * Код функции mean_fare_per_class():  
    ```
    def mean_fare_per_class():
        df = titanic_df.pivot_table(index=['Pclass'],
                                    values='Fare',
                                    aggfunc='mean') \
                        .reset_index() \
                        .rename(columns={'Fare': 'MeanFare'})
        df.to_csv(get_path('titanic_mean_fares.csv'))
    ```

1. Добавить в DAG таск с названием mean_fares_titanic_dataset, который будет исполнять функцию mean_fare_per_class(), причем эта задача должна запускаться в параллель с pivot_titanic_dataset после таски create_titanic_dataset.

    * Добавление нового таска в конец DAG'a  
    ```
    mean_fares_titanic_dataset = PythonOperator(
        task_id='mean_fares_dataset',
        python_callable=mean_fare_per_class,
        dag=dag,
    )
    ```

1. В конец пайплайна (после завершения тасок pivot_titanic_dataset и mean_fares_titanic_dataset) добавить шаг с названием last_task, на котором в STDOUT выводится строка, сообщающая об окончании расчета и выводящая execution date в формате YYYY-MM-DD. Пример строки: "Pipeline finished! Execution date is 2020-12-28"

    * Добавление last_task в конец DAG'a  
    ```
    last_task = BashOperator(
        task_id='last_task',
        bash_command='echo "Pipeline finished! Execution date is {{ ds }}"',
        dag=dag,
    )
    ```

    * Таким образом, финальный пайплайн будет выглядить следующим образом:  
    `first_task >> create_titanic_dataset >>  [pivot_titanic_dataset, mean_fares_titanic_dataset] >> last_task`  

    * [Ссылка на исходный код DAG'a](https://github.com/techhadera/dwh-reboot/blob/master/airflow/dags/dag_1.py)  

    * Скриншот графа  
    ![sample text](img/hw_1/graph.PNG)  

    * Вывод комманды в консоли "head ~/titanic_mean_fares.csv"  
    ![sample text](img/hw_1/head.PNG)  

    * Cодержание лога инстанса таски last_task в UI  
    [Ссылка на лог last_task](https://github.com/techhadera/dwh-reboot/blob/master/airflow/logs/hw_1/last_task.log)
