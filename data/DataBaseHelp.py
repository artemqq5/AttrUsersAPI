import os

import pymysql
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", "venv", ".env"))


class DataBaseHelp:

    def __init__(self):
        self.__connection = pymysql.connect(
            host="localhost",
            user="root",
            password=os.getenv("DATABASE_PASSWORD"),
            db=os.getenv("DATABASE_NAME"),
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def _select_one(self, query, args=None):
        try:
            with self.__connection as con:
                with con.cursor() as cursor:
                    cursor.execute(query, args)
                    return cursor.fetchone()
        except Exception as e:
            print(f"_select_one ({query}) ({args}): {e}")

    def _select(self, query, args=None):
        try:
            with self.__connection as con:
                with con.cursor() as cursor:
                    cursor.execute(query, args)
                    return cursor.fetchall()
        except Exception as e:
            print(f"_select ({query}) ({args}): {e}")

    def _insert(self, query, args=None):
        try:
            with self.__connection as con:
                with con.cursor() as cursor:
                    return cursor.execute(query, args)
        except Exception as e:
            print(f"_insert ({query}) ({args}): {e}")


