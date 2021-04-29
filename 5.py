# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:

    def __init__(self, t):
        self.title = t

    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pen(Stationery):
    def tool_pen(self, t):
        super().draw()


class Pencil(Stationery):
    def tool_pencil(self, t):
        super().draw()


class Handle(Stationery):
    def tool_handle(self, t):
        super().draw()


way_1 = Pen("ручкой")
way_1.tool_pen("ручкой")
way_2 = Pen("карандашом")
way_2.tool_pen("карандашом")
way_3 = Pen("маркером")
way_3.tool_pen("маркером")
