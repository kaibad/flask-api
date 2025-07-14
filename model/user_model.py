import mysql.connector
from flask import make_response

from configs.config import dbconfig


class UserModel:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host=dbconfig["host"],
                port=dbconfig["port"],
                user=dbconfig["username"],
                password=dbconfig["password"],
                database=dbconfig["database"],
            )
            self.conn.autocommit = True
            print("Connection established")
        except Exception as e:
            print(f"Error connecting to database: {e}")
            self.conn = None

    # Get method
    def user_getall_model(self):
        if not self.conn:
            return {"error": "Database connection not established."}

        try:
            # it is better to create a cursor where or when we need beacase the persistent cursor (self.cursor) in __init__, which is not ideal and can cause Memory leaks. and Locked resources if not properly closed.
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users_table")
            result = cursor.fetchall()
            cursor.close()

            if result:
                return make_response({"users": result}, 200)
            else:
                return make_response({"message": "No Data Found"}, 204)
        except Exception as e:
            return make_response({"error": str(e)}, 500)

    # post method
    def user_signup_model(self, data):
        try:
            cursor = self.conn.cursor()
            query = "INSERT INTO users_table (name, email, phone, role, password) VALUES (%s, %s, %s, %s, %s)"
            values = (
                data["name"],
                data["email"],
                data["phone"],
                data["role"],
                data["password"],
            )
            cursor.execute(query, values)
            cursor.close()
            return make_response({"message": "User created successfully"}, 201)
        except Exception as e:
            return make_response({"error": str(e)}, 500)

    # PUT method
    def user_updateprofile_model(self, data):
        try:
            cursor = self.conn.cursor()
            # Use %s to prevent SQL injection and keep your app secure — never directly inject strings using f"" or "{}" in SQL.
            query = """
                UPDATE users_table
                SET name = %s, email = %s, phone = %s, role = %s, password = %s
                WHERE id = %s
            """
            # Triple quotes in Python (""" ... """ or ''' ... ''') are used for multi-line strings.
            values = (
                data["name"],
                data["email"],
                data["phone"],
                data["role"],
                data["password"],
                data["id"],
            )
            cursor.execute(query, values)
            affected_rows = cursor.rowcount
            cursor.close()
            if affected_rows > 0:
                return make_response({"message": "User updated successfully"}, 201)
            else:
                return make_response(
                    {"message": "Nothing to update or user not found"}, 202
                )
        except Exception as e:
            return make_response({"error": str(e)}, 500)

    # DELETE method
    def user_deleteprofile_model(self, id):
        try:
            cursor = self.conn.cursor()
            query = " DELETE FROM users_table WHERE ID = %s "

            values = (id,)
            cursor.execute(query, values)
            affected_rows = cursor.rowcount
            cursor.close()
            if affected_rows > 0:
                return make_response({"message": "User Deleted successfully"}, 200)
            else:
                return make_response(
                    {"message": "Nothing to delete or user not found"}, 202
                )

        except Exception as e:
            return make_response({"error": str(e)}, 500)
