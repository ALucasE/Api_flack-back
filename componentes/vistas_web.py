from flask import render_template
from main import app
from componentes.modelo_producto import todos_los_productos
from componentes.modelo_producto import ver_producto


@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/inicio')
def inicio_auth():
    return render_template('inicio_auth.html')

@app.route('/api')
def api():
    return render_template('api.html')

@app.route('/productos')
def productos():
    data = todos_los_productos()
    return render_template('productos.html', data=data)

@app.route('/productos/nuevo')
def producto_nuevo():
    return render_template('producto_nuevo.html')

@app.route('/productos/modificar/<string:id>')
def producto_modificar(id):
    data = ver_producto(id)
    return render_template('producto_modificar.html', data=data)