"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

try:
    with open('task2.txt') as new_file:
        c_lines = new_file.readlines()
        for i, line in enumerate(c_lines):
            print(f'В строке {i + 1} слов: {len(line.split())}')
        print(f'Всего строк: {len(c_lines)}')
except IOError:
    print('Ошибка открытия файла!')
