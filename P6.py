from itertools import count, cycle


def f(a, b):
    for el in count(a):
        if el > b:
            break
        print(el, end=" ")
f(int((input("Введиет число начала отсчета: "))), int(input("Введите число окончания счета: ")))
print()

c = 1
my_list = [int(el) for el in input("Введите значения: ").split()]
for el in cycle(my_list):
    if c > 3 * len(my_list):
        break
    print(el)
    c += 1
