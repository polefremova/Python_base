# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения
# и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        sum = self.a + self.b + other.a + other.b
        return f"Сумма: {sum}"

    def __mul__(self, other):
        prod = (self.a * other.a - (self.b * other.b)) * (self.a * other.b + other.a * self.b)
        return f"Произведение: {round(prod, 4)}"

el_1 = Complex(7, 5.2)
el_2 = Complex(4.5, 9)
print(el_1 + el_2)
print(el_1 * el_2)