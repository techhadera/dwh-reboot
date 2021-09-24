# Практическое задание Hive

1. Скачать любой датасет с сайта Kaggle.com (10 МБ+) (не больше 1ГБ)

    * В качестве датасета используются данные о именах новорожденных в Америке по годам, на национальном уровне и на уровне штатов  
    `https://www.kaggle.com/kaggle/us-baby-names`
    В датасете имеется две таблицы. В таблице state_names.csv статистика по именам по штатам, в national_names.csv по именам на национальном уровне
1. Загрузить этот датасет в HDFS в свою домашнюю папку

    * Для того чтобы загрузить датасеты, нужно перебросить их на datanode по адресу 172.22.130.160. Это можно сделать через WinSCP  
      ![WinSCP](img/WinSCP.PNG)

1. Создать собственную базу данных в HIVE

    * Создание базы данных  
      ```
      create database znu_names
      location "/nzakharov/hive";
      ```

1. Создать таблицы внутри базы данных с использованием всех загруженных файлов. Один файл – одна таблица.

    * Создание таблицы national_names  
      ```
      create table znu_names.national_names (
        Id string,
        Name string,
        Year_ string,
        Gender string,
        Count_ string
      )
      ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
      STORED AS TEXTFILE
      location "/nzakharov/hive/national_names"
      tblproperties ("skip.header.line.count"="1");
      ```

    * Создание таблицы state_names  
      ```
      create table znu_names.state_names (
        Id int,
        Name string,
        Year_ int,
        Gender string,
        State string,
        Count_ int
      )
      ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
      STORED AS TEXTFILE
      location "nzakharov/hive/state_names"
      tblproperties ("skip.header.line.count"="1")
      ```

    * В том случае, если данные из csv не подгрузились, необходимо загрузить их через hive  
      ```
      LOAD DATA LOCAL INPATH '/home/nzakharov/state_names.csv' OVERWRITE INTO TABLE znu_names.state_names;
      ```
      ```
      LOAD DATA LOCAL INPATH '/home/nzakharov/national_names.csv' OVERWRITE INTO TABLE znu_names.movies;
      ```

1. Сделать любой отчет по загруженным данным используя групповые и агрегатные функции.

    * Выполним подсчет количества женских и мужских имен в таблице state_names  
    [Ссылка на файл](src/1.sql)  
      ```
      select count(*) total_count, gender
      from znu_names.state_names
      group by gender;
      ```
      Вывод(на момент выполнения практики, к hive было невозможно подключиться через DBeaver для формирования отчета в формате .html. Если доступ появится, отчет будет обновлен):  
      ```
      total_count     gender
      1081683         F
      743750          M
      Time taken: 5.08 seconds, Fetched: 2 row(s)
      ```

1. Сделать любой отчет по загруженным данным используя JOIN.

    * Выполним join двух таблиц state_names и national_names по составному ключу `(name, year_)`. Выведем информацию об именах и количестве имен новорожденных по годам. Сортируем выборку по году, и выводим последние 10 записей.  
    [Ссылка на файл](src/2.sql)  
      ```
      select nn.name, nn.year_, sn.count_
      from znu_names.national_names nn
      join znu_names.state_names sn
      on (sn.name = nn.name and sn.year_ = nn.year_)
      order by nn.year_ desc
      limit 10;
      ```
    * Вывод(на момент выполнения практики, к hive было невозможно подключиться через DBeaver для формирования отчета в формате .html. Если доступ появится, отчет будет обновлен):
      ```
      nn.name nn.year_        sn.count_
      Aaditya 2014            7
      Zuri    2014            28
      Aadya   2014            5
      Aadya   2014            5
      Aadya   2014            6
      Aadya   2014            11
      Aadya   2014            16
      Zuri    2014            7
      Aadya   2014            23
      Aadya   2014            7
      Time taken: 22.077 seconds, Fetched: 10 row(s)
      ```