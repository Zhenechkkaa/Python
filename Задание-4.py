"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

try:
    with open('task4.txt') as new_file:
        with open('task4-1.txt', 'w') as new_file2:
            my_list = ["Один", "Два", "Три", "Четыре"]
            c_lines = new_file.readlines()
            for num, line in enumerate(c_lines):
                if len(line):
                    words = line.split()
                    print(f'{my_list[num]} {words[1]} {words[2]}', file=new_file2)
except IOError:
    print('Ошибка открытия файла')
