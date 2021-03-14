my_list = [int(i) for i in input("Введите значения: ").split()]
new_list = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print("Ваш новый список:", new_list)
