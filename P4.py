from googletrans import Translator

with open("txt4.txt", "r", encoding="utf-8") as f_1, open("result_4.txt", "w+", encoding="utf 8") as f_2:
    text = f_1.read()
trans = Translator
res = trans.translate(text, dest='ru')
print(f"Ваш перевод записан в файл {res}", file=f_2)