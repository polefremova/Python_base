# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


with open("kolobok.txt", "w+", encoding="utf-8") as skazka:
    while True:
        text = input("enter smt: ")
        if text == "":
            break
        else:
            print(text, file=skazka)
    skazka.seek(0)
    print(skazka.read())