list_class = {}
with open("txt6.txt", "r",encoding="utf-8") as f6:
    for line in f6:
        name, point = line.split(":")
        sum_classes = sum(map(int, "".join([el for el in point if el == " " or (el >= '0' and el <= '9')]).split()))
        list_class[name] = sum_classes
print(f"{list_class}")
