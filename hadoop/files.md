# Практическое задание File Formats

Нужно загрузить в Hive (HDFS) достаточно большой датасет csv (100 МБ – 1 ГБ) и провести сравнительные эксперименты.
Что вам нужно сделать

1. Создать таблицы в форматах PARQUET или ORC c компрессией и без

    * Создание таблицы в формате PARQUET без компрессии. Введем `set parquet.compression=UNCOMPRESSED;` на случай если не сработает tblproperties  
      ```
      create table znu_names_parq.parq_state_names (
        Id string,
        Name string,
        Year_ string,
        Gender string,
        State string,
        Count_ string
      )
      STORED AS PARQUET
      tblproperties ('parquet.compression'='uncompressed');
      ```

    * Создание таблицы в формате PARQUET c компрессией. Введем `set parquet.compression=SNAPPY;` на случай если не сработает tblproperties  
      ```
      create table znu_names_parq.parq_state_names_comp (
        Id string,
        Name string,
        Year_ string,
        Gender string,
        State string,
        Count_ string
      )
      STORED AS PARQUET;
      tblproperties ('parquet.compression'='SNAPPY');
      ```

1. Перелить данные из таблицы csv в таблицу parquet/orc c компрессией и без

    * Загрузка таблицы без компрессии
      ```
      insert into table znu_names_parq.parq_state_names 
      select *
      from znu_names.state_names;
      ```

    * Загрузка таблицы c компрессией
      ```
      insert into table znu_names_parq.parq_state_names_comp
      select *
      from znu_names.state_names;
      ```

1. Посмотреть на получившийся размер данных
    * При помощи команды `hdfs dfs -du -h parq/*` можно посмотреть размеры файлов  
      ```
      72.2 M  216.6 M  parq/parq_state_names/000000_0
      36.1 M  108.3 M  parq/parq_state_names_comp/000000_0
      ```
      По размеру видно, что таблица `parq_state_names_comp` с компрессией.

    * Для потверждения того, что одна таблица имеет компрессию а вторая нет, можно выполнить `parquet-tools-1.9.0.jar meta` 
       
    * Выполним `hadoop jar /opt/parquet-tools-1.9.0.jar meta parq/parq_state_names/000000_0;`
    Результат:  
      ```
      2021-09-24 10:06:07,391 INFO hadoop.ParquetFileReader: Initiating action with parallelism: 5
      2021-09-24 10:06:07,393 INFO hadoop.ParquetFileReader: reading another 1 footers
      2021-09-24 10:06:07,394 INFO hadoop.ParquetFileReader: Initiating action with parallelism: 5
      file:        hdfs://dc1-21-07-05.ibs.org:8020/user/nzakharov/parq/parq_state_names/000000_0
      creator:     parquet-mr version 1.10.0 (build 031a6654009e3b82020012a18434c582bd74c73a)

      file schema: hive_schema
      --------------------------------------------------------------------------------
      id:          OPTIONAL BINARY O:UTF8 R:0 D:1
      name:        OPTIONAL BINARY O:UTF8 R:0 D:1
      year_:       OPTIONAL BINARY O:UTF8 R:0 D:1
      gender:      OPTIONAL BINARY O:UTF8 R:0 D:1
      state:       OPTIONAL BINARY O:UTF8 R:0 D:1
      count_:      OPTIONAL BINARY O:UTF8 R:0 D:1

      row group 1: RC:5647426 TS:75690283 OFFSET:4
      --------------------------------------------------------------------------------
      id:           BINARY UNCOMPRESSED DO:0 FPO:4 SZ:61013800/61013800/1.00 VC:5647426 ENC:BIT_PACKED,RLE,PLAIN
      name:         BINARY UNCOMPRESSED DO:0 FPO:61013804 SZ:10822725/10822725/1.00 VC:5647426 ENC:PLAIN_DICTIONARY,BIT_PACKED,RLE
      year_:        BINARY UNCOMPRESSED DO:0 FPO:71836529 SZ:35002/35002/1.00 VC:5647426 ENC:PLAIN_DICTIONARY,BIT_PACKED,RLE
      gender:       BINARY UNCOMPRESSED DO:0 FPO:71871531 SZ:1556/1556/1.00 VC:5647426 ENC:PLAIN_DICTIONARY,BIT_PACKED,RLE
      state:        BINARY UNCOMPRESSED DO:0 FPO:71873087 SZ:1996/1996/1.00 VC:5647426 ENC:PLAIN_DICTIONARY,BIT_PACKED,RLE
      count_:       BINARY UNCOMPRESSED DO:0 FPO:71875083 SZ:3815204/3815204/1.00 VC:5647426 ENC:PLAIN_DICTIONARY,BIT_PACKED,RLE
      ```

    * Выполним `hadoop jar /opt/parquet-tools-1.9.0.jar meta parq/parq_state_names_comp/000000_0;`
    Результат:
      ```
      2021-09-24 09:55:31,308 INFO hadoop.ParquetFileReader: Initiating action with parallelism: 5
      2021-09-24 09:55:31,310 INFO hadoop.ParquetFileReader: reading another 1 footers
      2021-09-24 09:55:31,310 INFO hadoop.ParquetFileReader: Initiating action with parallelism: 5
      file:        hdfs://dc1-21-07-05.ibs.org:8020/user/nzakharov/parq/parq_state_names_comp/000000_0
      creator:     parquet-mr version 1.10.0 (build 031a6654009e3b82020012a18434c582bd74c73a)

      file schema: hive_schema
      --------------------------------------------------------------------------------
      id:          OPTIONAL BINARY O:UTF8 R:0 D:1
      name:        OPTIONAL BINARY O:UTF8 R:0 D:1
      year_:       OPTIONAL BINARY O:UTF8 R:0 D:1
      gender:      OPTIONAL BINARY O:UTF8 R:0 D:1
      state:       OPTIONAL BINARY O:UTF8 R:0 D:1
      count_:      OPTIONAL BINARY O:UTF8 R:0 D:1

      row group 1: RC:5647426 TS:75690225 OFFSET:4
      --------------------------------------------------------------------------------
      id:           BINARY SNAPPY DO:0 FPO:4 SZ:24563346/61013742/2.48 VC:5647426 ENC:BIT_PACKED,PLAIN,RLE
      name:         BINARY SNAPPY DO:0 FPO:24563350 SZ:10717660/10822725/1.01 VC:5647426 ENC:BIT_PACKED,PLAIN_DICTIONARY,RLE
      year_:        BINARY SNAPPY DO:0 FPO:35281010 SZ:34833/35002/1.00 VC:5647426 ENC:BIT_PACKED,PLAIN_DICTIONARY,RLE
      gender:       BINARY SNAPPY DO:0 FPO:35315843 SZ:1612/1556/0.97 VC:5647426 ENC:BIT_PACKED,PLAIN_DICTIONARY,RLE
      state:        BINARY SNAPPY DO:0 FPO:35317455 SZ:1974/1996/1.01 VC:5647426 ENC:BIT_PACKED,PLAIN_DICTIONARY,RLE
      count_:       BINARY SNAPPY DO:0 FPO:35319429 SZ:2521835/3815204/1.51 VC:5647426 ENC:BIT_PACKED,PLAIN_DICTIONARY,RLE
      ```  
