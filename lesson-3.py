# Commands SELECT and INSERT

import sqlite3 as sq

with sq.connect("SQLite-lessons.db") as con:
    cur = con.cursor()
    # cur.execute("DROP TABLE IF EXISTS lesson_3")
    cur.execute("""CREATE TABLE IF NOT EXISTS lesson_3 (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER,
        score INTEGER
        )""")

    # cur.execute("""INSERT INTO lesson_2 (name, old, score) VALUES('qweqwe', 123, 235)""")
    cur.execute("SELECT * FROM lesson_3")

    # lst_res = cur.fetchall()
    # print(lst_res)

    size_res = cur.fetchmany(7)
    print(size_res)

    first_res = cur.fetchone()
    print(first_res)
