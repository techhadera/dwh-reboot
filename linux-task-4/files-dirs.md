# Практическое задание по теме Управление правами на файлы и каталоги

1. Создать файл file1 и наполнить его произвольным содержимым. Скопировать его в file2. Создать символическую ссылку file3 на file1. Создать жёсткую ссылку file4 на file1. Посмотреть, какие inode у файлов. Удалить file1. Что стало с остальными созданными файлами? Попробовать вывести их на экран.

    * Создание жесткой и символической ссылки на файл file1  
    ![sample text](img/full2.PNG)

    * Удаление file1. В данном случае перестанет работать символическая ссылка file3. Данные также можно получить по жесткой ссылке  
    ![sample text](img/del-file1.PNG)

1. Дать созданным файлам другие, произвольные имена. Создать новую символическую ссылку. Переместить ссылки в другую директорию.

    * Переименование файлов  
    ![sample text](img/rename-files.PNG)

    * Создание новой символической ссылки extra_link на файл new_file2  
    ![sample text](img/extra-link.PNG)

    * Перемещение всех ссылок в папку linkhouse. Ссылка extra_link перестала работать  
    ![sample text](img/link-house.PNG)

1. Создать два произвольных файла. Первому присвоить права на чтение и запись для владельца и группы, только на чтение — для всех. Второму присвоить права на чтение и запись только для владельца. Сделать это в численном и символьном виде.

    * Создание файлов file1 и file2. Присвоение файлу file1 права на чтение и запись для владельца и группы, а на чтение для всех. (символный вид)  
    ![sample text](img/make-files-per-file1-chmod-s.PNG)  
    В численном виде будет:  
    `chmod 774 file1 `

    * Выставление прав на file2  
    В численном: `chmod 744 file2`  
    В символьном: `chmod -R u=rw-, g=r--, o=r-- file2`

1. Создать группу developer и нескольких пользователей, входящих в неё. Создать директорию для совместной работы. Сделать так, чтобы созданные одними пользователями файлы могли изменять другие пользователи этой группы.

    * Создадим общую папку, установим необходимые права (rwx для группы developer и SGID для разрешения пользователям запускать исполняемые файлы от имени владельца (или группы) запускаемого файла), группу и пользователей входящих в нее.  
    `user@gb-test:/home$ sudo mkdir dev_project`  
    `user@gb-test:/home$ sudo chmod 2774 dev_project`  
    `user@gb-test:/home$ sudo useradd -s /bin/bash -d /home/dev_1 -m dev_1`  
    `user@gb-test:/home$ sudo useradd -s /bin/bash -d /home/dev_2 -m dev_2`  
    `user@gb-test:/home$ sudo usermod -aG developer dev_1`  
    `user@gb-test:/home$ sudo usermod -aG developer dev_2`  

    * Сменим группу общей папки  
    `user@gb-test:/home$ sudo chgrp developer -R dev_project`  
    
    * Заходим из под пользователя dev_1 и создаем файл в общей папке  
    `user@gb-test:/home$ sudo su dev_1`  
    `dev_1@gb-test:/home/dev_project$ echo 'note by dev_1' > notes.txt`  
    `dev_1@gb-test:/home/dev_project$ cat notex.txt`  
    `note by dev_1`  

    * Заходим из под пользователя dev_2 и пробуем изменить содержимое файла notes.txt, который создал пользователь dev_1  
    `user@gb-test:/home$ sudo su dev_2`  
    `dev_2@gb-test:/home/dev_project$ echo 'note by dev_2' >> notes.txt`  
    `dev_2@gb-test:/home/dev_project$ cat notes.txt`  
    `note by dev_1`  
    `note by dev_2`  

    * Результат работы команды `ls -hla`  
    `dev_2@gb-test:/home/dev_project$ ls -hla`  
    `total 12K`  
    `drwxrwsr-- 2 root  developer 4.0K Sep 11 17:12 .`  
    `drwxr-xr-x 6 root  root      4.0K Sep 11 17:08 ..`  
    `-rw-rw-r-- 1 dev_1 developer   28 Sep 11 17:14 notes.txt`  

1. Создать в директории для совместной работы поддиректорию для обмена файлами, но чтобы удалять файлы могли только их создатели.

    * Создадим поддиректорию `shared_files` для обмена файлами. Установим доступ 1774 (rwx для группы и владельца, а также sticky bit, для того чтобы файлы могли удалять только  их создатели)  
    `dev_1@gb-test:/home/dev_project$ mkdir shared_files`  
    `dev_1@gb-test:/home/dev_project$ chmod 1774 shared_files`  
    
    * Создадим файл dev1_file пользователем dev_1  
    `dev_1@gb-test:/home/dev_project/shared_files$ touch dev1_file`  

    * Зайдем через пользователя dev_2, создадим файл dev2_file и поменяем содержание файла dev1_file  
    `dev_2@gb-test:/home/dev_project/shared_files$ touch dev2_file`  
    `dev_2@gb-test:/home/dev_project/shared_files$ echo 'changes' >> dev1_file`  
    `dev_2@gb-test:/home/dev_project/shared_files$ cat dev1_file`  
    Вывод:  
    `changes`  

    * Попробуем удалить файл dev1_file юзером dev1_file  
    `dev_2@gb-test:/home/dev_project/shared_files$ rm dev1_file`  
    Получаем ошибку  
    `rm: cannot remove 'dev1_file': Operation not permitted`
