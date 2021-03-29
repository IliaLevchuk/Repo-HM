class Data:

    def __init__(self, date_month_year):
        self.date_month_year = str(date_month_year)

    @classmethod
    def data(cls, date_month_year):
        content = [i for i in date_month_year.split() if i != "-"]
        print(content)
        return int(content[0]), int(content[1]), int(content[2])

    @staticmethod
    def validation(date, month, year):
        if 0 < date < 31:
            if 0 < month < 12:
                if year > 0:
                    print(f"Ваша дата: {date}-{month}-{year}")
                else:
                    print("Не верно ввенден год")
            else:
                print("Не верно ввенден месяц")
        else:
            print("Не верно ввенден день")

data = Data(11 - 22 - 33)
print(data)
print(Data.data('11 - 22 - 33'))
Data.validation(11, 8, 2001)

