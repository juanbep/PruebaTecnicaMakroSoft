from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class TrabajadorDB(Base):
    __tablename__ = "trabajadores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    peso_acumulado = Column(Integer, default=0)

    entidad_respuesta = relationship("EntidadRespuestaDB", back_populates="trabajador")