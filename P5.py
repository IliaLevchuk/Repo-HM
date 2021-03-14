from functools import reduce

my_list = [el for el in range(100, 1001, 2)]

def f(a, b):
    return a * b
print(reduce(f,my_list))
