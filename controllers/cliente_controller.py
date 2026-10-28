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
        email = request.form['email']
        telefono = request.form['telefono']
        crear_cliente(nombre, email, telefono)
        return redirect(url_for('cliente.index'))
    return render_template('cliente/crear.html')

@cliente_bp.route('/editar/<int:id_cliente>', methods=['GET', 'POST'])
def editar(id_cliente):
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']
        actualizar_cliente(id_cliente, nombre, email, telefono)
        return redirect(url_for('cliente.index'))
    
    cliente = obtener_cliente_por_id(id_cliente)
    return render_template('cliente/editar.html', cliente=cliente)

@cliente_bp.route('/eliminar/<int:id_cliente>', methods=['POST'])
def eliminar(id_cliente):
    eliminar_cliente(id_cliente)
    return redirect(url_for('cliente.index'))