import sqlite3


def init_db():
    con = sqlite3.connect('C:/Users/meteor/PycharmProjects/foodie-surprisev2.0-tdd/instance/recipes.db')
    cur = con.cursor()

    with open('schema.sql', 'r') as sql_file:
        sql_script = sql_file.read()

    cur.executescript(sql_script)
    con.commit()
    con.close()


init_db()
print('Init-db : success')
