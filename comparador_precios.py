#archivo que importa la aplicacion flask creada y que va a ser cargada
from app import app
from app import routes

#el directorio que contiene dicho script de inicio se agrega automaticamente al 'sys.path'
#esto permite que los modulos del directorio raiz puedan ser importados sin problemas desde cualquier lugar del poyecto