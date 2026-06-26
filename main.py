from fastapi import FastAPI, HTTPException
from modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from modelos.facturas import Factura
from modelos.transacciones import Transaccion

app = FastAPI()

lista_clientes: list[Cliente] = []
lista_facturas: list[Factura] = []
lista_transacciones: list[Transaccion] = []

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

    raise HTTPException(
        status_code=400,
        detail=f"El cliente con id {cliente_id} no existe."
    )


# endpoint para crear un cliente y agregar a la lista
@app.post("/clientes", response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear):

    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    
    # generar el id
    id_cliente = len(lista_clientes) + 1
    cliente_val.id = id_cliente
    lista_clientes.append(cliente_val)
   
    return cliente_val


# endpoint para editar un cliente
@app.patch("/clientes/{cliente_id}", response_model=Cliente)
async def editar_cliente(cliente_id: int, datos_cliente: ClienteEditar):

    for i, obj_cliente in enumerate(lista_clientes):

        if obj_cliente.id == cliente_id:

            # validar cliente
            cliente_val = Cliente.model_validate(
                datos_cliente.model_dump()
            )

            cliente_val.id = cliente_id

            lista_clientes[i] = cliente_val

            return cliente_val

    raise HTTPException(
        status_code=400,
        detail=f"El cliente con id {cliente_id} no existe."
    )
    
    # crear los endpoint para facturas

@app.get("/facturas", response_model=list[Factura])
async def listar_facturas():
    return lista_facturas


@app.get("/facturas/{factura_id}", response_model=Factura)
async def listar_factura(factura_id: int):

    for i, obj_factura in enumerate(lista_facturas):

        if obj_factura.id == factura_id:
            return obj_factura

    raise HTTPException(
        status_code=400,
        detail=f"La factura con id {factura_id} no existe."
    )

@app.post("/facturas", response_model=Factura)
async def crear_factura(id_cliente: int, datos_factura: Factura):
    return {}

@app.patch("/facturas/{id_factura}", response_model=Factura)
async def editar_factura(id_factura: int, datos_factura: Factura):
    return{}


@app.delete("/facturas/{id_factura}", response_model=Factura)
async def eliminar_factura(id_factura: int):
    return{}
   
   
  # crear los endpoint para transacciones

@app.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones():
    return []

@app.get("/transacciones/{id_transaccion}", response_model=Transaccion)
async def listar_transaccion(id_transaccion: int):
    return {}


@app.post("/transacciones/{id_factura}", response_model=Transaccion)
async def crear_transaccion(id_factura: int, datos_transaccion: Transaccion):
    return {}


@app.patch("/transacciones/{id_transaccion}", response_model=Transaccion)
async def editar_transaccion(id_transaccion: int, datos_transaccion: Transaccion):
    return {}


@app.delete("/transacciones/{id_transaccion}", response_model=Transaccion)
async def eliminar_transaccion(id_transaccion: int):
    return {}