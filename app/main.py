from fastapi import FastAPI, HTTPException, status
from .modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from .modelos.facturas import Factura, FacturaCrear, FacturaEditar
from .modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar
from .enrutadores import clientes

app = FastAPI()

lista_clientes: list[Cliente] = []
lista_facturas: list[Factura] = []
lista_transacciones: list[Transaccion] = []

# incluir ruta de clientes
app.include_router(clientes.rutas_clientes, tags=["clientes"])


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