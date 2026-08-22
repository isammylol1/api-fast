from pydantic import BaseModel

class Restaurante(BaseModel):
    nome: str
    localizaçao: str
    