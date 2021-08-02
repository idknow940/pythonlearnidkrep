import sqlite3
from sqlite3 import Error
from pprint import pprint
import os
import sys

database = os.path.join(os.getcwd(), "databases", "game.db")
try:
    conn = sqlite3.connect(database)
except Error as e:
    print(e)
    sys.exit()


class Book:
    try:
        def __init__(self, name, author, date, rate, connection):
            self.name = name
            self.author = author
            self.date = date
            self.rate = rate
            self.connection = connection
            self.curs = connection.cursor()
    except Exception as e:
        print(e)

    def add_book(self):
        utc = """CREATE TABLE IF NOT EXISTS books(
                            id int PRIMARY KEY NOT NULL,
                            name text,
                            author text,
                            date text,
                            rate real
                        );"""
        
        iq = """INSERT INTO books(name, author, date, rate)
                        VALUES(?, ?, ?, ?)
                            """
        # self.curs.execute(utc)
        self.curs.execute(iq, (str(self.name), str(self.author), str(self.date), str(self.rate)))
        
        self.connection.commit()

    def remove_book(self):
        iq = """INSERT INTO books(name, author, date, rate)
                        VALUES(null, null, null, null)
                        """
        self.curs.execute(iq)
        self.connection.commit()


book1 = Book("main", "Python", "1980", 10.0, conn)
# book1.add_book()
# book1.remove_book()
