import sqlite3


def init_db():
    con = sqlite3.connect('recipe.db')
    cur = con.cursor()

    with open('schema.sql', 'r') as sql_file:
        sql_script = sql_file.read()

    cur.executescript(sql_script)
    con.commit()
    con.close()


init_db()
print('Init-db : success')
