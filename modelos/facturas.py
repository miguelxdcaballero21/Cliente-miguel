from pydantic import BaseModel
from datetime import date
# Clase base que contiene los datos principales
# de una factura
class FacturaBase(BaseModel):

    # Fecha en la que se creó la factura
    fecha: date

    # Valor total de la factura
    vr_total: float

    # ID del cliente asociado a la factura
    cliente_id: int


# Clase utilizada para crear una nueva factura
# Hereda todos los atributos de FacturaBase
class FacturaCrear(BaseModel):
    fehca: str
    vr_total: float
    cliente: cliente
 
class FacturaBase(BaseModel):
     pass
    # "pass" indica que no se agregan más atributos
    # solo se reutiliza la estructura de FacturaBase
class FacturaCrear(FacturaBase):
    pass

class FacturaEditar(FacturaBase):
    pass

# Clase que representa una factura completa
# normalmente usada para mostrar información
# obtenida desde la base de datos
class Factura(FacturaBase):

    # ID único de la factura
    # Puede ser un entero o None
    # (por ejemplo antes de guardarse en la BD)
    id: int | None = None