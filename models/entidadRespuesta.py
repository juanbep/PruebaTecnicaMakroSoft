from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from database import Base

class EntidadRespuestaDB(Base):
    __tablename__ = "entidad_respuesta"

    id = Column(Integer, primary_key=True, index=True)
    soporte_id = Column(Integer, ForeignKey('soportes.id'))
    trabajador_id = Column(Integer, ForeignKey('trabajadores.id'))

    soporte = relationship("SoporteDB", back_populates="entidad_respuesta")
    trabajador = relationship("TrabajadorDB", back_populates="entidad_respuesta")