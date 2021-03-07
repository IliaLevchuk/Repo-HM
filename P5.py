user_point = int(input("Введите число: "))
my_list = [7, 4, 6, 8, 7, 2]
my_list.extend([user_point])
my_list.sort(reverse=True)
print(my_list)