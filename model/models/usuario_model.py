import mysql.connector

class UsuarioModel:
    def __init__(self):
        # Configuración de conexión a la base de datos MySQL
        self.config = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': 'mi_base_de_datos'
        }

    def _get_connection(self):
        return mysql.connector.connect(**self.config)

    # 1. CREAR (Create)
    def crear(self, nombre, email):
        conn = self._get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)"
        cursor.execute(query, (nombre, email))
        conn.commit()
        cursor.close()
        conn.close()

    # 2. LEER TODOS (Read)
    def obtener_todos(self):
        conn = self._get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM usuarios ORDER BY id DESC"
        cursor.execute(query)
        usuarios = cursor.fetchall()
        cursor.close()
        conn.close()
        return usuarios

    # LEER UNO POR ID
    def obtener_por_id(self, id):
        conn = self._get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM usuarios WHERE id = %s"
        cursor.execute(query, (id,))
        usuario = cursor.fetchone()
        cursor.close()
        conn.close()
        return usuario

    # 3. ACTUALIZAR (Update)
    def actualizar(self, id, nombre, email):
        conn = self._get_connection()
        cursor = conn.cursor()
        query = "UPDATE usuarios SET nombre = %s, email = %s WHERE id = %s"
        cursor.execute(query, (nombre, email, id))
        conn.commit()
        cursor.close()
        conn.close()

    # 4. BORRAR (Delete)
    def eliminar(self, id):
        conn = self._get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM usuarios WHERE id = %s"
        cursor.execute(query, (id,))
        conn.commit()
        cursor.close()
        conn.close()