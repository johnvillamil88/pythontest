from flask import Flask, jsonify
import pyodbc 

app = Flask(__name__)

server = 'pytestgl.database.windows.net'
database = 'db_test'
username = 'pytestgl'
password = 'Pass$$1234'
driver = '{ODBC Driver 17 for SQL Server}'

@app.route('/productos')
def obtener_productos():
    try:
        conn = pyodbc.connect(f'SERVER={server};DATABASE={database};Uid={username};PWD={password};DRIVER={driver}')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM productos')
        productos = cursor.fetchall()
        conn.close()

        return jsonify({'productos': [dict(zip([column[0] for column in cursor.description], row)) for row in productos]})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/producto/<int:producto_id>')
def obtener_producto(producto_id):
    try:
        conn = pyodbc.connect(f'SERVER={server};DATABASE={database};Uid={username};PWD={password};DRIVER={driver}')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM productos WHERE id = ?', producto_id)
        producto = cursor.fetchone()
        conn.close()

        if producto:
            return jsonify(dict(zip([column[0] for column in cursor.description], producto)))
        else:
            return jsonify({'mensaje': 'Producto no encontrado'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
