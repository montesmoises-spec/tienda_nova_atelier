from config import get_db_connection

def obtener_productos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM producto")
    productos = cursor.fetchall()
    cursor.close()
    conn.close()
    return productos

def obtener_producto_por_id(id_producto):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM producto WHERE id_producto = %s", (id_producto,))
    producto = cursor.fetchone()
    cursor.close()
    conn.close()
    return producto

def crear_producto(nombre, precio, stock):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO producto (nombre, precio, stock) VALUES (%s, %s, %s)",
        (nombre, precio, stock)
    )
    conn.commit()
    cursor.close()
    conn.close()

def actualizar_producto(id_producto, nombre, precio, stock):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE producto SET nombre = %s, precio = %s, stock = %s WHERE id_producto = %s",
        (nombre, precio, stock, id_producto)
    )
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_producto(id_producto):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM producto WHERE id_producto = %s", (id_producto,))
    conn.commit()
    cursor.close()
    conn.close()