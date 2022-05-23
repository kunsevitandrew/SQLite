# JOIN operator to generate a summary report

import random
import sqlite3 as sq

with sq.connect("SQLite-lessons.db") as con:
    cur = con.cursor()
    # cur.execute("DROP TABLE IF EXISTS lesson_6")
    cur.execute("""CREATE TABLE IF NOT EXISTS lesson_6 (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            sex INTEGER NOT NULL DEFAULT 1,
            old INTEGER
            )""")

    # for generate random row
    name1 = "name-1"
    name2 = "name-2"
    cur.execute(
        f"INSERT INTO lesson_6 (name, sex, old) VALUES (\" {name1 if random.randint(1, 100) > 50 else name2} \", {random.random()}, {random.randint(1, 100)})")
