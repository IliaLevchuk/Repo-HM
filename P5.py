class Stationary:

    def __init__(self, title=""):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки! {self.title}')


class Pen(Stationary):
    def draw(self):
        print(f'Запуск отрисовки с Pen! {self.title}')


class Pencil(Stationary):
    def draw(self):
        print(f'Запуск отрисовки с Pencil! {self.title}')


class Marker(Stationary):
    def draw(self):
        print(f'Запуск отрисовки с Marker! {self.title}')

stat = Stationary()
stat.draw()

pen = Pen()
pencil = Pencil()
mark = Marker()

pen.draw()
pencil.draw()
mark.draw()
