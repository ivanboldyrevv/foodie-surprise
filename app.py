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
        self.options = {'rr': self.restart,
                        'r': self.process_category,
                        'q': self.quit
                        }

    @clear_console
    def run(self):
        self.print_categories()
        self.wait_input()

    def quit(self, chosen_category):
        print('GOODBYE PISS')
        exit()

    @design_pattern
    def print_categories(self):
        categories = self.db.get_categories()
        print('Выберите категорию')
        print('-' * 80)
        for category in categories:
            print('{}: {}'.format(category['name'], category['id']))

    def wait_input(self, chosen_category=None):
        user_input = input()
        if user_input.isdigit() and self.check_input_categories(user_input):
            chosen_category = user_input
            self.print_answer(chosen_category)
        if user_input in self.options:
            self.options[user_input](chosen_category)
        return self.wait_input(chosen_category)

    def check_user_input(self, user_input):
        if user_input not in self.options:
            print('Нет такой команды')
            sleep(2)
            return self.run()

    def check_input_categories(self, chosen_category):
        nums = [str(i) for i in range(1,11)]
        if chosen_category not in nums:
            print('Нет такой категории')
            sleep(1)
            self.restart(None)
        return True

    @clear_console
    def restart(self, chosen_category):
        self.run()

    @clear_console
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
        if user_input == 'q':
            self.quit(chosen_category)


if __name__ == '__main__':
    app = App()
    app.run()
