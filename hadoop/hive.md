# Практическое задание Hive

1. Скачать любой датасет с сайта Kaggle.com (10 МБ+) (не больше 1ГБ)

    * В качестве датасета используются метаданные о топ 5000 фильмах TMDd  
    `https://www.kaggle.com/tmdb/tmdb-movie-metadata`
    В датасете имеется две таблицы. В tmdb_5000_movies.csv данные о фильмах, в tmdb_5000_credits.csv состав исполнителей
1. Загрузить этот датасет в HDFS в свою домашнюю папку
1. Создать собственную базу данных в HIVE

    * Создание базы данных  
    `create database znu_tmdb;`

1. Создать таблицы внутри базы данных с использованием всех загруженных файлов. Один файл – одна таблица.

    * Создание таблицы credits  
      ```
      create table znu_tmdb.credits(
      movie_id string,
      title string,
      cast_ string,
      crew string)
      ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
      STORED AS TEXTFILE
      location '/ZakharovFolder/hive/credits';
      ```

    * Создание таблицы movies
      ```
      create table znu_tmdb.movies (
        budget string,
        genres string,
        homepage string,
        id string,
        keywords string,
        original_language string,
        original_title string,
        overview string,
        popularity string,
        production_companies string,
        production_countries string,
        release_date string,
        revenue string,
        runtime string,
        spoken_languages string,
        status string,
        tagline string,
        title string,
        vote_average string,
        vote_count string
      )
      ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
      STORED AS TEXTFILE
      location '/ZakharovFolder/hive/movies';
      ```

1. Сделать любой отчет по загруженным данным используя групповые и агрегатные функции.
1. Сделать любой отчет по загруженным данным используя JOIN.