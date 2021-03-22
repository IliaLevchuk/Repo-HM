
with open("txt1.txt", 'x' , encoding='utf-8') as f_1:
    while True:
        content = (input("Введите текст или для завершения нажмите (Enter): "))
        if not content:
            break
        f_1.write(f"{content}\n")



