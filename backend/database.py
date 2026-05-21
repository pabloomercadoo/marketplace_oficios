import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

#Traer la url de conexion de .env
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")


# Crear el motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear una sesión de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoFlush=False, bind=engine)

# Crear la clase base para los modelos de la base de datos
Base = declarative_base()

