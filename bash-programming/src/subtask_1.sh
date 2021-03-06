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