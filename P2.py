list_1 = list(input("Введите значения: "))
for i in range(1, len(list_1), 2):
    list_1.insert(i-1, list_1.pop(i))
print(" ".join(list_1))