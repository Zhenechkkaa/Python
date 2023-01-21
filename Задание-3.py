"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

try:
    with open("task3.txt") as new_file:
        ave_salary = 0
        c_lines = new_file.readlines()
        for line in c_lines:
            u_name, salary = line.split()
            salary = float(salary)
            ave_salary += salary
            if salary < 20000:
                print(f'Оклад менее 20 тыс: {u_name} {salary}')
        if len(c_lines) > 0:
            ave_salary /= len(c_lines)
            print(f'Средняя величина дохода сотрудников: {ave_salary:.2f}')
except IOError:
    print('Ошибка открытия файла')
