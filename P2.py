with open('text2.txt', "x" ,encoding="utf-8") as f_2:
    while True:
        content = (input("Введите текст или для завершения нажмите (Enter): "))
        if not content:
           break
        f_2.write(f"{content}\n")
lines = 0
words = 0
with open('text.txt', "r" ,encoding="utf 8") as object_file:
    for line in object_file:
       lines += 1
       n = len(line.split(" "))
       words += n
print(f"Количество строк {lines}, Количество слов {words}")
