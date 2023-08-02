from sqlalchemy import Column,types
from base_de_datos import conexion

class AreaModel(conexion.Model):
    id = Column(type_= types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False, unique=True)
    piso = Column(type_=types.Integer, nullable=False)
    # Name of the table
    __tablename__ = 'areas'