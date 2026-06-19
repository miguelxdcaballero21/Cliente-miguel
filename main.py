from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# crear el modelo clientes(id, nombre, email, descripcion)
class Cliente(BaseModel):
    id: int
    nombre: str
    email: str
    descripcion: str 

lista_clientes: list[Cliente] = []

# endpoint para listar todos los clientes
@app.get("/clientes")
def listar_clientes():
    return lista_clientes
    
# endpoint para listar un solo cliente
@app.get("/clientes/{cliente_id}")
def listar_cliente(cliente_id: int):

    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            return obj_cliente

    raise HTTPException(status_code=404, detail="Cliente no encontrado")

# endpoint para crear un cliente y agregar a la lista
@app.post("/clientes")
def crear_cliente(datos_cliente: Cliente):

    lista_clientes.append(datos_cliente)
   
    return datos_cliente