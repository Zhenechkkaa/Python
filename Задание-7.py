"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна
содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

import json

try:
    firm_dict = {}
    my_dict = {'average_profit': 0}
    result_list = [firm_dict, my_dict]
    with open('task7.txt', encoding='utf-8') as read_file:
        i_firm_count = 0
        c_lines = read_file.readlines()
        for line in c_lines:
            if len(line):
                firm_name, firm_type, firm_income, firm_costs = line.split()
                firm_profit = float(firm_income) - float(firm_costs)
                firm_dict[firm_name] = firm_profit
                if firm_profit > 0:
                    my_dict['average_profit'] += firm_profit
                    i_firm_count += 1
        if i_firm_count:
            my_dict["average_profit"] /= i_firm_count
        print(f'{json.dumps(result_list, ensure_ascii=False)}')
    with open('task7.json', 'w') as write_file:
        json.dump(result_list, write_file, ensure_ascii=False)
except IOError:
    print('Ошибка открытия файла')
