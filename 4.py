# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

import random


class Car:

    def __init__(self, n, c, s):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = bool

    def go(self):
        print(f"{self.name}, отличный старт")

    def stop(self):
        print(f"Остановка, {self.name}")

    def turn(self):
        self.direction = random.choice(["направо", "налево", "прямо", "обратно"])
        print("Автомобиль поехал", self.direction)

    def show_speed(self):
        print(f"Скорость автомобиля: {self.speed} км/ч")


class TownCar(Car):
    def inform(self):
        super().show_speed()
        if self.speed > 60:
            print("Превышение скорости!")


class SportCar(Car):
    def inform(self):
        print(f"Цвет {self.name} - {self.color}")


class WorkCar(Car):
    def inform(self):
        super().show_speed()
        if self.speed > 40:
            print("Превышение скорости!")


class PoliceCar(Car):
    pass


bmw = TownCar("BMW", "Белый", 90)
porsche = SportCar("Porsche", "Красный", 120)
honda = WorkCar("Honda", "Синий", 53)
lexus = PoliceCar("Lexus", "Белый", 60)

bmw.go()
porsche.inform()
honda.inform()
lexus.turn()
