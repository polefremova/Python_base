# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class MyError(Exception):

    def __init__(self, my_list):
        self.my_list = my_list


my_list = []
while True:
    m = input("Введите числа в список: ")
    list_m = m.split()
    for m in list_m:
        try:
            if m == '#':
                print(f"Операция завершена! Итоговый список:\n{my_list}")
                break
            else:
                try:
                    m = int(m)
                    my_list.append(int(m))
                except:
                    raise MyError("Введеное значение не является числом")
        except (ValueError, MyError) as error:
            print(error)

print(my_list)
