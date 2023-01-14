"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(arg1, arg2, arg3):
    print(f'Сумма наибольших двух аргументов равна: {arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')


my_func(
    int(input('Аргумент 1:')),
    int(input('Аргумент 2:')),
    int(input('Аргумент 3:')),
)


def my_func2(arg1, arg2, arg3):
    my_list = [arg1, arg2, arg3]
    my_list.sort()
    res = my_list[2] + my_list[1]
    print(f'Сумма наибольших двух аргументов равна: {res}')


my_func2(
    int(input('Аргумент 1:')),
    int(input('Аргумент 2:')),
    int(input('Аргумент 3:')),
)
