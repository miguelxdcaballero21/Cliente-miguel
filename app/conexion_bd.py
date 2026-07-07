from fastapi import FastAPI, Depends
from typing import Annotated
from sqlmodel import Session, SQLModel, create_engine

nombre_bd = "bd_clientes.sqlite3"
url_bd = f"sqlite:///{nombre_bd}"

# Motor de la base de datos
motor_bd = create_engine(url_bd)

# Método para crear las tablas
def crear_tablas(app: FastAPI):
    SQLModel.metadata.create_all(motor_bd)
    yield

# Método para obtener la sesión
def obtener_sesion():
    with Session(motor_bd) as mi_sesion:
        yield mi_sesion

# Inyección de dependencias
Sesion_dependencia = Annotated[Session, Depends(obtener_sesion)]