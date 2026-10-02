from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.Usuario_Model import UsuarioModel

# Definición del Blueprint para el controlador
usuario_bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')

# 1. LISTAR TODOS
@usuario_bp.route('/', methods=['GET'])
def index():
    lista_usuarios = UsuarioModel.obtener_todos()
    return render_template('usuarios/index.html', usuarios=lista_usuarios)

# 2. MOSTRAR FORMULARIO DE CREACIÓN Y GUARDAR
@usuario_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        
        if nombre and email:
            UsuarioModel.crear(nombre, email)
            flash('Usuario creado con éxito', 'success')
            return redirect(url_for('usuarios.index'))
            
    return render_template('usuarios/crear.html')

# 3. MOSTRAR FORMULARIO DE EDICIÓN Y ACTUALIZAR
@usuario_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        
        UsuarioModel.actualizar(id, nombre, email)
        flash('Usuario actualizado correctamente', 'success')
        return redirect(url_for('usuarios.index'))

    usuario = UsuarioModel.obtener_por_id(id)
    if not usuario:
        flash('Usuario no encontrado', 'danger')
        return redirect(url_for('usuarios.index'))

    return render_template('usuarios/editar.html', usuario=usuario)

# 4. ELIMINAR REGISTRO
@usuario_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    UsuarioModel.eliminar(id)
    flash('Usuario eliminado correctamente', 'info')
    return redirect(url_for('usuarios.index'))