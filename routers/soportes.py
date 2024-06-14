from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import random

from database import SessionLocal
from models.soporte import SoporteDB
from models.trabajador import TrabajadorDB
from models.entidadRespuesta import EntidadRespuestaDB
from schemas import EntidadRespuesta, Soporte, Trabajador

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EntidadRespuesta)
async def create_soporte(soporte: Soporte, db: Session = Depends(get_db)):
    trabajadores = db.query(TrabajadorDB).all()
    if not trabajadores:
        raise HTTPException(status_code=404, detail="NO hay trabajadores en la BD")

    # lógica de negocio
    peso_maximo = max(trabajadores, key=lambda x: x.peso_acumulado).peso_acumulado
    candidatos = [trabajador for trabajador in trabajadores if trabajador.peso_acumulado == peso_maximo]

    # lógica de negocio
    trabajador_asignado = random.choice(candidatos)
    trabajador_asignado.peso_acumulado += soporte.peso
    db.add(trabajador_asignado)
    db.commit()

    soporte_db = SoporteDB(**soporte.model_dump())
    db.add(soporte_db)
    db.commit()
    db.refresh(soporte_db)

    entidad_respuesta_db = EntidadRespuestaDB(soporte_id=soporte_db.id, trabajador_id=trabajador_asignado.id)
    db.add(entidad_respuesta_db)
    db.commit()
    db.refresh(entidad_respuesta_db)

    entidad_respuesta = EntidadRespuesta(
        soporte=Soporte.model_validate(soporte_db),
        trabajador=Trabajador.model_validate(trabajador_asignado)
    )

    return entidad_respuesta

@router.get("/", response_model=List[Soporte])
async def get_soportes(db: Session = Depends(get_db)):
    return db.query(SoporteDB).all()

@router.get("/trabajadores", response_model=List[Trabajador])
async def get_trabajadores(db: Session = Depends(get_db)):
    return db.query(TrabajadorDB).all()

@router.post("/reset")
async def reset_pesos(db: Session = Depends(get_db)):
    trabajadores = db.query(TrabajadorDB).all()
    for trabajador in trabajadores:
        trabajador.peso_acumulado = 0
    db.commit()
    return {"message": "Los pesos se han reiniciado a 0 para todos los trabajadores"}

