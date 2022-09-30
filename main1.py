day = int(input("Введи день недели: "))

if day > 7 or day < 1:
    print("Ошибка, введи заного")
elif day == 6 or day == 7:
    print("Выходной")
else:
    print("Не выходной")