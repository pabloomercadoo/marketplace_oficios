from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import models
from database import engine
from routers import auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173",
                   "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Mensaje": "hola desde el backend"}

