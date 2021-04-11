t = int
hour = int
minute = int
sec = int
t = int(input("Приветствую, введи свое число в секундах: "))
hour = t // 3600
minute = (t - hour * 3600) // 60
sec = t - (hour * 3600 + minute * 60)
if minute < 10:
    minute = str("0" + str(minute))
else:
    minute = int(minute)
if sec < 10:
    sec = str("0" + str(sec))
else:
    sec = int(sec)
print ("Твое число в формате чч:мм:сс - %s : %s : %s" %(hour,minute,sec))


