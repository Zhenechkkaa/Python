"""
Задание 4.
Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).
А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
            print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Превышение скорости {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Превышение скорости {self.speed} км/ч')


class PoliceCar(Car):
    pass


pc = PoliceCar(67, 'silver', 'Geely', True)
pc.go()
pc.turn('налево')
pc.show_speed()


wc = WorkCar(80, 'green', 'Nissan', False)
wc.go()
wc.stop()
wc.turn('направо')
wc.show_speed()


tc = TownCar(45, 'black', 'Fiat', False)
tc.go()
tc.stop()
tc.turn('направо')
tc.show_speed()


sc = SportCar(90, 'black', 'Honda', False)
sc.go()
sc.stop()
sc.turn('направо')
sc.show_speed()
