import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Coloca tu contraseña de MySQL aquí
        database="tienda_online"
    )
    return connection