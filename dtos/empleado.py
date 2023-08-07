from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.empleado import EmpleadoModel

class EmpleadoRequestDTO(SQLAlchemyAutoSchema):
    class Meta:
        model = EmpleadoModel