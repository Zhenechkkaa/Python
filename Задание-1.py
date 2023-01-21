"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

file_name = "task1.txt"

try:
    with open(file_name, 'w', encoding='utf-8') as file:
        while True:
            my_str = input('Введите строку: ')
            if my_str == "":
                break

            file.write(f'{my_str}\n')
except IOError:
    print("Произошла ошибка ввода-вывода!")
