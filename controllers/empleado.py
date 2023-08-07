from flask_restful import Resource, request
from models.empleado import EmpleadoModel
from base_de_datos import conexion
from dtos.empleado import EmpleadoRequestDTO
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError


class EmpleadosController(Resource):
     #         GET /empleados: devolver a los empleados y opcionalmente pasarle sus "query   params" que podrían ser:
    # email: filtrar por sus email
    # nombre: filtrar por sus nombres
    # PISTA: para validar si existe o no el query param usar condicionales (if - elif - else)

    def get(self):
   
        empleados = conexion.session.query(EmpleadoModel).all()
        dto = EmpleadoRequestDTO()
        
        # para filtrar por su email y nombre
        email = request.args.get('email')
        nombre = request.args.get('nombre')

        if email:
            empleadoEncontrado = conexion.session.query(EmpleadoModel).filter_by(email=email).first()
            if not empleadoEncontrado:
                return {
                    'message': 'No existe el empleado con ese email'
                }
            resultado = dto.dump(empleadoEncontrado)
            return {
                'content': resultado
            }, 200
        elif nombre:
            empleadoEncontrado = conexion.session.query(EmpleadoModel).filter_by(nombre=nombre).first()
            if not empleadoEncontrado:
                return {
                    'message': 'No existe el empleado con ese nombre'
                }
            resultado = dto.dump(empleadoEncontrado)
            return {
                'content': resultado
            }, 200
        else:
            resultado = dto.dump(empleados, many=True)
            return {
                'content': resultado
            }, 200
    
class EmpleadoController(Resource):
    def post(self):
        # POST /empleado: crear un empleado
        data:dict = request.get_json()
        dto = EmpleadoRequestDTO()
        try: 
            dataValidada = dto.load(data)
            nuevoEmpleado = EmpleadoModel(**dataValidada)
            conexion.session.add(nuevoEmpleado)
            conexion.session.commit()
            return {
                'message': 'Empleado creado exitosamente',
            }, 201                
        except ValidationError as e:
            return {
                'message': 'Hubo un error al validar los datos',
                'error': e.messages
            }, 400
        except IntegrityError as e:
            return {
                'message': 'Hubo un error al crear el empleado',
                'content': 'Faltan datos o el email ya existe'
            }, 400
        except Exception as e:
            conexion.session.rollback()
            return {
                'message': 'Hubo un error al crear el empleado',
                'content': e.args
            }, 400
        
    
