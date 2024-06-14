from fastapi import FastAPI
from routers import soportes

app = FastAPI()

app.include_router(soportes.router, prefix="/soportes", tags=["soportes"])

@app.get("/")
async def read_root():
    return {"message": "Bienvenido a la API para antender soportes"}