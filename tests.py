import unittest
from app import PageParser, OutputFormatting

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

result_dict = {
    'рецепт11 дней 1 часБастурма из свинины': 'https://food.ru/recipes/197718-basturma-iz-svininy',
    'рецепт15 минутКанапе с помидорами черри и сыром': 'https://food.ru/recipes/197641-kanape-na-shpazhkakh',
    'рецепт1 час 10 минутБлины с начинкой из курицы и ананаса': 'https://food.ru/recipes/197643-salat-v-blinakh',
    'рецепт30 минутДомашняя шаурма с курицей': 'https://food.ru/recipes/197656-shaurma-s-kuritsei-v-domashnikh-usloviiakh',
    'рецепт15 минутТарталетки с красной рыбой и огурцом': 'https://food.ru/recipes/197668-tartaletki-s-krasnoi-ryboi-i-ogurcom',
    'рецепт1 ч Хачапури на сковороде': 'https://food.ru/recipes/197566-khachapuri-na-skovorode',
    'рецепт15 минутБутерброды с красным луком и помидором': 'https://food.ru/recipes/197569-legkaia-zakuska',
    'рецепт1 день 2 часаПаштет из свиной и куриной печени': 'https://food.ru/recipes/197630-miasnaia-zakuska',
    'рецепт1 ч Бургер с креветкой кацу': 'https://food.ru/recipes/196937-burger-s-krevetkoi-katsu',
    'рецепт20 минутГорячие бутерброды с сосисками и моцареллой': 'https://food.ru/recipes/197040-buterbrody-na-skovorode',
    'рецепт30 минутТосты с беконом и яйцом': 'https://food.ru/recipes/197513-prostaia-novogodniaia-zakuska',
    'рецепт35 минутОстрые рыбные тако': 'https://food.ru/recipes/196935-ostrye-rybnye-tako',
    'рецепт30 минутБутерброды с тунцом': 'https://food.ru/recipes/197030-buterbrody-s-tuntsom',
    'рецепт3 ч 25 мСалат из огурцов с перцем чили': 'https://food.ru/recipes/197504-iz-svezhikh',
    'рецепт10 минутКапрезе в виде божьих коровок': 'https://food.ru/recipes/196956-kapreze-v-vide-bozhikh-korovok',
    'рецепт10 минутТарталетки со сливочным сыром и беконом': 'https://food.ru/recipes/197451-prostaia-zakuska',
    'рецепт30 минутСэндвич с обжаренной куриной грудкой и моцареллой': 'https://food.ru/recipes/197014-sendvich-s-obzharennoi-kurinoi-grudkoi-i-motsarelloi',
    'рецепт25 минутКлассический форшмак из сельди': 'https://food.ru/recipes/197736-forshmak-klassicheskii-iz-seldi',
    'рецепт45 минутСалат-закуска «Ракушка». Здоровое питание с Ольгой': 'https://food.ru/recipes/203345-salat-zakuska-rakushka-1700651561',
    'рецепт2 ч 25 мХот-доги с домашними булочками': 'https://food.ru/recipes/196889-bulochka-dlia-khot-doga'
}


class Tests(unittest.TestCase):
    format_obj = OutputFormatting()
    format_obj.dict = begin_menu
    correct_output = ('Доступный ЗОЖ: 1\n'
                      'Закуски: 2\n'
                      'Салаты: 3\n'
                      'Первый блюда: 4\n'
                      'Вторые блюда: 5\n'
                      'Гарниры: 6\n'
                      'Десерты: 7\n'
                      'Выпечка: 8\n'
                      'Напитки: 9\n'
                      'Заготовки и консервы: 10\n'
                      'Соусы и маринады: 11')

    def test_parse_non_existing_category(self):
        parse_obj = PageParser()
        parse_obj.category = 'non-existing-category'
        self.assertIsNone(parse_obj.get_parse_data_from_soup())

    def test_parse_existing_category(self):
        parse_obj = PageParser()
        parse_obj.category = 'zakuski'
        self.assertIsInstance(parse_obj.get_parse_data_from_soup(), dict)

    def test_begin_menu_output_formatting(self):
        self.assertEqual(self.format_obj.output_format(), self.correct_output)


if __name__ == '__main__':
    unittest.main()
