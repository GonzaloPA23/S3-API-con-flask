from flask_restful import Resource
from models.empleado import EmpleadoModel

class EmpleadosController(Resource):
    def get(self):
        return {
            'message': 'Hola desde empleados controller'
        }
    
class EmpleadoController(Resource):
    def post(self):
        return {
            'message': 'Hola desde empleado controller'
        }
    
