from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_file, make_response
from models.ModelUser import ModelUser


#inicio app de flask
app = Flask(__name__)
user_model = ModelUser()


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('cursos.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
      
        users = user_model.find_user_by_usuario(usuario)
        print(users)
        if users:
            print(users)
            user = users[0]
            
            contrasena = user['password']
            if contrasena == password:
                # Autenticación exitosa, puedes redirigir al usuario a otra página.
                return 'Autenticación exitosa'
            else:
                error= 'usuario o contraseña errado, intente nuevamente.'
                return render_template('login.html',error= error)
        
        return render_template('login.html')
    
    return render_template('login.html')

@app.route('/registro', methods=['POST','GET'])
def registro():
    if request.method == 'POST':
        usuario = request.form['usuario']
        email = request.form['email']
        password = request.form['password']
        users = user_model.find_user_by_usuario(usuario)
        # Buscar usuario por email
        contraseña = request.form['password']
        confirmar_contraseña = request.form['confirm']

        if len(users) > 0:
            mensaje = "Este usuario ya se encuentra registrado, ingrese uno distinto nuevamente"
            return render_template('registro.html',mensaje=mensaje)
        else:
            # El usuario no existe en la base de datos
            if contraseña == confirmar_contraseña:
                nuevo_usuario = {
                    'email': email,
                    'usuario':usuario,
                    'rol': "",
                    'password': password,
                }
                user_model.insert_user(nuevo_usuario)
                completado = "Registro completado, su usuario ha sido creado de form satisfactoria"
                return render_template('registro.html', completado=completado)
            else:
                mensaje = "Las contraseñas no coinciden, por favor revise nuevamente"
                return render_template('registro.html', mensaje=mensaje)      
    return render_template('registro.html')


if __name__== "__main__":
    # app.register_error_handler(404, pagina_no_encontrada)
    # app.register_error_handler(405, err403)    
    app.run(debug=True, port=5017, threaded=True)