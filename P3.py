class ListError(ValueError):
    def __init__(self, *args):
        self.args = args

    def list_chek(self):
        my_list = []
        while True:
            try:
                value = input('Введите число или для завершения "end": ')
                if value == "end":
                    print(f'Конечный список {my_list}')
                    break
                if not value.isdigit():
                    raise ListError(value)
                my_list.append(int(value))
            except ListError as er:
                print('Вы ввели str или Boole', er)
            print(my_list)

df = ListError()
df.list_chek()