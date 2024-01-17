from database import Database
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date

class alumnos(Database):
    __tablename__ = 'Alumnos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(20))
    apellidos = Column(String(30))
    materia = Column(String(30))
    presente = Column(String(10))
    
