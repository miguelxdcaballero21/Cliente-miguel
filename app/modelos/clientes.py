from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship


class ClienteBase(SQLModel):
    nombre: str
    email: str
    descripcion: str | None = None


class ClienteCrear(ClienteBase):
    pass


class ClienteEditar(ClienteBase):
    pass


class ClienteLeer(ClienteBase):
    id: int


class Cliente(ClienteBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    factura: list["Factura"] = Relationship(back_populates="cliente")