"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

import sys

script_name, emp_name, s_rate, emp_hours, emp_bonus = sys.argv


def salary(rate, hours, bonus):
    try:
        print(f'Заработная плата сотрудника {emp_name} составляет {int(rate) * int(hours) + int(bonus)}')
    except TypeError:
        exit()


salary(s_rate, emp_hours, emp_bonus)
