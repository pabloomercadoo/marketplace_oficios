from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models
import schemas

#Todas tus rutas van a empezar con /auth automáticamente

router = APIRouter(prefix="/auth", tags=["Autenticacion"])

#la llave para abrir la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#Tu ruta POST para iniciar sesión
@router.post("/login")
def login(credenciales: schemas.UserLogin, db: Session = Depends(get_db)):
    
    # 1. Buscamos en MYSQL si el email existe
    usuario = db.query(models.User).filter(models.User.email == credenciales.email).first()

    # 2. Si el usuario no existe, rebotamos la petición
    if not usuario:
        raise HTTPException(status_code=400, detail="usuario no encontrado")
    
    # 3. Verificamos si la contraseña coincide
    if usuario.password != credenciales.password:
        raise HTTPException(status_code=400, detail="contraseña incorrecta")
    
    # 4. Si todo está bien, le damos la bienvenida
    return {
        "mensaje": "¡Login exitoso!",
        "usuario": {
            "id": usuario.id,
            "nombre": usuario.name,
            "email": usuario.email
            }
    }