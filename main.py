from fastapi import FastAPI, HTTPException
from modelos.clientes import Cliente, ClienteCrear

app = FastAPI()

lista_clientes: list[Cliente] = []

# endpoint para listar todos los clientes
@app.get("/clientes", response_model=list[Cliente])
async def listar_clientes():
    return lista_clientes
    

# endpoint para listar un solo cliente
@app.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int):

    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            return obj_cliente

    raise HTTPException(status_code=404, detail="Cliente no encontrado")


# endpoint para crear un cliente y agregar a la lista
@app.post("/clientes", response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear):

    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    
    #generar el id 
    id_cliente = len(lista_clientes)+1
    cliente_val.id = id_cliente
    lista_clientes.append(cliente_val)
   
    return cliente_val

#endpoint para editar un cliente, y agregar a la lista
@app.patch("/clientes/{cliente_id}", response_model=Cliente)
async def editar_cliente(cliente_id: int, datos_cliente: Cliente_editar):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            return obj_cliente
        raise HTTPException(status_code=400, detail=f"el cliente con id {cliente_id}, no existe.")