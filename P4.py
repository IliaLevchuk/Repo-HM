user_words = input("Введите набор слов через пробел: ").split()
for i, words in enumerate(user_words, 1):
    print(f"{i}:{words:.10}")
