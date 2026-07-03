from pydantic import BaseModel
# Clase base que contiene los atributos principales
# de una transacción o detalle de factura
class TransaccionBase(BaseModel):

    # Cantidad de productos o servicios
    cantidad: int

    # Valor unitario de cada producto
    vr_unitario: float
    

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
class Transaccion(TransaccionBase):

    # ID único de la transacción
    # Puede ser entero o None si aún no existe
    factura_id: int
    id: int | None = None