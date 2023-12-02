begin_menu = {
    'Доступный ЗОЖ': [1, 'dostupnyi-zozh'],
    'Закуски': [2, 'zakuski'],
    'Салаты': [3, 'salaty'],
    'Первый блюда': [4, 'pervye-bliuda'],
    'Вторые блюда': [5, 'vtorye-bliuda'],
    'Гарниры': [6, 'garniry'],
    'Десерты': [7, 'deserty'],
    'Выпечка': [8, 'vypechka'],
    'Напитки': [9, 'napitki'],
    'Заготовки и консервы': [10, 'zagotovki'],
    'Соусы и маринады': [11, 'sousy-i-marinady']
}


class OutputFormatting:
    def __init__(self):
        self.dict = dict()

    def output_format(self):
        result = ''
        for key, values in self.dict.items():
            result += '{}: {}'.format(key, values[0]) + '\n'
        return result.strip()
