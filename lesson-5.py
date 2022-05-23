# Aggregation and grouping GROUP BY

# Aggregation functions:
# count() – подсчет числа записей;
# sum() – подсчет суммы указанного поля по всем записям выборки;
# avr() – вычисление среднего арифметического указанного поля;
# min() – нахождение минимального значения для указанного поля;
# max() – нахождение максимального значения для указанного поля.

import sqlite3 as sq

with sq.connect("SQLite-lessons.db") as con:
    cur = con.cursor()
    # cur.execute("DROP TABLE IF EXISTS lesson_5")
    cur.execute("""CREATE TABLE IF NOT EXISTS lesson_5 (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            sex INTEGER NOT NULL DEFAULT 1,
            old INTEGER
            )""")

    cur.execute("INSERT INTO lesson_5 (name, sex, old) VALUES (\"Anne\", 2, 19)")
