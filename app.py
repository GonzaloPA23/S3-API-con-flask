from flask import Flask
from base_de_datos import conexion
from urllib.parse import quote_plus
from flask_migrate import Migrate
from flask_restful import Api
from controllers.area import AreasController, AreaController, AreaIdController
from controllers.empleado import EmpleadosController, EmpleadoController

# Acá va toda la configuración de mi aplicación de flask y de mi api rest 
app = Flask(__name__)
api = Api(app) # esto sirve para poder crear las rutas de mi api rest en mi aplicación de flask 
# Se van a guardar todas las variables de nuestro proyecto de flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:%s@localhost:5432/empresa' % quote_plus('@Goldenboy2310@')
# inicializar mi aplicación de flask sql alchemy
# dentro de la aplicación de flask tendremos nuestra conexión a la base de datos
conexion.init_app(app)
Migrate(app, conexion) # inicializar la migración

# Acá se agregaran las rutas de nuestros controladores
api.add_resource(AreasController, '/areas') # /areas es la ruta que va a tener nuestro controlador
# api.add_resource(AreaController, '/area') # /area es la ruta que va a tener nuestro controlador
api.add_resource(AreaIdController, '/area/<int:id>') # /area/<int:id> es la ruta que va a tener nuestro controlador
api.add_resource(AreaController, '/area')
api.add_resource(EmpleadosController,'/empleados') # /empleados es la ruta que va a tener nuestro controlador
api.add_resource(EmpleadoController,'/empleado') # /empleado es la ruta que va a tener nuestro controlador

if __name__ == '__main__':
    app.run(debug=True)
