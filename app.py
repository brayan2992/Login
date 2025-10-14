from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "clave_secreta_123"  # necesaria para mostrar mensajes flash

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Validación simple
        if email == "admin@gmail.com" and password == "12345":
            flash("Inicio de sesión exitoso", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Correo o contraseña incorrectos", "danger")

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return "<h1>Bienvenido al panel de control 🎉</h1>"

if __name__ == '__main__':
    app.run(debug=True)
