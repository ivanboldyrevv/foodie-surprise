import requests

from bs4 import BeautifulSoup
from database import Database


class PageParser:
    def __init__(self):
        self.category = 'zakuski'
        self.__page_url = 'https://food.ru/recipes/'
        self.recipes_after_parse = {}

    def run(self):
        self.get_parse_data_from_soup()
        self.recipes_to_db()
        return 'Write to database: success'

    def recipes_to_db(self):
        db = Database()
        for recipe_name, recipe_url in self.recipes_after_parse.items():
            db.send_recipe_to_db(recipe_name, recipe_url)

    def get_parse_data_from_soup(self):
        for recipe in self.__cooking_soup().find_all('a', class_='card_card__CQFJS'):
            self.recipes_after_parse[recipe.text] = 'https://food.ru' + recipe.get('href')
        return self.recipes_after_parse if len(self.recipes_after_parse) else None

    def __get_page_text(self):
        page = requests.get(self.__page_url + self.category)
        return page.text

    def __cooking_soup(self):
        page = self.__get_page_text()
        soup = BeautifulSoup(page, 'html.parser')
        return soup


if __name__ == '__main__':
    script = PageParser()
    script.run()
