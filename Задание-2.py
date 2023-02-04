"""
Задание 2.
Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyException(Exception):

    @staticmethod
    def division_func(num1, num2):
        try:
            res = round(num1 / num2, 2)
        except ZeroDivisionError:
            print(f"На ноль делить нельзя!\n")
        else:
            print(f"{num1}/{num2} = {res} \n")


m_e = MyException()

m_e.division_func(10, 2)
m_e.division_func(7, 0)
m_e.division_func(-6, 3)
m_e.division_func(0, 5)
