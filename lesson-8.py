# Nested SQL queries
import random
import sqlite3 as sq

with sq.connect("SQLite-lessons.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS lesson_8 (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            col_0 TEXT NOT NULL,
            col_1 INTEGER NOT NULL DEFAULT 1,
            col_2 INTEGER
            )""")

    # for generate random row
    name1 = "name-1"
    name2 = "name-2"
    cur.execute(
        f"INSERT INTO lesson_8 (col_0, col_1, col_2) VALUES (\" {name1 if random.randint(1, 100) > 50 else name2} \", {random.random()}, {random.randint(1, 100)})")
