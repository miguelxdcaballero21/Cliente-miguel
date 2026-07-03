from fastapi import APIRouter, HTTPException, status

from ..modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from app.listas import lista_clientes

rutas_clientes = APIRouter()

# lista temporal de clientes
#lista_clientes: list[Cliente] = []


# endpoint para listar todos los clientes
@rutas_clientes.get("/clientes", response_model=list[Cliente])
async def listar_clientes():
    return lista_clientes


# endpoint para listar un solo cliente
@rutas_clientes.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int):

    for obj_cliente in lista_clientes:

        if obj_cliente.id == cliente_id:
            return obj_cliente

    raise HTTPException(
    status_code=404,
    detail=f"El cliente con id {cliente_id} no existe."
)


# endpoint para crear un cliente y agregar a la lista
@rutas_clientes.post("/clientes", response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear):

    cliente_val = Cliente.model_validate(datos_cliente.model_dump())

    # generar el id
    id_cliente = len(lista_clientes) + 1
    cliente_val.id = id_cliente

    lista_clientes.append(cliente_val)

    return cliente_val


# endpoint para editar un cliente
@rutas_clientes.patch("/clientes/{cliente_id}", response_model=Cliente)
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
    status_code=404,
    detail=f"El cliente con id {cliente_id} no existe."
)


# endpoint para eliminar un cliente
@rutas_clientes.delete("/clientes/{cliente_id}", response_model=Cliente)
async def eliminar_cliente(cliente_id: int):

    for i, obj_cliente in enumerate(lista_clientes):

        if obj_cliente.id == cliente_id:

            cliente_eliminado = lista_clientes.pop(i)

            return cliente_eliminado

    raise HTTPException(
        status_code=404,
        detail=f"El cliente con id {cliente_id} no existe."
    )