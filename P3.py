class Worker:

     def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage":wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f"Имя и фамилия сотрудника: {' '.join([self.name, self.surname])}"
    def get_full_profit(self):
        return f"Общий доход сотрудника: {sum(self._income.values())}"

Worker = Position('Pup', 'Pupich', 'Mer', 50000, 10000000)
print(f'{Worker.get_full_name()}\n{Worker.get_full_profit()}')

