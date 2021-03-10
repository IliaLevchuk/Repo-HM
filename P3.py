def SUM (x, y, z):
    list_1 = [x ,y, z]
    return sum(list_1) - min(list_1)
print(SUM(int(input("Введите X : ")), int(input("Введите Y : ")), int(input("Введите Z : "))))