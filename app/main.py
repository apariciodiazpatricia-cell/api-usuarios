import os

from dotenv import load_dotenv
from fastapi import FastAPI
from app.api import user_routes
from app import models
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

load_dotenv()

app = FastAPI()

app.include_router(user_routes.router)

print("Host:", os.getenv("DB_HOST"))
print("Puerto:", os.getenv("DB_PORT"))
print("Base de datos:", os.getenv("DB_NAME"))
print("Usuario:", os.getenv("DB_USER"))
print("Contraseña configurada:", bool(os.getenv("DB_PASSWORD")))
