from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship
# Clase base que contiene los atributos principales
# de una transacción o detalle de factura
class TransaccionBase(SQLModel):

    # Cantidad de productos o servicios
    cantidad: int = Field(default=0)
    # Valor unitario de cada producto
    vr_unitario: float = Field(default=0.0)
    

# Clase utilizada para crear una nueva transacción
# Hereda todos los atributos de TransaccionBase
class TransaccionCrear(TransaccionBase):
    pass
    # "pass" significa que no se agrega nada nuevo
    # pero se mantiene la estructura heredada

class TransaccionEditar(TransaccionBase):
    pass
# Clase que representa una transacción completa
# normalmente usada para mostrar datos desde la base de datos
class Transaccion(TransaccionBase, table=True):

    # ID único de la transacción
    # Puede ser entero o None si aún no existe
    id: int | None = Field(default=None, primary_key=True)
    factura_id: int | None = Field(default=None, foreign_key="factura.id")