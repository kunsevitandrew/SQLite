import sqlite3 as sq

# con = sq.connect("andrewK101.db")
# cur = con.cursor()
#
# cur.execute(""" """)
#
# # usually for db use extensions:
# # .db; .db3; .sqlite; .sqlite3
#
# con.close()

# NULL – значение NULL;
# INTEGER – целочисленный тип (занимает от 1 до 8 байт);
# REAL – вещественный тип (8 байт в формате IEEE);
# TEXT – строковый тип (в кодировке данных базы, обычно UTF-8);
# BLOB (двоичные данные, хранятся «как есть», например, для небольших изображений).

with sq.connect("SQLite-lessons.db") as con:
    cur = con.cursor()
    # cur.execute("""CREATE TABLE IF NOT EXISTS name_of_table (
    # name TEXT,
    # sex INTEGER,
    # old INTEGER,
    # score INTEGER
    # )""")

    # PRIMARY KEY, AUTOINCREMENT, NOT NULL и DEFAULT
    cur.execute("DROP TABLE IF EXISTS lesson_2")
    cur.execute("""CREATE TABLE IF NOT EXISTS lesson_2 (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER,
        score INTEGER
    )""")

    # cur.execute("""SELECT * FROM lesson_2""")
    # cur.execute("""SELECT rowid, * FROM lesson_2""")
    # cur.execute("""INSERT INTO lesson_2 (name, old, score) VALUES('Lise', 18, 1000)""")
