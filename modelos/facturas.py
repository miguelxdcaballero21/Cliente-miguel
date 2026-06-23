from pydantic import BaseModel
from datetime import date

class FacturaBase(BaseModel):
    fecha: date
    vr_total: float
    cliente_id: int

class FacturaCrear(FacturaBase):
    pass

class Factura(FacturaBase):
    id: int | None = None