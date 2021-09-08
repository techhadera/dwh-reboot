# Практическое задние по теме bash.

1. Написать скрипт, который удаляет из текстового файла пустые строки и заменяет маленькие символы на большие. Воспользуйтесь tr или SED.

    * Удаление пустых строк и перевод символов в uppercase при помощи SED  
      `sed -i '/./!d' text-with-empty-lines.txt` 
      `sed -i -e 's/\(.*\)/\U\1/' text-with-empty-lines.txt`

    * Удаление пустых строк и перевод символов в uppercase при помощи tr  
      `cat text-with-spaces.txt | tr -s '\n' | tr [:lower:] [:upper:] > text-with-spaces.txt.txt`

1. Создать скрипт, который создаст директории для нескольких годов (2010–2017), в них — поддиректории для месяцев (от 01 до 12), и в каждый из них запишет несколько файлов с произвольными записями. Например, 001.txt, содержащий текст «Файл 001», 002.txt с текстом «Файл 002» и т. д.

    * Код скрипта с комментариями  
      Ссылка на скрипт: [subtask_1.sh](https://github.com/techhadera/dwh-reboot/blob/master/bash-programming/src/subtask_1.sh)
      ```
      for i in {2010..2017}
      do
        # Создаем каталог с годом в интервале 2010-2017 и заходим в него
        mkdir $i
        cd $i
        for j in 01 02 03 04 05 06 07 08 09 {10..12}
        do
          # Создаем подкаталог с месяцем от 0-12, заходим в него
          mkdir $j
          cd $j
          for k in 001 002 003
          do
            # Внутри каждого подкаталога создаем три файла с некоторым содержимым
            echo "File $k" > $k.txt
          done
          # В конце цикла выходим из подкаталога с месяцем
          cd ..
        done
        # В конце цикла выходим из каталога с годом
        cd ..
      done
      ```

1. Использовать команду AWK на вывод длинного списка каталога, чтобы отобразить только права доступа к файлам. Затем отправить в конвейере этот вывод на sort и uniq, чтобы отфильтровать все повторяющиеся строки.

    * `ls /etc -l | awk '{ print $1 }' | uniq | sort`
    * Результат работы:  
      ```
      user@gb-test:~/bash-practise$ ls /etc -l |  awk '{ print $1 }' | sort | uniq
      drwx------
      drwxr-s---
      drwxrwxr-x
      drwxr-xr-x
      lrwxrwxrwx
      -r--r-----
      -r--r--r--
      -rw-r-----
      -rw-r--r--
      ```

1. Используя grep, проанализировать файл /var/log/syslog, отобрав события на своё усмотрение.

    * Отбираем все логи службы systemd за сентябрь
    `cat /var/log/syslog | grep -E 'Sep.*systemd.*'`
    * Пример вывода 10 последних записей
      ```
        syslog | grep -E 'Sep.*systemd.*' | tail
        Sep  6 11:06:46 gb-test kernel: [    4.058067] systemd[1]: Finished Uncomplicated firewall.
        Sep  6 11:06:46 gb-test kernel: [    4.067110] systemd[1]: Finished Remount Root and Kernel File Systems.
        Sep  6 11:06:46 gb-test kernel: [    4.069674] systemd[1]: Activating swap /swap.img...
        Sep  6 11:06:46 gb-test kernel: [    4.074746] systemd[1]: Condition check resulted in Rebuild Hardware Database being skipped.
        Sep  6 11:06:46 gb-test kernel: [    4.075494] systemd[1]: Condition check resulted in Platform Persistent Storage Archival being skipped.
        Sep  6 11:06:46 gb-test kernel: [    4.078021] systemd[1]: Starting Load/Save Random Seed...
        Sep  6 11:06:46 gb-test kernel: [    4.082107] systemd[1]: Starting Create System Users...
        Sep  6 11:06:46 gb-test kernel: [    4.088004] systemd[1]: Finished Monitoring of LVM2 mirrors, snapshots etc. using dmeventd or progress polling.
        Sep  6 11:06:46 gb-test kernel: [    4.094145] systemd[1]: Finished Load Kernel Modules.
      ```

1. Создать разовое задание на перезагрузку операционной системы, используя at.

    * Создание задание на перезагрузку. Внутри файла reboot находится только одна команда - reboot
    `sudo at -f /home/user/bash-practise/reboot.sh 8:14pm 09/08/2021`
    * Задача в списке atq  
    `10      Thu Sep  8 20:14:00 2021 a user`
  
1. Написать скрипт, делающий архивную копию каталога etc, и прописать задание в crontab.

    * Создаем crontab для root пользователя `sudo crontab -e`
    * Выбираем одни из текстовых редакторов, и в конце файла прописываем:
    `@weekly tar -zcf /var/backups/etc.tgz /etc/`
    Эта команда создает архивную копию каталога etc один раз в неделю.