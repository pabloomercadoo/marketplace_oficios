from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/", response_model=schemas.UserResponse)
def crear_usuario(usuario: schemas.UserCreate, db: Session = Depends(get_db)):

    #buscamos en mysql si el email ya existe
    usuario_existente = db.query(models.User).filter(models.User.email == usuario.email).first()

    # si existe el email, lanzamos un error
    if usuario_existente:
        raise HTTPException(status_code=400, detail="Este email ya esta registrado")
    
    # si no existe el email, creamos el usuario
    nuevo_usuario = models.User(
        name = usuario.name,
        email = usuario.email,
        password = usuario.password
    )

    # agregamos el nuevo usuario a la base de datos
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    # devolvemos el nuevo usuario creado
    return nuevo_usuario

