# Methods execute, executemany, executescript, commit, rollback
# BEGIN;

import random
import sqlite3 as sq

# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#
#     cur.execute("DROP TABLE IF EXISTS cars ")
#     cur.execute("""CREATE TABLE IF NOT EXISTS cars (
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )""")
#
#     # 1. execute
#     cur.execute("INSERT INTO cars VALUES(1,'Audi',52642)")
#     cur.execute("INSERT INTO cars VALUES(2,'Mercedes',57127)")
#     cur.execute("INSERT INTO cars VALUES(3,'Skoda',9000)")
#     cur.execute("INSERT INTO cars VALUES(4,'Volvo',29000)")
#     cur.execute("INSERT INTO cars VALUES(5,'Bentley',350000)")
#
#     # 2. commit and close
#     # con.commit() – применение всех изменений в таблицах БД;
#     # con.close() – закрытие соединения с БД.
#
#     # 3. executemany
#     cars = [
#         ('Audi', 52642),
#         ('Mercedes', 57127),
#         ('Skoda', 9000),
#         ('Volvo', 29000),
#         ('Bentley', 350000)
#     ]
#
#     cur.executemany("INSERT INTO cars VALUES(NULL,?,?)", cars)
#     # or
#     for car in cars:
#         cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)
#
#     # 4. executescript
#     cur.executescript("""DELETE FROM cars WHERE model LIKE 'A%';
#         UPDATE cars SET price = price+1000
#     """)


# 5. commit, rollback and BEGIN;
# con = None
# try:
#     con = sq.connect("cars.db")
#     cur = con.cursor()
#
#     cur.executescript("""CREATE TABLE IF NOT EXISTS cars (
#             car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             model TEXT,
#             price INTEGER
#         );
#         BEGIN;
#         INSERT INTO cars VALUES(NULL,'Audi',52642);
#         INSERT INTO cars VALUES(NULL,'Mercedes',57127);
#         INSERT INTO cars VALUES(NULL,'Skoda',9000);
#         INSERT INTO cars VALUES(NULL,'Volvo',29000);
#         INSERT INTO cars VALUES(NULL,'Bentley',350000);
#         UPDATE cars SET price = price+1000
#     """)
#     con.commit()
#
# except sq.Error as e:
#     if con:
#         con.rollback()
#     print("Runtime error")
# finally:
#     if con:
#         con.close()


# 6. isolation_level=None - instant save to sql
# it's slows down program (better cur.commit() at the end of the file)

# with sq.connect("cars.db", isolation_level=None) as con:
#     cur = con.cursor()
#
#     cur.executescript("""INSERT INTO cars VALUES(NULL,'Audi',52642);
#         INSERT INTO cars VALUES(NULL,'Mercedes',57127);
#         INSERT INTO cars VALUES(NULL,'Skoda',9000);
#         INSERT INTO cars VALUES(NULL,'Volvo',29000);
#         INSERT INTO cars VALUES(NULL,'Bentley',350000);
#     """)


# 7.
with sq.connect("cars.db") as con:
    cur = con.cursor()

    cur.executescript("""CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            price INTEGER
        );
        CREATE TABLE IF NOT EXISTS cust(name TEXT, tr_in INTEGER, buy INTEGER);        
    """)

    cur.execute("INSERT INTO cars VALUES(NULL,'car-1', 1000)")
    last_row_id = cur.lastrowid
    buy_car_id = 2
    cur.execute("INSERT INTO cust VALUES('car-2', ?, ?)", (last_row_id, buy_car_id))
