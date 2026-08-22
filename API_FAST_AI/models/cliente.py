from pydantic import BaseModel

class Cliente(BaseModel):
    nome: str
    idade: int
    tel: str
    cpf: str