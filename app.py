from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'clave_super_secreta'  #  Necesaria para usar sesiones

# 🔹 Configuración de conexión MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # si tienes contraseña, escríbela aquí
app.config['MYSQL_DB'] = 'login_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['MYSQL_PORT'] = 3306

# Inicializar conexión
try:
    mysql = MySQL(app)
    print("✅ Conexión a MySQL inicializada correctamente (puerto 3306).")
except Exception as e:
    print("❌ Error al inicializar MySQL:", e)


#  Página principal (Login)

@app.route('/')
def index():
    if 'nombre' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')


#  Procesar login

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM usuarios WHERE email=%s AND password=%s", (email, password))
        user = cur.fetchone()
        cur.close()

        if user:
            # ✅ Guardar datos del usuario en la sesión
            session['id'] = user['id']
            session['nombre'] = user['nombre']
            session['email'] = user['email']

            flash(f"Bienvenido {user['nombre']} 👋", "success")
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Correo o contraseña incorrectos")
    except Exception as e:
        print("❌ Error en login:", e)
        return f"Error al procesar el inicio de sesión: {e}"


#  Registro de nuevos usuarios

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

            flash("✅ Usuario registrado correctamente. Ahora puedes iniciar sesión.", "success")
            return redirect(url_for('index'))
        except Exception as e:
            print("❌ Error al registrar usuario:", e)
            return f"Error al guardar el usuario en la base de datos: {e}"

    return render_template('register.html')
#  Panel principal (Dashboard)

@app.route('/dashboard')
def dashboard():
    if 'nombre' not in session:
        return redirect(url_for('index'))
    return render_template('dashboard.html', nombre=session['nombre'])


#  Cerrar sesión

@app.route('/logout')
def logout():
    session.clear()
    flash("Sesión cerrada correctamente.", "info")
    return redirect(url_for('index'))


#  Ejecutar servidor Flask

if __name__ == '__main__':
    app.run(debug=True)
