from pydantic import BaseModel, computed_field
from sqlmodel import SQLModel, Field, Relationship
from .clientes import Cliente, ClienteLeer
from .transacciones import Transaccion
from datetime import datetime


# datos base
class FacturaBase(SQLModel):

    fecha: datetime = Field(default_factory=datetime.now)

    @computed_field
    @property
    def vr_total(self) -> float:
        total = 0.0

        if not hasattr(self, "transacciones") or not self.transacciones:
           return total

        for transaccion in self.transacciones:
            total += transaccion.cantidad * transaccion.vr_unitario

        return total
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
    #transacciones:list[Transaccion] = [] 
    
class FacturaLeerCompuesta(FacturaLeer):
    transacciones:list[Transaccion] = [] 
    

# factura completa
class Factura(FacturaBase, table=True):

    id: int | None = Field(default=None, primary_key=True)
    cliente_id: int = Field(default=None, foreign_key="cliente.id")
    #crear las relaciones virtuales no en la bd
    cliente : Cliente = Relationship(back_populates="factura") 
    transacciones: list[Transaccion] = Relationship(back_populates="factura")
    