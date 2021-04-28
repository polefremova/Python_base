# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.


words = dict(One="Один", Two="Два", Three="Три", Four="Четыре")

with open("translate.txt", "w", encoding="utf-8") as tr:
    with open("text_4.txt", "r", encoding="utf-8") as t_4:
        for text in t_4:
            print((text.replace(text.split()[0], words.get(text.split()[0]))), file=tr, end="")