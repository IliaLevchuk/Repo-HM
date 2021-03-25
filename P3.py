class Cell:

    def __init__(self, cells):
        self.cells = cells

    def __str__(self):
        print(f"Клетка состоит из {self.cells}")
    def __add__(self, other):
        print(f'Ваш ответ : {self.cells + other} ')

    def __sub__(self, other):
        if other > self.cells:
            print(f"{self.cells - other} - Невозможная операция")
        else:
            print(f'Ваш ответ : {(self.cells - other)}')

    def __mul__(self, other):
        print(f'Ваш ответ : {self.cells * other}')

    def __truediv__(self, other):
        print(f'Ваш ответ : {self.cells // other}')

    def make_order(self, cells_in_row):
        self.cells_in_row = cells_in_row
        rows, till = self.cells // cells_in_row, self.cells % cells_in_row
        print('\n'.join(["*" * rows] * rows +(["*" * till] if till else [])))


cell = Cell(7)
cell.make_order(4)
cell.__sub__(4)
cell.__add__(5)
