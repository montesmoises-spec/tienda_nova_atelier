from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.cliente_model import obtener_clientes, insertar_cliente # Adapta según las funciones del modelo

cliente_bp = Blueprint('cliente', __name__, url_prefix='/clientes')

@cliente_bp.route('/')
def index():
    clientes = obtener_clientes()
    return render_template('cliente/index.html', clientes=clientes)

@cliente_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        insertar_cliente(nombre)
        flash('Cliente registrado exitosamente', 'success')
        return redirect(url_for('cliente.index'))
    return render_template('cliente/crear.html')