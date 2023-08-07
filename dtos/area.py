from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.area import AreaModel

class AreaRequestDTO(SQLAlchemyAutoSchema):
    class Meta:
        model = AreaModel
        include_fk = True