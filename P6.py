stuff = []
while input("Вы хотите добавить товар: Enter Да/Нет  ") == "lf":
    nomber = int(input("Введите номер продукта: "))
    parametrs = {"Имя": None, "Цена": None, "Количество": None, "Ед": None}
    for i in parametrs.keys():
        print(i, end = ", ")
        parametrs[i] = input("Add Parametrs :")
        if parametrs[i].isdigit():
            parametrs[i] = int(parametrs[i])
    stuff.append(tuple([nomber, parametrs]))
print(stuff)
analitics = {}
for a in stuff:
    for i, n in a[1].items():
        if not i in analitics.keys():
            analitics[i] = [n]
        else:
            if n in analitics[i]:
                continue
            analitics[i].append(n)

print(analitics)
