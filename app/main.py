from fastapi import FastAPI

from .enrutadores.clientes import rutas_clientes
from .enrutadores.facturas import rutas_facturas
from .enrutadores.transacciones import rutas_transacciones

app = FastAPI()

# routers
app.include_router(rutas_clientes, tags=["clientes"])
app.include_router(rutas_facturas, tags=["facturas"])
app.include_router(rutas_transacciones, tags=["transacciones"])