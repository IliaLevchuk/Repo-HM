

#def fact(a):
#    point = 1
#    while point < a:
#        yield point
#        point += 1

#c = 0
#my_list = [int(el) for el in input("Введите значения: ").split()]
#for el in my_list:
#    for i in fact(el):
#        if c > 10:
#            break
#        print(i, end="*")
#        c += 1


def fact(a):
    for i in range(1, a+1):
        point = 1
        while i > 0:
            point *= i
            i -= 1
        yield point

n = int(input())
x = [i for i in fact(n)]
print(x)
for i in x:
    print(i)