1. Посчитать count некоторых колонок в разных форматах хранения

    * Подсчитаем количество новорожденных с женскими именами в таблице с форматом хранения parquet с компрессией
      ```
      select count(*) females_count
      from znu_names_parq.parq_state_names_comp
      where gender = 'F';
      ```
      Результат:
      ```
      females_count
      3154009
      Time taken: 8.996 seconds, Fetched: 1 row(s)
      ```

    * Создание таблицы с форматом avro и вставка данных  
      ```
      create table znu_names_avro.avro_state_names_comp (
        Id string,
        Name string,
        Year_ string,
        Gender string,
        State string,
        Count_ string
      )
      stored as avro
      tblproperties ("avro.output.codec"="snappy");
      ```
      ```
      insert into table znu_names_avro.avro_state_names_comp
      select * from znu_names.state_names;
      ```
      Проверка существования файла командой `hdfs dfs -du -h avro/*`
      Результат:
      ```
      179.9 M  539.7 M  avro/avro_state_names_comp/000000_0
      ```

    * Подсчитаем количество новорожденных с женскими именами в таблице с форматом хранения avro с компрессией
      ```
      select count(*) females_count
      from znu_names_avro.avro_state_names_comp
      where gender = 'F';
      ```
      Результат:
      ```
      females_count
      3154009
      Time taken: 9.216 seconds, Fetched: 1 row(s)
      ```

