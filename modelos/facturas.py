from pydantic import BaseModel, computed_field
from modelos.clientes import Cliente
from modelos.transacciones import Transaccion
from datetime import datetime


# datos base
class FacturaBase(BaseModel):

    fecha: datetime = datetime.now()
    transacciones: list[Transaccion] = []


    @computed_field
    @property
    def vr_total(self) -> float:

        total = 222

        for transaccion in self.transacciones:
            total += transaccion.valor

        return total


# crear factura
class FacturaCrear(FacturaBase):
    pass


# editar factura
class FacturaEditar(FacturaBase):
    pass


# factura completa
class Factura(FacturaBase):

    id: int | None = None
    cliente: Cliente