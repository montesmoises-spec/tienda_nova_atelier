from flask import Blueprint, render_template, request, redirect, url_for
from models.detalle_pedido_model import DetallePedidoModel

# Definición del Blueprint para Detalle de Pedido
detalle_pedido_bp = Blueprint('detalle_pedido', __name__, url_prefix='/detalle_pedido')

# 1. RUTA: Listar ítems de un pedido específico
@detalle_pedido_bp.route('/pedido/<int:id_pedido>')
def obtener_por_pedido(id_pedido):
    detalles = DetallePedidoModel.obtener_por_pedido(id_pedido)
    return render_template('detalle_pedido/index.html', detalles=detalles, id_pedido=id_pedido)

# 2. RUTA: Agregar un ítem al detalle del pedido
@detalle_pedido_bp.route('/crear/<int:id_pedido>', methods=['GET', 'POST'])
def crear(id_pedido):
    if request.method == 'POST':
        id_producto = request.form['id_producto']
        cantidad = request.form['cantidad']
        precio_unitario = request.form['precio_unitario']
        
        # Guardar en la base de datos
        DetallePedidoModel.crear(id_pedido, id_producto, cantidad, precio_unitario)
        return redirect(url_for('detalle_pedido.obtener_por_pedido', id_pedido=id_pedido))
    
    return render_template('detalle_pedido/crear.html', id_pedido=id_pedido)

# 3. RUTA: Actualizar cantidad o precio de un ítem
@detalle_pedido_bp.route('/editar/<int:id_detalle>/<int:id_pedido>', methods=['GET', 'POST'])
def editar(id_detalle, id_pedido):
    if request.method == 'POST':
        cantidad = request.form['cantidad']
        precio_unitario = request.form['precio_unitario']
        
        DetallePedidoModel.actualizar(id_detalle, cantidad, precio_unitario)
        return redirect(url_for('detalle_pedido.obtener_por_pedido', id_pedido=id_pedido))
    
    return render_template('detalle_pedido/editar.html', id_detalle=id_detalle, id_pedido=id_pedido)

# 4. RUTA: Eliminar un ítem del detalle
@detalle_pedido_bp.route('/eliminar/<int:id_detalle>/<int:id_pedido>')
def eliminar(id_detalle, id_pedido):
    DetallePedidoModel.eliminar(id_detalle)
    return redirect(url_for('detalle_pedido.obtener_por_pedido', id_pedido=id_pedido))