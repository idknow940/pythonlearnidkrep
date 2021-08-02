import sqlite3
from sqlite3 import Error
from pprint import pprint
import os
import sys

database = os.path.join(os.getcwd(), 'databases', "game.db")
print(database)
try:
    conn = sqlite3.connect(database)
except Error as e:
    print(e)
    sys.exit()

curs = conn.cursor()

# user_table_create = """CREATE TABLE IF NOT EXISTS users (
#                                         id integer PRIMARY KEY,
#                                         name text NOT NULL,
#                                         username text NOT NULL,
#                                         password text NOT NULL,
#                                         created_at text NOT NULL
#                                     );"""
# curs.execute(user_table_create)
#
# conn.commit()

# query:
# insert_query = """INSERT INTO users (name, username, password, created_at)
#                     VALUES("idk", 'idknow94', 'superstrongpassword', '2021-7-29');
#                 """
#
# curs.execute(insert_query)
# conn.commit()

# update_query = """UPDATE users
#                     SET username = 'johnxxxpro'
#                     WHERE id = 2
#                 """
# with curs:
#     curs.execute(update_query)

username = input("username: ")
password = input("password: ")

curs.execute("SELECT * FROM {} WHERE username='{}' and password='{}'".format("users", username, password))

if curs.fetchone():
    print("Logged in!")
else:
    raise Exception(":|")

result = curs.fetchall()
# result_1 = curs.fetchone()
# result_2 = curs.fetchmany(2)
# print(result)
# print(result_1)
# print(result_2)
# print(type(result))
# print(result[0])
# for i in result:
#     print(i)

# from pprint import pprint
#
# select = """select * from film
#             where title like "%vangers"
#             order by rate desc"""
# result = curs.execute(select)
# pprint(result.fetchall())
# database = os.path.join(os.getcwd(), '..', "film.db")
# # print(database)
# # try:
# #     conn = sqlite3.connect(database)
# # except Error as e:
# #     print(e)
# #     sys.exit()
# #
# # # Creating a cursor to execute commands (queries)
# # curs = conn.cursor()
#
# # lets create a new film for film table
# class Film:
#     def __init__(self, film_id, title, description, release_year: str, rate, length: int, special_features):
#         self.film_id = film_id
#         self.title = title
#         self.description = description
#         self.release_year = release_year
#         self.rate = rate
#         self.length = length
#         self.special_features = special_features
#         self.conn = None
#         self.curs = None
#
#     def connect(self):
#         database = os.path.join(os.getcwd(), '..', "film.db")
#         try:
#             conn = sqlite3.connect(database)
#         except Error as e:
#             print(e)
#             sys.exit()
#         self.conn = conn
#         self.curs = conn.cursor()
#
#     def get_atr_as_tuple(self):
#         return (self.film_id, self.title, self.description, self.release_year, self.rate, self.length,
#         self.special_features)
#
#     def get_atr_as_dict(self):
#         return {
#             'film_id': self.film_id,
#             'title': self.title,
#             'description': self.description,
#             'release_year': self.release_year,
#             'rate': self.rate,
#             'length': self.length,
#             'special_features': self.special_features
#         }
#
#     def insert_function_film(self):
#         insert_query = """INSERT INTO film(film_id, title, description, release_year, rate, length, special_features)
#                             VALUES(?,?,?,?,?,?,?);
#                             """
#         if not self.conn:
#             self.connect()
#
#         curs.execute(insert_query, self.get_atr_as_tuple())
#         conn.commit()
#
#     def remove_from_table(self):
#         if not self.conn:
#             self.connect()
#
#         remove_query = """remove from film
#                             where film_id = 501"""
#
#     def __repr__(self):
#         return self.title
#
#
# #
# desc = """In_a post-apocalyptic wasteland, Max, a drifter and survivor, unwillingly joins Imperator Furiosa,
# 		a rebel warrior, in a quest to overthrow a tyrant who controls the lands water supply."""
# film_1 = Film(501, 'Mad_Max', desc, '2015', 120, 5, 'Action')
# film_2 = Film(601, 'Avangers', 'marvel movie', '2015', 5, 120, 'Action')
# film_3 = Film(701, 'Avangers 2', 'marvel movie', '2015', 5, 120, 'Action')
# # film_1.insert_function_film()
#
# #
# #
# #
#
#
# def insert_function_film_2(value):
# 	insert_query = """INSERT INTO film(film_id, title, description, release_year, rate, length, special_features)
#  	                    VALUES(:film_id,:title,:description,:release_year,:rate,:length,:special_features);
# 	                    """
# 	curs.execute(insert_query, value)
# 	conn.commit()
# insert_function_film(film_2.get_atr_as_tuple())
# insert_function_film_2(film_3.get_atr_as_dict())
