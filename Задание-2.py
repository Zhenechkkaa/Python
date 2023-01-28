"""
Задание 2.
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.
Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:
    __length = 0
    __width = 0

    def __init__(self, length, width, weight, thickness):
        self.__length = length
        self.__width = width
        self.weight = weight
        self.thickness = thickness

    def asp_mass(self):
        my_length = self.__length
        my_width = self.__width
        my_weight = self.weight
        my_thickness = self.thickness
        total = my_length * my_width * my_weight * my_thickness / 1000
        return print(f"Масса асфальта:\n "
                     f"{my_length} м * {my_width} м * {my_weight} кг * {my_thickness} м = ", total, "т")


my_road = Road(20, 5000, 25, 0.05)
my_road.asp_mass()
