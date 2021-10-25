# Практическое задание по Pentaho

1. Развернуть на рабочем компьютере БД Postgre SQL .Развернуть Pentaho Data Integration. В БД создать две таблицы (курсы валют и разница курсов валют по дням), создать тестовые данные для загрузки в (данные взять с сайта ЦБ).

    * После установки Postgre и Pentaho, создадим базу данных currencies_db.  
    `CREATE DATABASE currencies_db;`  

    * Перед тем как создавать таблицу для хранения курсов валют, необходимо просмотреть структуру данных, который возвращает сайт ЦБ.  
    ![sample text](img/cber.PNG)  

    * Создадим таблицу currencies, которая будет хранить актуальные данные курсов валют.
    ```
    create table currencies (
        entry_id BIGSERIAL NOT NULL PRIMARY KEY,
        valute_id VARCHAR(10) NOT NULL,
        num_code VARCHAR(5) NOT NULL,
        char_code VARCHAR(8) NOT NULL,
        nominal SMALLSERIAL NOT NULL,
        name VARCHAR(40) NOT NULL,
        value NUMERIC NOT NULL,
        gather_date DATE NOT NULL
    )
    ```  
    Стоит пояснить, что колонка gather_date представляет собой дату сбора курса валют, он парсится из полученного файла.  

    Сгенерированные сиквенсы для столбцов num_code и nominal можно удалить, а default значение убрать.  
    `ALTER TABLE currencies ALTER COLUMN num_code DROP DEFAULT;`  
    `ALTER TABLE currencies ALTER COLUMN nominal DROP DEFAULT;`  

    * Создадим таблицу currencies_diff, в ней будут хранится исторические данные о смене курсов валют, в колонке difference будет указана разница между датой сбора данных (date_to) и последней актуальной даты сбора в таблице currencies (date_from).  
    ```
    create table currencies_diff (
        entry_id BIGSERIAL NOT NULL PRIMARY KEY,
        valute_id VARCHAR(10) NOT NULL PRIMARY KEY,
        num_code VARCHAR(5) NOT NULL,
        char_code VARCHAR(8) NOT NULL,
        nominal SMALLSERIAL NOT NULL,
        name VARCHAR(40) NOT NULL,
        difference NUMERIC NOT NULL,
        date_from DATE NOT NULL,
        date_to DATE NOT NULL
    )
    ```

    Удаляем значение по умолчанию для nominal  
    `ALTER TABLE currencies_diff ALTER COLUMN nominal DROP DEFAULT;`  

    * Для загрузки тестовых (инициализирующих) данных, можно создать временный пайплайн  
    ![sample text](img/init_p.PNG)

    * В шаге Input url создает строка с ссылкой для получения xml данных с сайта ЦБ.  
    ![sample text](img/input.PNG)  

    * В шаге Get today currency data выполняется http GET запрос по ссылке. Полученне данные сохраняются в колонку currency_data.  
    ![sample text](img/get.PNG)  

    * На этапе Get data from XML происходит парсинг XML строки. Учитывая структуру данных, необходимо определить корневой элемент, для осуществления перебора элементов, хранящих информацию о данных курса валют.  
    ![sample text](img/path.PNG)  

    В этом же шаге, мы определяем путь до атрибутов и полей данных в формате XPath, также указываем тип и формат данных.  
    ![sample text](img/fields.PNG)  

    * Колонка данных value (обозначает курс валюты) имеет запятую в качестве разделителя между целой и дробной частью. Для избежания проблем, лучше поменять разделитель на точку - шаг Format currency values.  
    ![sample text](img/str.PNG)

    * В шаге Select columns происходит отбор колонок, с которыми будет проходить дальнейшая работа.  
    ![sample text](img/select1.PNG)  

    * На этапе Initial insert into currencies table, происходит инициализация таблицы currencies тестовыми данными.  
    ![sample text](img/insert1.PNG)  

    Предварительно перед вставкой данных, необходимо настроить подключение к БД.  
    ![sample text](img/connect.PNG)  


