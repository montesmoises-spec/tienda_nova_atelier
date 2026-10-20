from config.conexion import obtener_conexion

class ClienteModel:
    """Clase dedicada exclusivamente a ejecutar sentencias SQL para la tabla 'clientes'."""

    @staticmethod
    def crear(nombre, email, telefono):
        """CREATE: Inserta un nuevo cliente."""
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            sql = "INSERT INTO clientes (nombre, email, telefono) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nombre, email, telefono))
            conexion.commit()
            nuevo_id = cursor.lastrowid
            cursor.close()
            conexion.close()
            return nuevo_id
        return None

    @staticmethod
    def obtener_todos():
        """READ: Obtiene todos los clientes."""
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            sql = "SELECT * FROM clientes"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            cursor.close()
            conexion.close()
            return resultados
        return []

    @staticmethod
    def obtener_por_id(id_cliente):
        """READ: Obtiene un cliente por su ID."""
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            sql = "SELECT * FROM clientes WHERE id_cliente = %s"
            cursor.execute(sql, (id_cliente,))
            resultado = cursor.fetchone()
            cursor.close()
            conexion.close()
            return resultado
        return None

    @staticmethod
    def actualizar(id_cliente, nombre, email, telefono):
        """UPDATE: Actualiza los datos de un cliente."""
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            sql = "UPDATE clientes SET nombre = %s, email = %s, telefono = %s WHERE id_cliente = %s"
            cursor.execute(sql, (nombre, email, telefono, id_cliente))
            conexion.commit()
            filas_afectadas = cursor.rowcount
            cursor.close()
            conexion.close()
            return filas_afectadas > 0
        return False

    @staticmethod
    def eliminar(id_cliente):
        """DELETE: Elimina un cliente por su ID."""
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            sql = "DELETE FROM clientes WHERE id_cliente = %s"
            cursor.execute(sql, (id_cliente,))
            conexion.commit()
            filas_afectadas = cursor.rowcount
            cursor.close()
            conexion.close()
            return filas_afectadas > 0
        return False