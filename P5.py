with open("text5.txt", "w+", encoding="utf-8") as f:
    while True:
        content = (input("Введите цифры через пробел или для завершения нажмите (Enter): "))
        if not content:
            break
        f.write(content)
        f.seek(0)
    print(f"Сумма чисел в файле:{sum(map(int, ''.join(f.readlines()).split()))}")
