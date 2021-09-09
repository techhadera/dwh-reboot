 FROM ubuntu:latest
 MAINTAINER User GB
 RUN apt update
 RUN apt upgrade
 RUN apt install nginx -y
 RUN apt install php-fpm -y
 VOLUME "/var/www/html"
 EXPOSE 80
 CMD /usr/sbin/nginx -g "daemon off;"