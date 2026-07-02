from fastapi import FastAPI, HTTPException, status
from modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from modelos.facturas import Factura, FacturaCrear, FacturaEditar
from modelos.transacciones import Transaccion,TransaccionCrear,TransaccionEditar



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
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"La factura con id {factura_id} no existe."
    )

@app.post("/facturas/{cliente_id}", response_model=Factura)
async def crear_factura(cliente_id: int, datos_factura: FacturaCrear):

    cliente_encontrado = None

    # buscar cliente
    for cliente in lista_clientes:
        if cliente.id == cliente_id:
            cliente_encontrado = cliente

    # validar cliente
    if cliente_encontrado is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El cliente con id {cliente_id} no existe."
        )

    # convertir datos a diccionario
    factura_dict = datos_factura.model_dump()

    # agregar cliente
    factura_dict["cliente"] = cliente_encontrado

    # validar factura
    factura_val = Factura.model_validate(factura_dict)

    # generar id
    factura_val.id = len(lista_facturas) + 1

    # guardar factura
    lista_facturas.append(factura_val)

    return factura_val

@app.patch("/facturas/{id_factura}", response_model=Factura)
async def editar_factura(id_factura: int, datos_factura: Factura):
    pass


@app.delete("/facturas/{id_factura}", response_model=Factura)
async def eliminar_factura(id_factura: int):
    pass
   
   
  # crear los endpoint para transacciones

@app.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones():
    return lista_transacciones

@app.get("/transacciones/{id_transaccion}", response_model=Transaccion)
async def listar_transaccion(id_transaccion: int):
    pass


@app.post("/transacciones/{factura_id}", response_model=Transaccion)
async def crear_transaccion(
    factura_id: int,
    datos_transaccion: TransaccionCrear
):

    # buscar factura
    factura_encontrada = None

    for factura in lista_facturas:
        if factura.id == factura_id:
            factura_encontrada = factura

    # validar factura
    if not factura_encontrada:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La factura con id {factura_id} no existe."
        )

    # convertir a diccionario
    transaccion_dict = datos_transaccion.model_dump()

    # agregar factura_id
    transaccion_dict["factura_id"] = factura_id

    # validar transaccion
    transaccion_val = Transaccion.model_validate(
        transaccion_dict
    )

    # generar id
    transaccion_val.id = len(lista_transacciones) + 1

    # guardar transaccion global
    lista_transacciones.append(transaccion_val)

    # agregar transaccion a la factura
    factura_encontrada.transacciones.append(transaccion_val)

    return transaccion_val


@app.patch("/transacciones/{id_transaccion}", response_model=Transaccion)
async def editar_transaccion(id_transaccion: int, datos_transaccion: Transaccion):
    pass


@app.delete("/transacciones/{id_transaccion}", response_model=Transaccion)
async def eliminar_transaccion(id_transaccion: int):
    pass