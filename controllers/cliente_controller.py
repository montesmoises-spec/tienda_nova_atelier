from flask import Blueprint, render_template, request, redirect, url_for
from models.cliente_models import *

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/')
def index():
    clientes = obtener_clientes()
    return render_template('cliente/index.html', clientes=clientes)

@cliente_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        crear_producto(nombre, precio, stock)
        return redirect(url_for('producto.index'))
    return render_template('producto/crear.html')

@cliente_bp.route('/editar/<int:id_producto>', methods=['GET', 'POST'])
def editar(id_producto):
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        actualizar_producto(id_producto, nombre, precio, stock)
        return redirect(url_for('producto.index'))
    
    producto = obtener_producto_por_id(id_producto)
    return render_template('producto/editar.html', producto=producto)

@cliente_bp.route('/eliminar/<int:id_producto>', methods=['POST'])
def eliminar(id_producto):
    eliminar_producto(id_producto)
    return redirect(url_for('producto.index'))