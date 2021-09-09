# Практическое задание по теме Docker

1. Запустить контейнер с Ubuntu.

    * После выполнения примеров из видео, образ ubuntu уже находится в списке образов docker. Поэтому его можно сразу запустить при помощи команды
    `docker run -t -i --rm ubuntu bash`
    Результат работы команды `ls -li` внутри контейнера
      ```
      total 48
      4947 lrwxrwxrwx   1 root root    7 Aug 27 07:16 bin -> usr/bin
      802481 drwxr-xr-x  2 root root 4096 Apr 15  2020 boot
      2 drwxr-xr-x   5 root root  360 Sep  9 06:46 dev
      544811 drwxr-xr-x   1 root root 4096 Sep  9 06:46 etc
      8467 drwxr-xr-x   2 root root 4096 Apr 15  2020 home
      5062 lrwxrwxrwx   1 root root    7 Aug 27 07:16 lib -> usr/lib
      5063 lrwxrwxrwx   1 root root    9 Aug 27 07:16 lib32 -> usr/lib32
      5064 lrwxrwxrwx   1 root root    9 Aug 27 07:16 lib64 -> usr/lib64
      5065 lrwxrwxrwx   1 root root   10 Aug 27 07:16 libx32 -> usr/libx32
      8468 drwxr-xr-x   2 root root 4096 Aug 27 07:16 media
      8469 drwxr-xr-x   2 root root 4096 Aug 27 07:16 mnt
      8470 drwxr-xr-x   2 root root 4096 Aug 27 07:16 opt
      1 dr-xr-xr-x 179 root root    0 Sep  9 06:46 proc
      8472 drwx------   2 root root 4096 Aug 27 07:27 root
      8473 drwxr-xr-x   5 root root 4096 Aug 27 07:27 run
      5070 lrwxrwxrwx   1 root root    8 Aug 27 07:16 sbin -> usr/sbin
      8477 drwxr-xr-x   2 root root 4096 Aug 27 07:16 srv
      1 dr-xr-xr-x  13 root root    0 Sep  9 06:46 sys
      8479 drwxrwxrwt   2 root root 4096 Aug 27 07:27 tmp
      8480 drwxr-xr-x  13 root root 4096 Aug 27 07:16 usr
      8753 drwxr-xr-x  11 root root 4096 Aug 27 07:27 var
      ```

1. Используя Dockerfile, собрать связку nginx + PHP-FPM в одном контейнере.

    * Содержание Dockerfile
      Ссылка на файл: [Dockerfile](https://github.com/techhadera/dwh-reboot/blob/master/docker/src/Dockerfile)
      ```    
      FROM ubuntu:latest
      MAINTAINER User GB
      RUN apt update
      RUN apt upgrade
      RUN apt install nginx -y
      RUN apt install php-fpm -y
      VOLUME "/var/www/html"
      EXPOSE 80
      CMD /usr/sbin/nginx -g "daemon off;"
      ```
    * Сборка Dockerfile  
    `docker build -t nginx_phpfpm .`
    Результат сборки:
      ```
      Successfully built cbffd4aeba21
      Successfully tagged nginx_phpfpm:latest
      ```

    