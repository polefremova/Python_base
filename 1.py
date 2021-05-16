# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

from datetime import date


class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def set_date(cls, date):
        d, m, y = map(int, date.split("-"))
        date_1 = cls(d, m, y)
        # return date_1
        return cls(d, m, y)


    @staticmethod
    def validation(date):
        d, m, y = map(int, date.split("-"))
        if d in range(1, 32) and m in range(1, 13) and y in range(1000, 4000):
            print(f"Дата {date} корректна!")
            return d, m, y
        else:
            print("Данные не соответствуют формату 'дата'")


n = "28-17-2010"
res_1 = Date.set_date(n)
res_2 = Date.validation(n)
