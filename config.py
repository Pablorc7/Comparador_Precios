#configuraciones de la aplicacion

import os

#comenzamos tomando la ruta absoluta del directorio raiz (proyecto_isi)
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    #definimos variables de configuracion

    #ubicacion de la base de datos relacional a usar con nuestra aplicacion flask
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///'+os.path.join(basedir,'app.db')