from flask import Flask 
 
app = Flask(__name__) 
 
@app.route('/') 
def inicio(): 
    return '<h1>Mi primera aplicación con Flask</h1><p>Laboratorio S07b para realizar cosas mas en concreto - Programación IV</p>' 
 
@app.route('/acerca') 
def acerca(): 
    return '<h1>Acerca de la aplicación</h1><p>Esta es una aplicación de ejemplo creada con Flask para el laboratorio S07b.</p>'      
    return '<h1>Acerca del estudiante</h1><p>Nombre: Escriba aquí su nombre completo Edwin isaac Zeledon.</p>'  
    return '<h1>Acerca del estudiante</h1><p>Nombre: Edwin Isaac Zeledon.</p>'
 

@app.route('/contacto')
def contacto():
    return '<h1>Contacto</h1><p>Correo electrónico: escriba aquí su correo electrónico.</p>'  
    return '<h1>Contacto</h1><p>Correo electrónico: test @gmail.com</p>' 
if __name__ == '__main__': 
    app.run(debug=True) 