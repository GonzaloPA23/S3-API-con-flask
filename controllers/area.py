from models.area import AreaModel
from flask_restful import Resource

class AreasController(Resource):
    def get(self):
        return {
            'message': 'Hola desde areas controller'
        }

    
class AreaController(Resource):
    def get(self,id):
        return {
            'message': 'Hola desde area controller'
        }
    
    def post(self,id):
        return {
            'message': 'Hola desde area controller'
        }