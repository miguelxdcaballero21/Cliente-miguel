from fastapi import APIRouter, HTTPException, status

from ..modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar
from ..modelos.facturas import Factura
from app.listas import lista_transaccion, lista_facturas

rutas_transacciones = APIRouter()

# listar transacciones
@rutas_transacciones.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones():
    return lista_transaccion


# listar una transacción
@rutas_transacciones.get("/transacciones/{id_transaccion}", response_model=Transaccion)
async def listar_transaccion(id_transaccion: int):

    for transaccion in lista_transaccion:
        if transaccion.id == id_transaccion:
            return transaccion

    raise HTTPException(
        status_code=404,
        detail=f"La transacción con id {id_transaccion} no existe."
    )


# crear transacción
@rutas_transacciones.post("/transacciones/{factura_id}", response_model=Transaccion)
async def crear_transaccion(factura_id: int, datos_transaccion: TransaccionCrear):

    factura_encontrada = None

    for factura in lista_facturas:
        if factura.id == factura_id:
            factura_encontrada = factura

    if not factura_encontrada:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La factura con id {factura_id} no existe."
        )

    transaccion_dict = datos_transaccion.model_dump()
    transaccion_dict["factura_id"] = factura_id

    transaccion_val = Transaccion.model_validate(transaccion_dict)
    transaccion_val.id = len(lista_transaccion) + 1

    lista_transaccion.append(transaccion_val)
    factura_encontrada.transacciones.append(transaccion_val)

    return transaccion_val


# editar
@rutas_transacciones.patch("/transacciones/{id_transaccion}", response_model=Transaccion)
async def editar_transaccion(id_transaccion: int, datos_transaccion: TransaccionEditar):

    for i, transaccion in enumerate(lista_transaccion):

        if transaccion.id == id_transaccion:

            actualizada = transaccion.model_copy(
                update=datos_transaccion.model_dump(exclude_unset=True)
            )

            lista_transaccion[i] = actualizada
            return actualizada

    raise HTTPException(
        status_code=404,
        detail=f"La transacción con id {id_transaccion} no existe."
    )


# eliminar
@rutas_transacciones.delete("/transacciones/{id_transaccion}", response_model=Transaccion)
async def eliminar_transaccion(id_transaccion: int):

    for i, transaccion in enumerate(lista_transaccion):

        if transaccion.id == id_transaccion:
            return lista_transaccion.pop(i)

    raise HTTPException(
        status_code=404,
        detail=f"La transacción con id {id_transaccion} no existe."
    )