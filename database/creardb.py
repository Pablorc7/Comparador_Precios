import sqlite3
#from alcampo import categorias_alcampo
#from dia import categorias_dia
from mercadona import categorias_mercadona
import sys

# Forzar a que tenga la codificación "utf-8" para su impresión por consola
sys.stdout.reconfigure(encoding='utf-8')

lista_supers = [("alcampo",), ("dia",), ("mercadona",)]

# Agrega los supermercados a la base de datos.
# :param cursor: Cursor de la base de datos.
def agregar_supermercados(cursor):
    cursor.executemany("INSERT INTO supermercado VALUES (NULL,?)", lista_supers)


# Agrega los productos a un supermercado.
# :param cursor: Cursor de la base de datos.
def agregar_productos(cursor):
    #cursor.executemany("INSERT INTO producto VALUES (NULL,?,?,?,?,?,?)", categorias_alcampo())
    #cursor.executemany("INSERT INTO producto VALUES (NULL,?,?,?,?,?,?)", categorias_dia())
    cursor.executemany("INSERT INTO producto VALUES (NULL,?,?,?,?,?,?)", categorias_mercadona())

# Función que crea la base de datos
def crear_bd():
    conexion = sqlite3.connect("app.db")
    cursor = conexion.cursor()

    
    try:
        # Tabla de los supermercados
        cursor.execute('''
            CREATE TABLE supermercado (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(50)
            )
        ''')

        # Procedemos a crear las tablas de los supermercados
        cursor.execute(''' 
            CREATE TABLE producto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100),
                precio FLOAT,
                precio_kg VARCHAR(50),
                url_imagen VARCHAR(255),
                id_supermercado INTEGER,
                nombre_busqueda VARCHAR(100),
                FOREIGN KEY(id_supermercado) REFERENCES supermercados(id)
            )
        ''')

    except sqlite3.OperationalError:
        print("Error al crear las tablas")
    

    # Llamamos a la función para agregar los supermercados y productos a estos
    agregar_supermercados(cursor)
    agregar_productos(cursor)
    
    conexion.commit()
    conexion.close()


#este archivo lo ejecuto una sola vez, manualmente, para la creacion de la bd e insercion de datos
if __name__ == "__main__":
    crear_bd()