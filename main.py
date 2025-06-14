
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Mensaje(BaseModel):
    texto: str

@app.get("/")
def read_root():
    return {"mensaje": "Melania API está viva y lista para ayudarte."}

@app.post("/mensaje")
def responder(mensaje: Mensaje):
    return {"respuesta": f"Hola! Recibí tu mensaje: {mensaje.texto}"}
