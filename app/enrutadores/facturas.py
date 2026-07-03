from fastapi import APIRouter, HTTPException, status

from ..modelos.facturas import Factura, FacturaCrear, FacturaEditar
from app.listas import lista_facturas, lista_clientes

rutas_facturas = APIRouter()


# LISTAR FACTURAS
@rutas_facturas.get("/facturas", response_model=list[Factura])
async def listar_facturas():
    return lista_facturas


# LISTAR UNA FACTURA
@rutas_facturas.get("/facturas/{factura_id}", response_model=Factura)
async def listar_factura(factura_id: int):

    for obj_factura in lista_facturas:
        if obj_factura.id == factura_id:
            return obj_factura

    raise HTTPException(
        status_code=404,
        detail=f"La factura con id {factura_id} no existe."
    )


# CREAR FACTURA
@rutas_facturas.post("/facturas/{cliente_id}", response_model=Factura)
async def crear_factura(cliente_id: int, datos_factura: FacturaCrear):

    cliente_encontrado = None

    for cliente in lista_clientes:
        if cliente.id == cliente_id:
            cliente_encontrado = cliente
            break

    if cliente_encontrado is None:
        raise HTTPException(
            status_code=404,
            detail=f"El cliente con id {cliente_id} no existe."
        )

    factura_dict = datos_factura.model_dump()
    factura_dict["cliente"] = cliente_encontrado

    factura_val = Factura.model_validate(factura_dict)

    factura_val.id = len(lista_facturas) + 1

    lista_facturas.append(factura_val)

    return factura_val


# EDITAR FACTURA
@rutas_facturas.patch("/facturas/{factura_id}", response_model=Factura)
async def editar_factura(factura_id: int, datos_factura: FacturaEditar):

    for i, factura in enumerate(lista_facturas):

        if factura.id == factura_id:

            factura_actualizada = factura.model_copy(
                update=datos_factura.model_dump(exclude_unset=True)
            )

            lista_facturas[i] = factura_actualizada

            return factura_actualizada

    raise HTTPException(
        status_code=404,
        detail=f"La factura con id {factura_id} no existe."
    )


# ELIMINAR FACTURA
@rutas_facturas.delete("/facturas/{factura_id}", response_model=Factura)
async def eliminar_factura(factura_id: int):

    for i, factura in enumerate(lista_facturas):

        if factura.id == factura_id:

            factura_eliminada = lista_facturas.pop(i)

            return factura_eliminada

    raise HTTPException(
        status_code=404,
        detail=f"La factura con id {factura_id} no existe."
    )