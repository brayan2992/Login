import MySQLdb

try:
    conexion = MySQLdb.connect(
        host="localhost",
        user="root",         # tu usuario
        passwd="",           # tu contraseña (si tienes)
        db="login_db"        # tu base de datos
    )
    print("✅ Conexión exitosa a la base de datos")
    conexion.close()
except Exception as e:
    print("❌ Error al conectar:", e)
