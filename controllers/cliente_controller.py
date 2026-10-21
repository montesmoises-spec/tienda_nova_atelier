from models.cliente_model import ClienteModel

class ClienteController:
    """Controlador para gestionar la lógica de negocio de Clientes."""

    @staticmethod
    def crear_cliente(nombre, email, telefono):
        if not nombre or not email:
            return {"exito": False, "mensaje": "El nombre y el email son obligatorios."}
        
        id_creado = ClienteModel.crear(nombre, email, telefono)
        if id_creado:
            return {"exito": True, "mensaje": "Cliente creado correctamente.", "id_cliente": id_creado}
        return {"exito": False, "mensaje": "Error al intentar registrar el cliente."}

    @staticmethod
    def listar_clientes():
        clientes = ClienteModel.obtener_todos()
        return {"exito": True, "datos": clientes}

    @staticmethod
    def obtener_cliente(id_cliente):
        cliente = ClienteModel.obtener_por_id(id_cliente)
        if cliente:
            return {"exito": True, "datos": cliente}
        return {"exito": False, "mensaje": f"No se encontró el cliente con ID {id_cliente}."}

    @staticmethod
    def actualizar_cliente(id_cliente, nombre, email, telefono):
        if not id_cliente or not nombre or not email:
            return {"exito": False, "mensaje": "El ID, nombre y email son obligatorios."}
        
        actualizado = ClienteModel.actualizar(id_cliente, nombre, email, telefono)
        if actualizado:
            return {"exito": True, "mensaje": "Cliente actualizado correctamente."}
        return {"exito": False, "mensaje": "No se pudo actualizar el cliente (verifique si el ID existe)."}

    @staticmethod
    def eliminar_cliente(id_cliente):
        eliminado = ClienteModel.eliminar(id_cliente)
        if eliminado:
            return {"exito": True, "mensaje": "Cliente eliminado correctamente."}
        return {"exito": False, "mensaje": "No se pudo eliminar el cliente."}