# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


with open("text_3.txt", "r", encoding="utf-8") as t_3:
    sal = 0
    sol = 0
    content = t_3.readline()
    try:
        for line in content:
            line = content.split()
            if float(line[1]) < 20000.0:
                print("Зарплата менее 20 тыс. ", line[0])
                sal = sal + float(line[1])
                content = t_3.readline()
            if float(line[1]) >= 20000.0:
                sol = sol + float(line[1])
                content = t_3.readline()
    except:
        av_sal = (sal + sol) / 10
        print("Средняя заработная плата: ", av_sal)
