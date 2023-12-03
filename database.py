from db1.get_db import get_db


class Database:
    def __init__(self):
        self.db = get_db()
        self.recipes_dict = {}

    def send_recipe_to_db(self, name, url, category):
        self.db.execute('INSERT OR IGNORE INTO recipes (name, url, category) VALUES (?, ?, ?)', (name, url, category))
        self.db.commit()

    def get_recipes_from_db_to_dict(self):
        recipes = self.db.execute('SELECT name, url FROM recipes').fetchall()
        for recipe in recipes:
            self.recipes_dict[recipe['name']] = recipe['url']

    def get_recipes_dict(self):
        return self.recipes_dict

    def get_categories(self):
        return self.db.execute('SELECT * FROM category').fetchall()

    def get_recipes_by_category(self, category_id):
        return self.db.execute('SELECT recipes.name as recipe_name, recipes.url as recipe_url FROM category '
                               'JOIN recipes ON recipes.category = category.id '
                               'WHERE category = ? '
                               'ORDER BY RANDOM() '
                               'LIMIT 5', (category_id,)).fetchall()
