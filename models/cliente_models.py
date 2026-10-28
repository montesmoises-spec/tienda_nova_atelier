from config import get_db_connection

def obtener_clientes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    cursor.close()
    conn.close()
    return clientes

def obtener_cliente_por_id(id_cliente):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes WHERE id_cliente = %s", (id_cliente,))
    cliente = cursor.fetchone()
    cursor.close()
    conn.close()
    return cliente

def crear_cliente(nombre, email, telefono):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO clientes (nombre, email, telefono) VALUES (%s, %s, %s)",
        (nombre, email, telefono)
    )
    conn.commit()
    cursor.close()
    conn.close()

def actualizar_cliente(id_cliente, nombre, email, telefono):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE clientes SET nombre = %s, email = %s, telefono = %s WHERE id_cliente = %s",
        (nombre, email, telefono, id_cliente)
    )
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_cliente(id_cliente):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id_cliente = %s", (id_cliente,))
    conn.commit()
    cursor.close()
    conn.close()