from flask import Flask
from controllers.producto_controller import producto_bp

app = Flask(__name__)

# Registro del Blueprint/Controlador
app.register_blueprint(producto_bp, url_prefix='/productos')

@app.route('/')
def home():
    return redirect('/productos')

if __name__ == '__main__':
    app.run(debug=True)