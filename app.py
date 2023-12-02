from database import Database
import os
from time import sleep


def design_pattern(func):
    def wrapper(*args):
        print('-' * 80)
        func(*args)
        print('-' * 80)
        print('Выход: q, рестарт: rb, рестарт текущей категории: r')

    return wrapper


def clear_console(func):
    def wrapper(*args):
        os.system('cls')
        func(*args)

    return wrapper


class App:
    def __init__(self):
        self.db = Database()
        self.options = {'rb': self.restart,
                        'r': self.process_category,
                        'q': self.quit
                        }

    def run(self):
        self.print_categories()
        chosen_category = int(input())
        if self.check_input_categories(chosen_category):
            self.print_answer(chosen_category)
        else:
            self.restart(chosen_category)

        user_input = input()
        if user_input in self.options:
            self.options[user_input](chosen_category)

    def quit(self, chosen_category):
        print('GOODBYE PISS')
        exit()

    def check_input_categories(self, chosen_category):
        if 1 > chosen_category or chosen_category > 11:
            print('Нет такой категории')
            sleep(1)
            return False
        return True

    @clear_console
    def restart(self, chosen_category):
        # Действия, которые нужно выполнить при перезапуске программы
        print("Restarting...")
        # Опционально можно добавить дополнительную логику или очистку перед перезапуском
        # ...
        self.run()

    @design_pattern
    def print_categories(self):
        categories = self.db.get_categories()
        print('Выберите категорию')
        print('-' * 80)
        for category in categories:
            print('{}: {}'.format(category['name'], category['id']))

    @design_pattern
    def print_answer(self, chosen_category):
        recipes_category = self.db.get_recipes_by_category(chosen_category)
        for recipe in recipes_category:
            print(recipe['recipe_name'], recipe['recipe_url'])

    @clear_console
    def process_category(self, chosen_category):
        self.print_answer(chosen_category)
        user_input = input()

        if user_input == 'r':
            self.process_category(chosen_category)


if __name__ == '__main__':
    app = App()
    app.run()
