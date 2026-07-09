from flask import Flask 
 
app = Flask(__name__) 
 
@app.route('/') 
def inicio(): 
    return '<h1>Mi primera aplicación con Flask</h1><p>Laboratorio S07b para realizar cosas mas en concreto - Programación IV</p>' 
 
@app.route('/acerca') 
def acerca(): 
    return '<h1>Acerca del estudiante</h1><p>Nombre: Escriba aquí su nombre completo Edwin isaac Zeledon.</p>' 
 
if __name__ == '__main__': 
    app.run(debug=True) 