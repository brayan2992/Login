from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# 🔹 Configuración de MySQL (ajusta si usas contraseña)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'login_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# 🔹 Página principal (login)
@app.route('/')
def index():
    return render_template('login.html')

# 🔹 Procesar login
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios WHERE email=%s AND password=%s", (email, password))
    user = cur.fetchone()
    cur.close()

    if user:
        return redirect(url_for('dashboard'))
    else:
        return render_template('login.html', error="Correo o contraseña incorrectos")

# 🔹 Registro de nuevos usuarios
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']

        try:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)", (nombre, email, password))
            mysql.connection.commit()
            cur.close()
            print("✅ Usuario registrado correctamente.")
            return redirect(url_for('index'))
        except Exception as e:
            print("❌ Error al registrar:", e)
            return "Error al guardar el usuario en la base de datos."

    return render_template('register.html')

# 🔹 Página después del login
@app.route('/dashboard')
def dashboard():
    return "<h1>✅ Bienvenido al panel principal</h1>"

if __name__ == '__main__':
    app.run(debug=True)
