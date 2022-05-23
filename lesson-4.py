# Commands UPDATE and DELETE
# Check SQL file

import sqlite3 as sq


with sq.connect("SQLite-lessons.db") as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS lesson_4")
    cur.execute("""CREATE TABLE IF NOT EXISTS lesson_4 (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER,
        score INTEGER
        )""")
    cur.execute("INSERT INTO lesson_4 (name, sex, old, score) VALUES (\"Anne\", 2, 19, 500)")
