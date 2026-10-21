from models.producto_model import ProductoModel

class ProductoController:
    """Controlador para gestionar la lógica de negocio de Productos."""

    @staticmethod
    def crear_producto(nombre, precio, stock):
        if not nombre or precio < 0 or stock < 0:
            return {"exito": False, "mensaje": "Datos inválidos (precio y stock deben ser valores positivos)."}

        id_creado = ProductoModel.crear(nombre, precio, stock)
        if id_creado:
            return {"exito": True, "mensaje": "Producto creado con éxito.", "id_producto": id_creado}
        return {"exito": False, "mensaje": "Error al registrar el producto."}

    @staticmethod
    def listar_productos():
        productos = ProductoModel.obtener_todos()
        return {"exito": True, "datos": productos}

    @staticmethod
    def actualizar_producto(id_producto, nombre, precio, stock):
        if not id_producto or not nombre or precio < 0 or stock < 0:
            return {"exito": False, "mensaje": "Datos incompletos o valores numéricos no válidos."}

        actualizado = ProductoModel.actualizar(id_producto, nombre, precio, stock)
        if actualizado:
            return {"exito": True, "mensaje": "Producto actualizado correctamente."}
        return {"exito": False, "mensaje": "No se pudo actualizar el producto."}

    @staticmethod
    def eliminar_producto(id_producto):
        eliminado = ProductoModel.eliminar(id_producto)
        if eliminado:
            return {"exito": True, "mensaje": "Producto eliminado con éxito."}
        return {"exito": False, "mensaje": "No se pudo eliminar el producto."}