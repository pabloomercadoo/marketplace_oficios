from sqlalchemy import Column, Integer, String
from database import Base

#Crear la clase User que hereda de la clase Base
class User(Base):
    __tablename__ = "users"

    #crear las columnas
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(100), unique=True, index=True)
    password = Column(String(100))

    


