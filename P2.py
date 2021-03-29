import traceback

class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt

a = int(input("Введтие числитель: "))
b = int(input("Введтие знаменатель: "))


try:
    if b == 0:
        raise ZeroError("На ноль делить нельзя")
except ZeroError as error:
    print(error)
except ValueError:
    print("Вы ввели не число")
except Exception as er:
    with open("Error.txt", "w+") as f:
        print(f"Какая-то непонятная ошибка: {f.write(traceback.format_exc(er))}")
else:
    print(f"Все хорошо. Ваше результат: {a / b}")


