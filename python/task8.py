initial_text = 'Необходимо считать любой текстовый файл на вашем ПК (можно создать новый) и создать на его основе новый файл, где содержимое будет записано в обратном порядке. В конце программы вывести на экран оба файла - старый в неизменном виде и новый в обратном порядке.'

# Создание и запись текста в файл
with open('file1.txt', 'w', encoding='utf8') as w_file:
  w_file.write(initial_text)

# Чтение из файла, редактирование считанного текста
with open('file1.txt', 'r', encoding='utf8') as r_file:
  read_text = r_file.read()
  reversed_text = read_text[::-1]

# Запись редактированного текста в новый файл
with open('file2.txt', 'w', encoding='utf8') as w_file:
  w_file.write(reversed_text)