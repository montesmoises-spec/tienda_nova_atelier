import mysql.connector

def obtener_conexion():
    """Establece y retorna la conexión con la base de datos MySQL."""
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="tienda_online" # BD definida en el SQL[cite: 2]
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al conectar con la base de datos: {err}")
        return None