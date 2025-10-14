from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Página principal (login)
@app.route('/')
def index():
    return render_template('login.html')

# Procesamiento del login
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # Ejemplo de usuario válido
    if email == "Bryan@gmail.com" and password == "12345":
        return redirect(url_for('dashboard'))
    else:
        # Retorna de nuevo el login con un mensaje de error
        return render_template('login.html', error="Correo o contraseña incorrectos")

# Página de destino (dashboard)
@app.route('/dashboard')
def dashboard():
    return "<h1>✅ Bienvenido al panel principal</h1>"

if __name__ == '__main__':
    app.run(debug=True)
