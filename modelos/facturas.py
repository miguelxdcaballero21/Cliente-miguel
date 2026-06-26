from datetime import date
from pydantic import BaseModel
from modelos.clientes import Cliente

# Clase base que contiene los datos principales
# de una factura
class FacturaBase(BaseModel):

    fecha: date
    vr_total: float
    cliente: Cliente

# Crear factura
class FacturaCrear(FacturaBase):
    pass
 
# Editar factura
class FacturaEditar(FacturaBase):
    pass

# Modelo completo de factura
class Factura(FacturaBase):

    id: int | None = None