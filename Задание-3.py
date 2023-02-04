"""
Задание 3.
Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class Error:
    def __init__(self):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except ValueError:
                print(f"Вы ввели не число!")
                y_or_n = input(f'Хотите продолжить? y/n: ')

                if y_or_n == 'y':
                    print(self.my_input())
                elif y_or_n == 'n':
                    break
                else:
                    break


a = Error()
a.my_input()
