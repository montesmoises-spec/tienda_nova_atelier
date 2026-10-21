from flask import Blueprint, render_template, request, redirect, url_for
# Conexión directa con la clase Modelo del Integrante M
from models.cliente_model import ClienteModel

# Definición del Blueprint para la entidad Cliente
cliente_bp = Blueprint('cliente', __name__, url_prefix='/clientes')

# 1. RUTA: Listar todos los clientes
@cliente_bp.route('/')
def index():
    # Llama a ClienteModel.obtener_todos()
    clientes = ClienteModel.obtener_todos()
    return render_template('cliente/index.html', clientes=clientes)

# 2. RUTA: Crear cliente
@cliente_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        # Recibe los datos enviados desde el formulario (Vista)
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']
        
        # Envia los datos a ClienteModel.crear(...)
        ClienteModel.crear(nombre, email, telefono)
        return redirect(url_for('cliente.index'))
    
    return render_template('cliente/crear.html')

# 3. RUTA: Editar cliente
@cliente_bp.route('/editar/<int:id_cliente>', methods=['GET', 'POST'])
def editar(id_cliente):
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']
        
        # Llama a ClienteModel.actualizar(...)
        ClienteModel.actualizar(id_cliente, nombre, email, telefono)
        return redirect(url_for('cliente.index'))
    
    # Si es GET, busca los datos del cliente por id_cliente
    cliente = ClienteModel.obtener_por_id(id_cliente)
    return render_template('cliente/editar.html', cliente=cliente)

# 4. RUTA: Eliminar cliente
@cliente_bp.route('/eliminar/<int:id_cliente>')
def eliminar(id_cliente):
    # Llama a ClienteModel.eliminar(...)
    ClienteModel.eliminar(id_cliente)
    return redirect(url_for('cliente.index'))