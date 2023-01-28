"""
Задание 5.
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        self.title = 'pen'
        print(f'Запуск отрисовки {self.title}')


class Pencil(Stationary):
    def draw(self):
        self.title = 'pencil'
        print(f'Запуск отрисовки {self.title}')


class Handle(Stationary):
    def draw(self):
        self.title = 'handle'
        print(f'Запуск отрисовки {self.title}')


pen = Pen('title1')
pencil = Pencil('title2')
handle = Handle('title3')
pen.draw()
pencil.draw()
handle.draw()
