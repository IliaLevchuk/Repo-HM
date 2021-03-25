import random


class Matrix:

    def __init__(self, strings, columns):
        self.strings = strings
        self.columns = columns
        self.matrix = [[random.randint(0, 100) for x in range(strings)] for y in range(columns)]


    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        result = []
        print(other)
        for item in zip(self.matrix, other):
            result.append([sum([j, k]) for j, k in zip(*item)])
        return result


#При попытке сложения двух объектро класса Matrix, выдает ошибку, не смог разобраться почему.(вторую матрицу он делает int строкой, а не списком).
# и как можно применить способ __str__ к сумме матриц?
obj = Matrix(2, 2)
obj_2 = Matrix(2, 2)
print(Matrix.__str__(obj))
print("-" * 70)
print(Matrix.__str__(obj_2))
print(f"Ваша новая матрица: {(obj.__add__(obj_2)).__str__()}")