2. Разработать функционал загрузки тестовых данных в БД c ведением истории в формате CSD1 (срезами/снимками). Создать пакет, содержащий процедуру расчета разницы курсов на основе загруженных данных и ее сохранения во второй таблице). Настроить планировщики Pentaho Data Integration, чтобы ежедневно загружали данные в БД и рассчитывали разницу (ежедневно).

    * При добавлени всех необходимых шагов, итоговый пайплайн будет выглядеть следующим образом:  
    ![sample text](img/pipeline.PNG)  

    Как видно на скриншоте, инициализация тестовыми данными отключена, и поток данных уже направлен на процесс добавления историчный данных в таблицу currencies_diff и обновление данных в таблице currencies.

    * На новом шаге Join old and new currencies tables происходит объединение новой и старой таблицы с курсами валют по ключу valute_id.  

    Данный код:
    ```
        select value as value_old, gather_date as gather_date_old
        from currencies
        where valute_id = ?;
    ```
    Добавляет к только что полученной таблице с курсами валют предыдущие данные из таблицы currencies. В данном примере под знак вопроса подставляется параметр valute_id из новой таблицы. И в итоге формируется следующая таблица:  
    ![sample text](img/table_join.PNG)  

    * На этапе Calculate rates difference происходит создание новой таблицы, означающей разницу нового и старого курса валют.  
    ![sample text](img/calc.PNG)  

    * В шаге Select columns for insert/update происходит выборка и переимнование некоторых колонок для вставки в таблицу currencies_diff и позже обновление данных в таблице currencies.  
    ![sample text](img/select2.PNG)  

    * Поскольку таблица currencies существует в формате CSD1, должны обновляться только данные о курсах валют и дата загрузки данных.  
    ![sample text](img/update.PNG)

    * Таблица currencies_diff должна иметь историчность изменений.  
    ![sample text](img/insert2.PNG)

    * Для того чтобы эта трансформация запускалась каждый день, необходимо создать джобу, выбрать блок Start и выбрать период.  
    ![sample text](img/start.PNG)  

    Далее нужно добавить блок трансформации и выбрать созданный ранее файл test.ktr.  
    ![sample text](img/job.PNG)  

    Сохраняем джобу и запускаем.  
    ![sample text](img/save_job.PNG)  

    Во вкладке job metrics можно смотреть логи работы задачи.  
    ![sample text](img/metric.PNG)  

    Таким образом, если произойдут запросы с 2021-10-19 по 2021-10-23. Таблица currencies будет выглядеть следующим образом:  
    ![sample text](img/curr.PNG)  
    
    А таблица currencies_diff:  
    ![sample text](img/curr_diff.PNG)  


    Все преобразования таблиц и работа с базой данных осуществляется через Pentaho, для упрощения менеджмента пайплайна.


1. Развернуть Apache Superset два dashboard-а

    * После установки Apache Superset и дополнительных модулей для работы с PostgresSQL, запуска сервера, можно увидеть приветственное окно web ui.  
    ![sample text](img/welcome.PNG)  

    * Создадим подключение к базе данных Postgre.  
    ![sample text](img/superset_db.PNG)  

    * Импортируем датасеты (таблицы), исключим колонку entry_id.  
    ![sample text](img/superset_df_all.PNG)  

    * Создадим дашборд Currency charts admin, на нем поместим две таблицы, currency table просто отображает таблицу currency_diff, а total growth показывает суммарный рост курса валют за весь промежуток времени.  
    ![sample text](img/admin.PNG)  

    * Создадим Currency charts user, на нем отобразим круговую диаграмму, на котором демонстрируется процент роста валют. А на графике Line chart отобразим движение разницы курса валют по дням.
    ![sample text](img/user.PNG)  


1. Ограничения и допущения

    * Первое допущение - каждый день запрос курса валют не будет завершаться с ошибкой, и если запрос завершится с ошибкой, то данные за текущий день будут пропущены. Решить это проблему можно при помощи добавления проверки доступности ресурса, и в том случае если за текущий день выполнить задачу не удалось, она выполнится в следующий раз.

    * Второе допущение - каждый день в 12 часов дня новые курсы валют будут доступны на сайте. Но на выходных ЦБ не выставляет новые курсы валют, поэтому будет генерироваться бессмысленные записи два раза в неделю. Но существует несложный способ удалить такие записи если date_from = date_to. Либо можно добавить проверку на актуальность даты.  
