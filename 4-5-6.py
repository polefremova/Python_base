# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class Warehouse:
    pass


class Shelf(Warehouse):
    def total(self):
        self.total = []

    def to_get(self, quantity):
        self.total.append(quantity)


class Technics:
    def __init__(self, type, model, price, quantity):
        self.type = type
        self.model = model
        self.price = price
        self.quantity = quantity

    def to_send(self, q, *shelfs):
        for shelf in shelfs:
            shelf.to_get(q)

    def info(self):
        type = int(input("Выберите необходимый вариант:\n1 - Принтер,\n2 - Сканер,\n3 - Ксерокс\nПоле ввода: "))
        if type not in range(1, 4):
            print("Данный тип товара отсутствует")
        else:
            model = input("Введите название модели техники: ")
            price = int(input("Введите цену товара: "))
            quantity = int(input("Количество экземпляров: "))
            print("Ваш заказ укомплектован")

class Printer(Technics):
    # super().__init__(self, model, price, quantity):
    pass


class Copier(Technics):
    # super().__init__(self, model, price, quantity):
    pass


class Scanner(Technics):
    # super().__init__(self, model, price, quantity):
    pass


p = Printer(1, "Epson", 5000, 10)
s = Scanner(2, "HP", 6500, 5)
c = Copier(3, "Xerox", 4800, 12)
q = 5
p.info()
s.info()
c.info()
sh_1 = Shelf("Секция 1")
sh_2 = Shelf("Секция 2")
n.to_send(q, sh_1)