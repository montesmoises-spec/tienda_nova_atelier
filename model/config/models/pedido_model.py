from config.conexion import obtener_conexion

class PedidoModel:
    """Clase dedicada a ejecutar sentencias SQL para la tabla 'pedido'."""

    @staticmethod
    def crear(id_cliente):
        """CREATE: Crea un nuevo registro de pedido asociado a un cliente."""
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            sql = "INSERT INTO pedido (id_cliente) VALUES (%s)"
            cursor.execute(sql, (id_cliente,))
            conexion.commit()
            nuevo_id = cursor.lastrowid
            cursor.close()
            conexion.close()
            return nuevo_id
        return None

    @staticmethod
    def obtener_todos():
        """READ: Obtiene todos los pedidos con información del cliente."""
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            sql = """
                SELECT p.id_pedido, p.fecha, c.id_cliente, c.nombre AS cliente_nombre, c.email
                FROM pedido p
                INNER JOIN clientes c ON p.id_cliente = c.id_cliente
            """
            cursor.execute(sql)
            resultados = cursor.fetchall()
            cursor.close()
            conexion.close()
            return resultados
        return []

    @staticmethod
    def obtener_por_id(id_pedido):
        """READ: Obtiene un pedido específico por ID."""
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            sql = "SELECT * FROM pedido WHERE id_pedido = %s"
            cursor.execute(sql, (id_pedido,))
            resultado = cursor.fetchone()
            cursor.close()
            conexion.close()
            return resultado
        return None

    @staticmethod
    def eliminar(id_pedido):
        """DELETE: Elimina un pedido por su ID (las FK eliminan sus detalles por CASCADE)."""
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            sql = "DELETE FROM pedido WHERE id_pedido = %s"
            cursor.execute(sql, (id_pedido,))
            conexion.commit()
            filas_afectadas = cursor.rowcount
            cursor.close()
            conexion.close()
            return filas_afectadas > 0
        return False