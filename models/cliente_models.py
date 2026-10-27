from config import get_db_connection



def crear(nombre, email, telefono):
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


def obtener_clientes():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM clientes"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultados
    return []


def obtener_por_id(id_cliente):
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


def actualizar(id_cliente, nombre, email, telefono):
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


def eliminar(id_cliente):
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