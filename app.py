from flask import Flask, render_template
import sqlite3


app = Flask(__name__)

# === CONFIGURACIÓN DE LA BASE DE DATOS ===
def get_db_connection():
    # Ruta absoluta construida desde la raíz del proyecto
    conn = sqlite3.connect('PANADERIA.db')
    conn.row_factory = sqlite3.Row
    return conn
   

# === RUTA PRINCIPAL ===
@app.route('/')

def index():
    conn = get_db_connection()
    clientes_y_productos=conn.execute('SELECT * FROM CLIENTES INNER JOIN PRODUCTOS ON CLIENTES.ID_PRODUCTO=PRODUCTOS.ID_PRODUCTO').fetchall()
    conn.close()

    return render_template('index.html', datos=clientes_y_productos)
   
# === EJECUCIÓN DEL SERVIDOR ===
if __name__ == '__main__':
    app.run(debug=True)
