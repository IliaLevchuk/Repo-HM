month = int(input("Введите месяц: "))
if 0 < month <= 12:
    dict_1 = {"Зима": (1, 2, 12),
              "Весна": (3, 4, 5),
              "Лето": (6, 7, 8),
              "Осень": (9, 10 ,11)
             }
    dict_2 = ["Зима", "Весна", "Лето", "Осень", "Зима"]
    for i in dict_1.keys():
     if month in dict_1[i]:
       print(f'Словарь: {i}\nСписок: {dict_2[int((month) // 3)]}')
       break
else:print("Ошибка")

