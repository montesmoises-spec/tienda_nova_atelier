from config.conexion import obtener_conexion

class ProductoModel:
    """Clase dedicada exclusivamente a ejecutar sentencias SQL para la tabla 'producto'."""

    @staticmethod
    def crear(nombre, precio, stock):
        """CREATE: Inserta un nuevo producto."""
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            sql = "INSERT INTO producto (nombre, precio, stock) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nombre, precio, stock))
            conexion.commit()
            nuevo_id = cursor.lastrowid
            cursor.close()
            conexion.close()
            return nuevo_id
        return None

    @staticmethod
    def obtener_todos():
        """READ: Obtiene todos los productos."""
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            sql = "SELECT * FROM producto"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            cursor.close()
            conexion.close()
            return resultados
        return []

    @staticmethod
    def actualizar(id_producto, nombre, precio, stock):
        """UPDATE: Actualiza los datos de un producto."""
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            sql = "UPDATE producto SET nombre = %s, precio = %s, stock = %s WHERE id_producto = %s"
            cursor.execute(sql, (nombre, precio, stock, id_producto))
            conexion.commit()
            filas_afectadas = cursor.rowcount
            cursor.close()
            conexion.close()
            return filas_afectadas > 0
        return False

    @staticmethod
    def eliminar(id_producto):
        """DELETE: Elimina un producto por su ID."""
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            sql = "DELETE FROM producto WHERE id_producto = %s"
            cursor.execute(sql, (id_producto,))
            conexion.commit()
            filas_afectadas = cursor.rowcount
            cursor.close()
            conexion.close()
            return filas_afectadas > 0
        return False