def DIV (x, y):
    try:
        x / y
        return x / y
    except ZeroDivisionError:
        return ("Ошибка деление на 0")
    except ValueError:
        return ("Можно вводить только числа")
print(DIV((int(input("Введите X = "))), int(input("Введите Y = "))))







