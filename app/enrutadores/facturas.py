from fastapi import APIRouter, HTTPException, status

from app.modelos.clientes import Cliente

from ..modelos.facturas import Factura, FacturaCrear, FacturaEditar, FacturaLeer, FacturaLeerCompuesta
from app.listas import lista_facturas, lista_clientes
from ..conexion_bd import Sesion_dependencia
from sqlmodel import select

rutas_facturas = APIRouter()


# LISTAR FACTURAS
@rutas_facturas.get("/facturas", response_model=list[FacturaLeerCompuesta])
async def listar_facturas(sesion: Sesion_dependencia):
    #select * from factura 
    consulta = select(Factura)
    lista_facturas = sesion.exec(consulta).all()
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
@rutas_facturas.post("/facturas/{cliente_id}")
async def crear_factura(cliente_id: int, datos_factura: FacturaCrear, sesion: Sesion_dependencia):

    print("1. Entró al método")

    cliente_encontrado = sesion.get(Cliente, cliente_id)
    print("2. Cliente encontrado:", cliente_encontrado)

    if not cliente_encontrado:
        raise HTTPException(
            status_code=404,
            detail=f"El cliente con id {cliente_id} no existe."
        )

    factura_dict = datos_factura.model_dump()
    factura_dict["cliente_id"] = cliente_id
    print("3. Dict:", factura_dict)

    factura_val = Factura.model_validate(factura_dict)
    print("4. Modelo:", factura_val)

    sesion.add(factura_val)
    print("5. Antes del commit")

    sesion.commit()
    print("6. Después del commit")

    sesion.refresh(factura_val)
    print("7. Después del refresh")

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