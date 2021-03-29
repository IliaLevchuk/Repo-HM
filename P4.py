from abc import ABC, abstractmethod
from prettytable import PrettyTable
x = PrettyTable()


class Stok():

    def __init__(self):
        self.unit_sklad = {}

    def add_product(self, equipment):
        try:
            self.unit_sklad.setdefault(equipment.name, []).append(equipment.__dict__)
            if not (equipment.__dict__).get('model') == int \
                    or (equipment.__dict__).get('year') == int:
                raise ValueError(equipment.year, equipment.quantity)
        except ValueError as error:
            print("Неверно введены данные, введите числовые занчения", error)
        else:
            print(f"Вы добавили: {equipment.name}")


    def extract_data(self, name, model, year, make, quantity):
        if self.unit_sklad[name]:
            self.unit_sklad.setdefault(name).pop(0)
        # if self.unit_sklad[model]:
        #     self.unit_sklad.setdefault(model).pop(0)
        # if self.unit_sklad[year]:
        #     self.unit_sklad.setdefault(year).pop(0)
        # if self.unit_sklad[make]:
        #     self.unit_sklad.setdefault(make).pop(0)
        # if self.unit_sklad[quantity]:
        #     self.unit_sklad.setdefault(quantity).pop(0)


class OrgTech(ABC):
    def __init__(self, name, model, year, make, quantity):
        self.name = name
        self.quantity = quantity
        self.year = year
        self.make = make
        self.model = model

    def __str__(self):
        x.add_column('Name', self.name)
        x.add_column('Model', self.model)
        x.add_column('Year', self.year)
        x.add_column('Make', self.make)
        x.add_column('Quantity', self.quantity)
        return x

    def ection(self):
         pass


class Printer(OrgTech):

    def __init__(self, name, model, year, make, quantity, series):
        super().__init__(name, model, year, make, quantity)
        self.series = series

    def __str__(self):
        x.add_column('Name', [self.name])
        x.add_column('Model', [self.model])
        x.add_column('Year', [self.year])
        x.add_column('Make', [self.make])
        x.add_column('Quantity', [self.quantity])
        x.add_column('Series', [self.series])
        return x

    @staticmethod
    def action():
        print("Распечатываю")


class Xerox(OrgTech):

    def __init__(self, name, model, year, make, quantity):
        super().__init__(name, model, year, make, quantity)

    def __str__(self):
        x.add_column('Name', [self.name])
        x.add_column('Model', [self.model])
        x.add_column('Year', [self.year])
        x.add_column('Make', [self.make])
        x.add_column('Quantity', [self.quantity])
        return x

    @staticmethod
    def action():
        print("Копирую")


class Scanner(OrgTech):

    def __init__(self, name, model, year, make, quantity):
        super().__init__(name, model, year, make, quantity)

    def __str__(self):
        x.add_column('Name', [self.name])
        x.add_column('Model', [self.model])
        x.add_column('Year', [self.year])
        x.add_column('Make', [self.make])
        x.add_column('Quantity', [self.quantity])
        return x

    @staticmethod
    def action():
        print("Сканирую")


sklad = Stok()
printer = Printer("hp", "2000", 2020, "russia", 6, 12006)
printer.action()
print(printer.__str__())
sklad.add_product(printer)


