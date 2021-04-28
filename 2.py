# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.


with open("morozko.txt", "w+", encoding="utf-8") as chudo:
    num = 0
    while True:
        text = input("enter smt: ")
        num = num + 1
        if text == "":
            break
        else:
            print(f"{num}) {text}", file=chudo)
            my_text = text.split()
            print(f"Количество слов: ", len(my_text))
    chudo.seek(0)
    print(chudo.read())
    print(f"Всего {num - 1} строк")