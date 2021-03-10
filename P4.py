def my_func(x, y):
    z = 1
    for i in range(abs(y)):
        z = z / x
    return z
print(my_func(int(input()), int(input())))