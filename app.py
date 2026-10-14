from flask import Flask, redirect, url_for
from controllers.cliente_controller import cliente_bp

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'

# Registrar Blueprints / Controladores
app.register_blueprint(cliente_bp)

@app.route('/')
def root():
    return redirect(url_for('cliente.index'))

if __name__ == '__main__':
    app.run(debug=True)