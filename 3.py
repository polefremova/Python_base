# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    def __init__(self, n, s, p, wage, bonus):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, n, s, p, wage, bonus):
        super().__init__(n, s, p, wage, bonus)

    def get_full_name(self):
        print("Сотрудник: ", self.name + " " + self.surname)

    def get_total_income(self):
        salary = self._income.get("wage") + self._income.get("bonus")
        print(f"Зарплата: {salary} тыс. руб.")


emp_1 = Position("Мария", "Петрова", "Экономист", 30000, 5500)
emp_1.get_full_name()
emp_1.get_total_income()