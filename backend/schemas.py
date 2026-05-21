from pydantic import BaseModel, EmailStr

# Filtro para recibir datos del cliente

class UserCreate(BaseModel):
    name: str
    email: EmailStr #valida automaticamente que el email tenga un formato correcto
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True #permite convertir un objeto de la base de datos a un objeto de respuesta, incluso si los nombres de los campos son diferentes


