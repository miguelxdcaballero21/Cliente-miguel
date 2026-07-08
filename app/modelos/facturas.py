from pydantic import BaseModel, computed_field
from sqlmodel import SQLModel, Field, Relationship
from .clientes import Cliente, ClienteLeer
from .transacciones import Transaccion
from datetime import datetime


# datos base
class FacturaBase(SQLModel):

    fecha: str = Field(default=datetime.now())
    #transacciones: list[Transaccion] = []


    @computed_field
    @property
    def vr_total(self) -> float:

        #factura_id_actual = getattr(self, "id", None)

        #total_factura = 0.0

        #if not factura_id_actual or not self.transacciones:
           # return total_factura

        # recorrer transacciones
        #for transaccion in self.transacciones:

         #   if transaccion.factura_id == factura_id_actual:
          #      total_factura += (
           #         transaccion.vr_unitario * transaccion.cantidad
          #      )

        return 0.0


# crear factura
class FacturaCrear(FacturaBase):
    pass


# editar factura
class FacturaEditar(FacturaBase):
    pass

    #crear modelo para mostrar usuario o el cliente
class FacturaLeer(FacturaBase):
    id: int 
    cliente: ClienteLeer

# factura completa
class Factura(FacturaBase, table=True):

    id: int | None = Field(default=None, primary_key=True)
    cliente_id: int = Field(default=None, foreign_key="cliente.id")
    #crear las relaciones virtuales no en la bd
    cliente : Cliente = Relationship(back_populates="factura") 
    