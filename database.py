from db1.get_db import get_db


class Database:
    def __init__(self):
        self.db = get_db()
        self.recipes_dict = {}

    def send_recipe_to_db(self, name, url):
        self.db.execute('INSERT INTO recipes (name, url) VALUES (?, ?)', (name, url))
        self.db.commit()

    def get_recipes_from_db_to_dict(self):
        recipes = self.db.execute('SELECT name, url FROM recipes').fetchall()
        for recipe in recipes:
            self.recipes_dict[recipe['name']] = recipe['url']

    def get_recipes_dict(self):
        return self.recipes_dict

