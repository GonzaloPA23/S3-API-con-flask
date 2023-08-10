from models.area import AreaModel
from dtos.area import AreaRequestDTO
from base_de_datos import conexion
from flask_restful import Resource,request
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError

class AreasController(Resource):
    def get(self):
        """ 
        file: yaml/getArea.yml 
        """
        areas = conexion.session.query(AreaModel).all() # select * from areas
        resultado = AreaRequestDTO(many=True).dump(areas)
        return {
            'content': resultado
        }, 200
    
class AreaController(Resource):   
    def post(self):
        """  
        file: yaml/postArea.yml
        """
       # crear una area
        data:dict = request.get_json()
        dto = AreaRequestDTO()

        try:
            dataValidada = dto.load(data)
            nuevaArea = AreaModel(**dataValidada)
            conexion.session.add(nuevaArea)
            conexion.session.commit()
            return {
                'message': 'Area creada exitosamente',
                'content': dto.dump(nuevaArea)
            }, 201
        except ValidationError as e:
            return {
                'message': 'Hubo un error al validar los datos',
                'error': e.messages
            }, 400
        except IntegrityError as e:
            return {
                'message': 'Hubo un error al crear el area',
                'content' : 'El nombre del area ya existe'
            }, 400
        except Exception as e:
            conexion.session.rollback()
            return {
                'message': 'Hubo un error al crear el area'
            }, 400

    
class AreaIdController(Resource):
    def get(self,id):
        """ 
        file: yaml/getAreaId.yml
        """
        usuarioEncontrado = conexion.session.query(AreaModel).filter_by(id=id).first()
        if not usuarioEncontrado:
            return {
                'message': 'No existe el area con ese id'
            }, 404
        dto = AreaRequestDTO()
        resultado = dto.dump(usuarioEncontrado)
        return {
            'content': resultado
        }, 200