import mysql.connector

from configs.config import dbconfig


class user_model:
    # connection establishment with database
    def __init__(self):
        try:
            self.con = mysql.connector.connect(
                host=dbconfig["host"],
                port=dbconfig["port"],
                user=dbconfig["username"],
                password=dbconfig["password"],
                database=dbconfig["database"],
            )
            self.con.autocommit = True
            print("connection established")
        except Exception as e:
            print(f"Error connecting to database: {e}")

    def user_getall_model(self):
        cursor = self.con.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users_table")
        result = cursor.fetchall()
        cursor.close()
        return result
