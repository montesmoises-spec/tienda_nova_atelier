from flask import Blueprint, render_template, request, redirect, url_for
from models.producto_model import *

producto_bp = Blueprint('producto', __name__)

@producto_bp.route('/')
def index():
    productos = obtener_productos()
    return render_template('producto/index.html', productos=productos)

@producto_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        crear_producto(nombre, precio, stock)
        return redirect(url_for('producto.index'))
    return render_template('producto/crear.html')

@producto_bp.route('/editar/<int:id_producto>', methods=['GET', 'POST'])
def editar(id_producto):
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        actualizar_producto(id_producto, nombre, precio, stock)
        return redirect(url_for('producto.index'))
    
    producto = obtener_producto_por_id(id_producto)
    return render_template('producto/editar.html', producto=producto)

@producto_bp.route('/eliminar/<int:id_producto>', methods=['POST'])
def eliminar(id_producto):
    eliminar_producto(id_producto)
    return redirect(url_for('producto.index'))