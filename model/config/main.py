from models.cliente_model import ClienteModel
from models.producto_model import ProductoModel
from models.pedido_model import PedidoModel
from models.detalle_pedido_model import DetallePedidoModel

# 1. Crear o seleccionar un pedido para el cliente con ID 1
id_pedido = PedidoModel.crear(id_cliente=1)
print(f"Nuevo pedido creado con ID: {id_pedido}")

# 2. Agregar un producto (ID 1) al detalle de ese pedido
id_detalle = DetallePedidoModel.crear(
    id_pedido=id_pedido,
    id_producto=1,
    cantidad=3,
    precio_unitario=2500.00
)
print(f"Detalle agregado con ID: {id_detalle}")

# 3. Consultar todos los pedidos con sus detalles
pedidos = PedidoModel.obtener_todos()
print("\n--- PEDIDOS REGISTRADOS ---")
for p in pedidos:
    print(f"Pedido #{p['id_pedido']} - Cliente: {p['cliente_nombre']} - Fecha: {p['fecha']}")
    detalles = DetallePedidoModel.obtener_por_pedido(p['id_pedido'])
    for d in detalles:
        print(f"   -> Producto: {d['producto_nombre']} | Cantidad: {d['cantidad']} | Precio: ${d['precio_unitario']}")