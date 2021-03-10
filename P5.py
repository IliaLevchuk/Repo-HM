def SUM (list_digit):
    digit_sum = 0
    while True:
        n = list_digit.split(" ")
        for digit in n:
            try:
                digit = int(digit)
                digit_sum += digit
            except Exception:
                if digit == "f":
                    print(f"Сумма {digit_sum}")
                    return digit_sum
                else:
                    print(f"Сумма {digit_sum}, Допущенна ошибка")
                    return digit_sum
        list_digit = input("Введите числа : ")

print(SUM(input("Введите числа ")))




