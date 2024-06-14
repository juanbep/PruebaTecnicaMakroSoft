from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class SoporteDB(Base):
    __tablename__ = "soportes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(String, index=True)
    prioridad = Column(Integer)
    peso = Column(Integer)

    entidad_respuesta = relationship("EntidadRespuestaDB", back_populates="soporte")