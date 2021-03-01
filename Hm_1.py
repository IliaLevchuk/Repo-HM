a = 5
b = 5
print(a + b)


#sex = input("Укажите ваш пол: ")
#name = input("Укажите ваше имя: ")
#age = int(input("Укажите ваш возраст: "))

#print(sex, name, age, )


#time = int(input("Введите время в секундах: "))
#hours = time//3600
#minutes = (time - hours *3600)//60
#seconds = time - (hours * 3600 + minutes * 60)
#print(f"{hours}: {minutes}: {seconds}" )


#n = int(input("Ведите число: "))
#Point = str(n)
#P1 = Point + Point
#P2 = Point + Point + Point
#result = n + int(P1) + int(P2)
#print(result)

#number = abs(int(input("Введите число: ")))
#max = number % 10
#while number >= 1:
  #  number = number // 10
   # if number % 10 > max:
 #       max = number % 10
   # if number > 9:
#        continue
  #  else:
  #      print("Максимальное число = ", max)
 #       break


#money = float(input("Укажите вашу прибыль: "))
#expenses = float(input("Укажите ваши издержки: "))
#if money > expenses :
#        print(f"Ваша фирама работает с прибылью.Рентабельность выручки составила {money / expenses:.3f}")
#        worker = int(input("Укажите количество работников фирмы "))
#        print(f"Прибыль на одного сотрудника составляет: {money / worker:.2f} ")
#elif money == expenses:
#   print("Ваша фирма работает в ноль")
#else: print("Ваша фирама работает в убыток")


a = int(input("Километраж первого дня: "))
b = int(input("Необходимый результат: "))
result_days = 1
result_km = a
while result_km < b:
    a = a * 1.1
    result_days += 1
    if a < b:
        continue
    else:
     print(f"Спортсмен достигнете результата {b} км за {result_days} дней")
     break




