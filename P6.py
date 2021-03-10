def int_funk(letters):
    n = list(letters)
    n.insert(0, n.pop(0).upper())
    for j in n:
        print(j, end="")

words = input("Введите слова через пробел: ").split()
for i in words:
    int_funk(i)
    print(i, end=" ")