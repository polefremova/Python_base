# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

from itertools import cycle


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "\n".join(map(str, self.matrix))

        # Подскажите, можно ли использовать такой вариант? Или как его необходимо доработать?
        # count = 0
        # for row in cycle(self.matrix):
        #     if count > len(self.matrix):
        #         break
        #     print(row)
        #     count +=1

    def __add__(self, other):
        try:
            for el in range(len(self.matrix)):
                for el_other in range(len(other.matrix[el])):
                    self.matrix[el][el_other] = self.matrix[el][el_other] + other.matrix[el][el_other]
            return "\n".join(map(str, self.matrix))
        except IndexError:
            print("Не удается сложить разноразмерные матрицы")


matrix_1 = Matrix([[31, 32], [37, 43], [51, 86]])
matrix_2 = Matrix([[3, 5], [2, 6], [-1, -8]])
# matrix_3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
print("\n".join(map(str, matrix_1.matrix)))
print(f"\nСумма матриц:\n{matrix_1 + matrix_2}")