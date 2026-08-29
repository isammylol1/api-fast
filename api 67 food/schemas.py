from pydantic import BaseModel

class Restaurante(BaseModel):
    id: int
    nome: str
    localização: str