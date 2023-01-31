"""
Задание 2.
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Единственный класс этого проекта — одежда (класс Clothes).
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property
Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57
Два класса: абстрактный и Clothes
"""

from abc import abstractmethod, ABC


class Textile:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def coat_textile(self):
        return self.width / 6.5 + 0.5

    def costume_textile(self):
        return self.height * 2 + 0.3

    @property
    def full_textile(self):
        return str(f'Общий расход ткани: \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3):.2f}')

    @abstractmethod
    def abstract(self):
        return 'Абстрактный класс'


class Coat(Textile, ABC):
    def __init__(self, w, h):
        super().__init__(w, h)
        self.coat_textile = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Расход ткани на пальто: {self.coat_textile}'


class Costume(Textile, ABC):
    def __init__(self, w, h):
        super().__init__(w, h)
        self.costume_textile = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Расход ткани на костюм: {self.costume_textile}'


coat = Coat(5, 10)
costume = Costume(5, 10)
print(coat)
print(costume)
print(coat.full_textile)
print(costume.full_textile)
print(coat.abstract())
print(costume.abstract())
