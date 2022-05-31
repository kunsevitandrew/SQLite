# Methods fetchall, fetchmany, fetchone, iterdump
# fetchall() – возвращает число записей в виде упорядоченного списка;
# fetchmany(size) – возвращает число записей не более size;
# fetchone() – возвращает первую запись.

import sqlite3 as sq

cars = [
    ('Audi', 52642),
    ('Mercedes', 57127),
    ('Skoda', 9000),
    ('Volvo', 29000),
    ('Bentley', 350000)
]

# with sq.connect("cars.db") as con:
#     # con.row_factory = sq.Row
#     cur = con.cursor()
#
#     cur.executescript("""CREATE TABLE IF NOT EXISTS cars (
#             car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             model TEXT,
#             price INTEGER)
#     """)
#
#     cur.executemany("INSERT INTO cars VALUES(NULL,?, ?)", cars)
#
#     # 1. fetchall
#     rows = cur.fetchall()
#     print(rows)
#     # -- [('Audi', 52642), ('Mercedes', 57127), ('Skoda', 9000), ('Volvo', 29000), ('Bentley', 350000)]
#
#     # 2. fetchone
#     row = cur.fetchone()
#     print(row)
#     # -- ('Audi', 52642)
#
#     # 3. fetchmany
#     size = 3
#     rows = cur.fetchmany(size)
#     print(rows)
#     # -- [('Audi', 52642), ('Mercedes', 57127), ('Skoda', 9000)]
#
#     # 4.
#     for result in cur:
#         print(result)
#
#     # 5. Row
#     print(result['model'], result['price'])
#
#     # Storage images in db (BLOB)
#     cur.executescript("""CREATE TABLE IF NOT EXISTS users (
#         name TEXT,
#         ava BLOB,
#         score INTEGER)
#     """)


# Backup db
with sq.connect("cars.db") as con:
    cur = con.cursor()

    for sql in con.iterdump():
        print(sql)

# Create an in-memory database
data = [("car", "машина"), ("house", "дом"), ("tree", "дерево"), ("color", "цвет")]

con = sq.connect(':memory:')
with con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS dict(
        eng TEXT, rus TEXT    
    )""")

    cur.executemany("INSERT INTO dict VALUES(?,?)", data)

    cur.execute("SELECT rus FROM dict WHERE eng LIKE 'c%'")
    print(cur.fetchall())