1. Посчитать агрегаты по одной и нескольким колонкам в разных форматах

    * Подсчитаем количество новорожденных с именами за все года в таблице в формате parquet с компрессией (агрегат по одной колонке)  
      ```
      select name, sum(count_) total_count
      from znu_names_parq.parq_state_names_comp
      group by name
      order by sum(count_) desc
      limit 10;
      ```
      Результат:
      [Ссылка на html отчет](https://techhadera.github.io/dwh-reboot/hadoop/urls/parq.html)  
      ```
      name    total_count
      James   4957166.0
      John    4845414.0
      Robert  4725713.0
      Michael 4312975.0
      William 3839236.0
      Mary    3740495.0
      David   3562278.0
      Richard 2534949.0
      Joseph  2485220.0
      Charles 2252146.0
      Time taken: 792.325 seconds, Fetched: 10 row(s)
      ```

      * Подсчитаем количество новорожденных с именами за все года и минимальное количество детей с данным именем за все время в таблице в формате parquet с компрессией (агрегат по двум колонкам)  
      ```
      select name, sum(count_) total_count, min(count_) min_count
      from znu_names_parq.parq_state_names_comp
      group by name
      limit 10;
      ```
      Результат:  
      [Ссылка на html отчет](https://techhadera.github.io/dwh-reboot/hadoop/urls/parq_2.html)  
      ```
      name    total_count min_count
      Aaban	  12.0	      6
      Aadan	  23.0	      5
      Aadarsh	5.0	        5
      Aaden	  3426.0	    10
      Aadhav	6.0	        6
      Aadhya	453.0	      11
      Aadi	  313.0	      10
      Aadil	  5.0	        5
      Aadin	  5.0	        5
      Aadit	  18.0	      5
      ```
    * Подсчитаем количество новорожденных с именами за все года в таблице в формате avro с компрессией (агрегат по одной колонке)  
      ```
      select name, sum(count_) total_count
      from znu_names_avro.avro_state_names_comp
      group by name
      order by sum(count_) desc
      limit 10;
      ```
      Результат:
      [Ссылка на html отчет](https://techhadera.github.io/dwh-reboot/hadoop/urls/avro.html) 
      ```
      name    total_count
      James   4957166.0
      John    4845414.0
      Robert  4725713.0
      Michael 4312975.0
      William 3839236.0
      Mary    3740495.0
      David   3562278.0
      Richard 2534949.0
      Joseph  2485220.0
      Charles 2252146.0
      Time taken: 503.09 seconds, Fetched: 10 row(s)
      ```
    * Подсчитаем количество новорожденных с именами за все года и минимальное количество детей с данным именем за все время в таблице в формате avro с компрессией (агрегат по двум колонкам)  
      ```
      select name, sum(count_) total_count, min(count_) min_count
      from znu_names_avro.avro_state_names_comp
      group by name
      limit 10;
      ```
      Результат:  
      [Ссылка на html отчет](https://techhadera.github.io/dwh-reboot/hadoop/urls/avro_2.html)  
      ```
      name    total_count min_count
      Aaban	  12.0	      6
      Aadan	  23.0	      5
      Aadarsh	5.0	        5
      Aaden	  3426.0	    10
      Aadhav	6.0	        6
      Aadhya	453.0	      11
      Aadi	  313.0	      10
      Aadil	  5.0	        5
      Aadin	  5.0	        5
      Aadit	  18.0	      5
      ```
1. Сделать выводы о эффективности хранения и компрессии.

    * Колоночный формат  
    Колоночные форматы данных, такие как ORC или Parquet хорошо подходят для операции чтения и запросов данных, чем для записи. Ну и поскольку это колоночный формат, данный формат идеален для запросов подмножества столбцов в многоколоночной таблице. Но с таким форматом существует необходимость быть внимательным к схеме, поскольку эволюция(добавление изменение столбцов) схем невозможна. Также в колоночных форматах присутствует схема данных, в которой можно посмотреть типы колонок и их типы данных. Эффективное хранение данных позволяет сжимать данные, для того чтобы данные занимали меньше места.

    * Строчный формат  
    Строчные форматы, такие как Avro более эффективны в плане записи и эволюции схемы. Данный формат хорошо подходит для ETL операций, в которых запрашиваются все столбцы

    * Компрессия при помощи gzip  
    Компрессия при помощи gzip использует много CPU ресурсов чем snappy, но за счет этого позволяет добиться более сильного сжатия. Данный способ лучше применять к данным, к которым доступ нужен не так часто.

    * Компрессия при помощи snappy  
    Компрессия при помощи snappy использует среднее количество CPU ресурсов чем gzip, но и сжимает данные не так сильно. Данный способ лучше применять к данным, к которым доступ довольно часто.

    * Выводы по практике  
    Запросы с агрегирующими функциями выполняются быстрее в таблицах с колоночным форматом(потому что они работают по колонкам, а доступ к колонкам очень быстрый). В практической работе над своим датасетом, я наблюдал что elapsed time в среднем чуть больше при работе с таблицами в строчном формате. Очевидно, что обращение к таблицам имеющим сжатие, занимает больше времени чем к таблицам которые его не имеют, но поскольку датасет не такой большой, разницу заметить не получилось. 