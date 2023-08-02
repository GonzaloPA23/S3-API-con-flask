from flask import Flask
from base_de_datos import conexion
from urllib.parse import quote_plus
from flask_migrate import Migrate
from models.area import AreaModel
from models.empleado import EmpleadoModel

app = Flask(__name__)

# Se van a guardar todas las variables de nuestro proyecto de flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:%s@localhost:5432/empresa' % quote_plus('@Goldenboy2310@')

# inicializar mi aplicación de flask sql alchemy
# dentro de la aplicación de flask tendremos nuestra conexión a la base de datos
conexion.init_app(app)

Migrate(app, conexion) # inicializar la migración

if __name__ == '__main__':
    app.run(debug=True)
