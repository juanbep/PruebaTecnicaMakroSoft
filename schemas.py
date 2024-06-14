from pydantic import BaseModel
from pydantic import ConfigDict
from typing import Optional

class Soporte(BaseModel):
    id: Optional[int]
    nombre: str
    descripcion: str
    prioridad: int
    peso: int

    class Config:
        from_attributes = True

class Trabajador(BaseModel):
    id: Optional[int]
    nombre: str
    peso_acumulado: int

    class Config:
        from_attributes = True

class EntidadRespuesta(BaseModel):
    soporte: Soporte
    trabajador: Trabajador

    class Config:
        from_attributes = True
