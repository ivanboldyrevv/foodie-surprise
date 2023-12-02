import requests

import re

from bs4 import BeautifulSoup
from database import Database

patterns = [r'рецепт\d+ минут', r'рецепт\d+ч \d+ минут', r'рецепт\d+ часа \d+ минут',
            r'рецепт\d+ часа \d+ м', r'рецепт\d+ ч \d+ м', r'рецепт\d+ час',
            r'рецепт\d+ ч', r'рецепт\d+ д \d+ ч', r'рецепт\d+ день+ \d+ час', r' \d+ минут']


class PageParser:
    def __init__(self):
        self.db = Database()
        self.category = 'zakuski'
        self.__page_url = 'https://food.ru/recipes/'
        self.recipes_after_parse = {}

    def run(self):
        self.get_parse_data_from_soup()
        self.recipes_to_db()
        return 'Write to database: success'

    def recipes_to_db(self):
        for recipe_name, recipe_values in self.recipes_after_parse.items():
            recipe_name = '{}'.format(re.sub("|".join(patterns), '', recipe_name))
            self.db.send_recipe_to_db(recipe_name, recipe_values[0], recipe_values[1])

    def get_parse_data_from_soup(self):
        categories = self.db.get_categories()
        for url_name in categories:
            for recipe in self.__cooking_soup(url_name['url_name']).find_all('a', class_='card_card__CQFJS'):
                self.recipes_after_parse[recipe.text] = ['https://food.ru' + recipe.get('href'), url_name['id']]
        return self.recipes_after_parse

    def __get_page_text(self, category):
        page = requests.get(self.__page_url + category)
        return page.text

    def __cooking_soup(self, category):
        page = self.__get_page_text(category)
        soup = BeautifulSoup(page, 'html.parser')
        return soup


if __name__ == '__main__':
    script = PageParser()
    script.run()
