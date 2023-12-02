import sqlite3


def get_db():
    db = sqlite3.connect('C:/Users/meteor/PycharmProjects/foodie-surprisev2.0-tdd/instance/recipes.db', detect_types=sqlite3.PARSE_DECLTYPES)
    db.row_factory = sqlite3.Row
    return db
