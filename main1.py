day = int(input("Введи день недели: "))

if day > 7 or day < 1:
    print("Please, repeat the input")
elif day == 6 or day == 7:
    print("Выходной")
else:
    print("Не выходной")