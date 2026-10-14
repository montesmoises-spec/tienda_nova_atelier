from models.cliente_model import ClienteModel
from models.producto_model import ProductoModel

# --- PROBAR CREACIÓN (CREATE) ---
id_nuevo = ClienteModel.crear("Juan Perez", "juan@email.com", "+56 9 1111 2222")
print(f"Cliente creado con ID: {id_nuevo}")

# --- PROBAR LECTURA (READ) ---
print("\nLista de Clientes:")
clientes = ClienteModel.obtener_todos()
for c in clientes:
    print(c)

# --- PROBAR ACTUALIZACIÓN (UPDATE) ---
exito_act = ClienteModel.actualizar(1, "Pedro Actualizado", "pedro_nuevo@email.com", "+56 9 4675 3456")
print(f"\n¿Cliente actualizado?: {exito_act}")

# --- PROBAR ELIMINACIÓN (DELETE) ---
# exito_del = ClienteModel.eliminar(2)
# print(f"¿Cliente eliminado?: {exito_del}")