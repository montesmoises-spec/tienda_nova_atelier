from flask import Flask, redirect, url_for
from controllers.producto_controller import producto_bp
from controllers.cliente_controller import cliente_bp

app = Flask(__name__)

# Registrar el Blueprint del controlador de productos
app.register_blueprint(producto_bp, url_prefix='/productos')
app.register_blueprint(cliente_bp, url_prefix='/clientes')

@app.route('/')
def index():
    # Redirige por defecto a la vista principal de productos
    return redirect(url_for('producto.index'))

if __name__ == '__main__':
    app.run(debug=True)