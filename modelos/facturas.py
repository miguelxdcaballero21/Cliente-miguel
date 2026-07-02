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

        factura_id_actual = getattr(self, "id", None)

        total_factura = 0.0

        if not factura_id_actual or not self.transacciones:
            return total_factura

        # recorrer transacciones
        for transaccion in self.transacciones:

            if transaccion.factura_id == factura_id_actual:
                total_factura += (
                    transaccion.vr_unitario * transaccion.cantidad
                )

        return total_factura


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
    