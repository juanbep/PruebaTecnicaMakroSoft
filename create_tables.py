from sqlalchemy.orm import sessionmaker
from database import engine, Base
from models.soporte import SoporteDB
from models.trabajador import TrabajadorDB
from models.entidadRespuesta import EntidadRespuestaDB

# Crear las tablas en la base de datos (se eliminarán primero si existen)
Base.metadata.drop_all(bind=engine)  # Elimina todas las tablas
Base.metadata.create_all(bind=engine)  # Recrea todas las tablas

# Inicializar la sesión de SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

# Insertar registros de prueba para la tabla trabajadores
trabajadores_prueba = [
    TrabajadorDB(nombre="Pedro", peso_acumulado=0),
    TrabajadorDB(nombre="Felipe", peso_acumulado=0),
    TrabajadorDB(nombre="Andrea", peso_acumulado=0),
    TrabajadorDB(nombre="Maria", peso_acumulado=0),
    TrabajadorDB(nombre="Juan", peso_acumulado=0)
]

session.add_all(trabajadores_prueba)
session.commit()

print("Base de datos reiniciada y registros de prueba de trabajadores insertados.")

