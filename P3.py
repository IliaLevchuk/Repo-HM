with open('text3.txt', "x" ,encoding="utf-8") as f_3:
    while True:
        content = (input("Введите имя сотрудника и его заработную плату через пробел или для завершения нажмите (Enter):"))
        if not content:
           break
        f_3.write(f"{content}\n")

with open('text3.txt', "r" ,encoding="utf 8") as object_file:
    data_dir = {line.split()[0]: float(line.split()[1]) for line in object_file}
    print(f"Средняя заработная плата = {sum(data_dir.values())/ len(data_dir)}\n"
          f"Список сотрудников с зарплатой меньше 20к {[el[0] for el in data_dir.items() if el[1]<20000]}")
