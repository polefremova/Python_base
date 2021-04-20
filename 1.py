# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def my_func(per_a, per_b):
    try:
        per_b != 0
        sub = per_a / per_b
        print(f"Решение: {per_a} / {per_b} = ", sub)
    except ZeroDivisionError:
        print("Ошибка! Деление на ноль запрещено")


my_func((int(input("per_a: "))), (int(input("per_b: "))))