from models.detalle_pedido_model import DetallePedidoModel
from models.pedido_model import PedidoModel

class DetallePedidoController:
    """Controlador para la gestión individual de los ítems de un pedido."""

    @staticmethod
    def agregar_item(id_pedido, id_producto, cantidad, precio_unitario):
        """Agrega un ítem individual a un pedido existente."""
        if not id_pedido or not id_producto:
            return {"exito": False, "mensaje": "El ID de pedido y producto son obligatorios."}
        
        if cantidad <= 0 or precio_unitario < 0:
            return {"exito": False, "mensaje": "La cantidad debe ser mayor a 0 y el precio no puede ser negativo."}

        # Validar existencia del pedido antes de insertar
        pedido = PedidoModel.obtener_por_id(id_pedido)
        if not pedido:
            return {"exito": False, "mensaje": f"El pedido con ID {id_pedido} no existe."}

        id_detalle = DetallePedidoModel.crear(id_pedido, id_producto, cantidad, precio_unitario)
        if id_detalle:
            return {"exito": True, "mensaje": "Ítem agregado al pedido con éxito.", "id_detalle": id_detalle}
        return {"exito": False, "mensaje": "Error al registrar el ítem en el detalle."}

    @staticmethod
    def listar_por_pedido(id_pedido):
        """Obtiene la lista de ítems asociados a un pedido específico."""
        if not id_pedido:
            return {"exito": False, "mensaje": "Se requiere el ID del pedido."}

        items = DetallePedidoModel.obtener_por_pedido(id_pedido)
        return {"exito": True, "datos": items}

    @staticmethod
    def actualizar_item(id_detalle, cantidad, precio_unitario):
        """Modifica la cantidad o precio de un ítem de detalle existente."""
        if not id_detalle:
            return {"exito": False, "mensaje": "El ID del detalle es obligatorio."}

        if cantidad <= 0 or precio_unitario < 0:
            return {"exito": False, "mensaje": "La cantidad debe ser mayor a 0 y el precio no puede ser negativo."}

        actualizado = DetallePedidoModel.actualizar(id_detalle, cantidad, precio_unitario)
        if actualizado:
            return {"exito": True, "mensaje": "Ítem actualizado correctamente."}
        return {"exito": False, "mensaje": "No se pudo actualizar el ítem (verifique si el ID de detalle existe)."}

    @staticmethod
    def eliminar_item(id_detalle):
        """Elimina un ítem específico del detalle del pedido."""
        if not id_detalle:
            return {"exito": False, "mensaje": "El ID del detalle es obligatorio."}

        eliminado = DetallePedidoModel.eliminar(id_detalle)
        if eliminado:
            return {"exito": True, "mensaje": "Ítem eliminado correctamente del pedido."}
        return {"exito": False, "mensaje": "No se pudo eliminar el ítem."}