from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hola desde flask!</h1>"

@app.route('/contacto')
def contacto():
    return "<h1>Contacto</h1>"

@app.route('/quienes')
def quienes():
    return "<h1>Quienes</h1>"

@app.route('/servicios')
def servicios():
    return "<h1>Sevicios</h1>"

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f"<h1>hola, {nombre}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)