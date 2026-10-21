from models.pedido_model import PedidoModel
from models.detalle_pedido_model import DetallePedidoModel
from models.cliente_model import ClienteModel

class PedidoController:
    """Controlador para gestionar la lógica de Pedidos y sus DetallePedido."""

    @staticmethod
    def crear_pedido_completo(id_cliente, lista_productos):
        """
        Crea un pedido e inserta múltiples detalles.
        lista_productos debe ser una lista de diccionarios:
        [{"id_producto": 1, "cantidad": 2, "precio_unitario": 1000.0}, ...]
        """
        cliente = ClienteModel.obtener_por_id(id_cliente)
        if not cliente:
            return {"exito": False, "mensaje": f"El cliente con ID {id_cliente} no existe."}

        if not lista_productos:
            return {"exito": False, "mensaje": "El pedido debe contener al menos un producto."}

        # 1. Crear la cabecera del pedido
        id_pedido = PedidoModel.crear(id_cliente)
        if not id_pedido:
            return {"exito": False, "mensaje": "Error al registrar la cabecera del pedido."}

        # 2. Insertar los items en detalle_pedido
        detalles_creados = []
        for prod in lista_productos:
            id_detalle = DetallePedidoModel.crear(
                id_pedido=id_pedido,
                id_producto=prod["id_producto"],
                cantidad=prod["cantidad"],
                precio_unitario=prod["precio_unitario"]
            )
            detalles_creados.append(id_detalle)

        return {
            "exito": True,
            "mensaje": "Pedido realizado con éxito.",
            "id_pedido": id_pedido,
            "items_procesados": len(detalles_creados)
        }

    @staticmethod
    def listar_pedidos():
        pedidos = PedidoModel.obtener_todos()
        return {"exito": True, "datos": pedidos}

    @staticmethod
    def obtener_detalle_pedido(id_pedido):
        pedido = PedidoModel.obtener_por_id(id_pedido)
        if not pedido:
            return {"exito": False, "mensaje": f"El pedido con ID {id_pedido} no existe."}

        items = DetallePedidoModel.obtener_por_pedido(id_pedido)
        return {
            "exito": True,
            "pedido": pedido,
            "detalles": items
        }

    @staticmethod
    def eliminar_pedido(id_pedido):
        eliminado = PedidoModel.eliminar(id_pedido)
        if eliminado:
            return {"exito": True, "mensaje": "Pedido y sus detalles eliminados correctamente."}
        return {"exito": False, "mensaje": "No se pudo eliminar el pedido."}