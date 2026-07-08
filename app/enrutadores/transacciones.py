from fastapi import APIRouter, HTTPException, status

from ..modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar
from ..modelos.facturas import Factura
from ..listas import lista_transaccion, lista_facturas
from ..conexion_bd import Sesion_dependencia
from sqlmodel import select

rutas_transacciones = APIRouter()

# listar transacciones
@rutas_transacciones.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones(sesion: Sesion_dependencia):
        #consulta = select(Transaccion)
        #listar_transacciones = sesion.exec(consulta).all()
    return sesion.exec(select(Transaccion)).all()


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
async def crear_transaccion(
    factura_id: int,
    datos_transaccion: TransaccionCrear,
    sesion: Sesion_dependencia
):
    factura_encontrada = sesion.get(Factura, factura_id)

    if not factura_encontrada:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La factura con id {factura_id} no existe."
        )

    transaccion_dict = datos_transaccion.model_dump()
    transaccion_dict["factura_id"] = factura_id

    transaccion_val = Transaccion.model_validate(transaccion_dict)

    sesion.add(transaccion_val)
    sesion.commit()
    sesion.refresh(transaccion_val)

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