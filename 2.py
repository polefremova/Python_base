# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyError(Exception):

    def __init__(self, sub):
        self.sub = sub

a = int(input("Делимое: "))
b = int(input("Делитель: "))

try:
    sub = a / b
    if b == 0:
        raise MyError("Делитель не может равнаться 0!")
except (ZeroDivisionError, MyError) as error:
    print(error)
else:
    print(f"Решение: {a} / {b} = ", sub)