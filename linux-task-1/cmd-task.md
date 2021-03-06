# Практическое задание по теме Навыки работы в командной строке Linux.

1. Навигация по файловой системе. Попрактиковаться в перемещении между каталогами, используя полный и относительный путь. Перечислить, какие параметры команды cd позволят быстро вернуться в домашний каталог, позволят перейти на уровень выше.

    * Переход, используя относительный путь  
    ![sample text](img/cd-1.PNG)
    
    * Переход, используя абсолютный путь  
    ![sample text](img/cd-2.PNG)
    
    * Переход через домашний каталог  
    ![sample text](img/cd-3.PNG)
    
    * Для быстрого перехода в домашний каталог, можно использовать: `cd ~`
    
    * Для быстрого перехода на уровень выше, можно использовать: `cd ..`

1. Управление файлами и каталогами и текстовые редакторы. Создать файл с наполнением, используя несколько способов. Использовать разобранные текстовые редакторы для наполнения файлов данными. Создать копии созданных файлов, создать несколько каталогов с подкаталогами, перенести несколько файлов в созданные каталоги. Перечислить команды и используемые параметры команд.

    * Создание и заполнение файла через `echo`  
    ![sample text](img/echo.PNG)
      
    * Наполнение файла при помощи Vim  
    ![sample text](img/vim1.PNG)  
    ![sample text](img/vim2.PNG)
      
    * Наполнение файла при помощи nano  
    ![sample text](img/nano1.PNG)  
    ![sample text](img/nano2.PNG)
      
    * Создание копий созданных текстовых файлов
    ![sample text](img/cp-1.PNG)
      
    * Создание нескольких каталогов с подкаталогами и перенос файлов  
    ![sample text](img/mkdir-mv-1.PNG)
      
    * Команды, и используемые параметры  
    
      * Копирование `cp file_1 file_2`, параметр `r` - для рекурсивного копирования каталога
      * Перенос `mv file_1 file_2`
      * Создание каталогов `mkdir folder_name` параметр `p` - для создания вложенных подкаталогов

1. Используя дополнительный материал, настроить авторизацию по SSH с использованием ключей.
    * Первый шаг, это генерирование ssh ключа на сервере  
    ![sample text](img/ssh-1.PNG)

    * После генерации, ключ выглядит следующим образом. Хорошей практикой считается добавление ключа в authorized_keys  
    ![sample text](img/ssh-2.PNG)

    * Далее, при помощи утилиты pscp копируем приватный ключ с сервера  
    ![sample text](img/ssh-3.PNG)

    * Вставляем его в PuTTY key Generator и сохраняем приватный ключ  
    ![sample text](img/ssh-4.PNG)

    * Указываем данный ключ во вкладке ssh -> auth   
    ![sample text](img/ssh-5.PNG)

    * Подключаемся к серверу. На второй строке видно, что при подключении использовался ключ а не пароль.  
    ![sample text](img/ssh-6.PNG)