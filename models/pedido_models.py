from config.conexion import obtener_conexion

class PedidoModel:
    """Modelo adaptado para PedidoController."""

    @staticmethod
    def crear(id_cliente):
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