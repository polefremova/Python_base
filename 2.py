# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, parametrs):
        self.parametrs = parametrs

    @property
    def consumption(self):
        print(f"Всего затрачено ткани: {round((self.parametrs / 6.5 + 0.5), 1) + (2 * self.parametrs + 0.3)}")

    @abstractmethod
    def abstract(self):
        return "Smth"


class Coat(Clothes):
    def consumption(self):
        print(f"Необходимо на пошив пальто: {round((self.parametrs / 6.5 + 0.5), 1)}")

    def abstract(self):
        pass


class Costume(Clothes):
    def consumption(self):
        print(f"Необходимо на пошив костюма: {2 * (self.parametrs) + 0.3}")

    def abstract(self):
        pass


n = Coat(100)
m = Costume(50)
print(n.consumption())
print(m.consumption())
print(f"Всего затрачено ткани: {round((n.parametrs / 6.5 + 0.5), 1) + (2 * m.parametrs + 0.3)}")