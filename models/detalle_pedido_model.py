from config.conexion import obtener_conexion

class DetallePedidoModel:
    """Clase dedicada a ejecutar sentencias SQL para la tabla 'detalle_pedido'."""

    @staticmethod
    def crear(id_pedido, id_producto, cantidad, precio_unitario):
        """CREATE: Agrega un detalle/ítem a un pedido existente."""
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            sql = """
                INSERT INTO detalle_pedido (id_pedido, id_producto, cantidad, precio_unitario)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (id_pedido, id_producto, cantidad, precio_unitario))
            conexion.commit()
            nuevo_id = cursor.lastrowid
            cursor.close()
            conexion.close()
            return nuevo_id
        return None

    @staticmethod
    def obtener_por_pedido(id_pedido):
        """READ: Obtiene todos los ítems de un pedido específico."""
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            sql = """
                SELECT dp.id_detalle, dp.id_pedido, dp.cantidad, dp.precio_unitario,
                       pr.nombre AS producto_nombre
                FROM detalle_pedido dp
                INNER JOIN producto pr ON dp.id_producto = pr.id_producto
                WHERE dp.id_pedido = %s
            """
            cursor.execute(sql, (id_pedido,))
            resultados = cursor.fetchall()
            cursor.close()
            conexion.close()
            return resultados
        return []

    @staticmethod
    def actualizar(id_detalle, cantidad, precio_unitario):
        """UPDATE: Modifica la cantidad o precio de un detalle de pedido."""
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            sql = """
                UPDATE detalle_pedido 
                SET cantidad = %s, precio_unitario = %s 
                WHERE id_detalle = %s
            """
            cursor.execute(sql, (cantidad, precio_unitario, id_detalle))
            conexion.commit()
            filas_afectadas = cursor.rowcount
            cursor.close()
            conexion.close()
            return filas_afectadas > 0
        return False

    @staticmethod
    def eliminar(id_detalle):
        """DELETE: Elimina un ítem específico del detalle."""
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            sql = "DELETE FROM detalle_pedido WHERE id_detalle = %s"
            cursor.execute(sql, (id_detalle,))
            conexion.commit()
            filas_afectadas = cursor.rowcount
            cursor.close()
            conexion.close()
            return filas_afectadas > 0
        return False