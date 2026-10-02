from flask import Flask, redirect, url_for
from controllers.usuario_controller import usuario_bp

app = Flask(__name__)
app.secret_key = 'cambia-esta-clave'  # necesaria para usar flash()

# Registrar el controlador de usuarios
app.register_blueprint(usuario_bp)


# La página principal redirige al listado de usuarios
@app.route('/')
def inicio():
    return redirect(url_for('usuarios.index'))


if __name__ == '__main__':
    app.run(debug=True)