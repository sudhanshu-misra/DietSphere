import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="dietsphere_user",
        password="diet123",
        database="dietsphere"
    )