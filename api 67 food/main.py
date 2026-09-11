from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import bd
from schemas import Restaurante

from schemas.restaurante import Restaurante
from models.cliente import Cliente


from fastapi.staticfiles import StaticFiles

"""
Nome: 67food

"""
from sqlite3 import Connection

from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles

import bd
from schemas import Restaurante


app = FastAPI(title="98food")
app.mount("/static", StaticFiles(directory="./static"))

restaurantes = []


@app.get("/restaurantes",
         tags=["restaurantes"])
def obter_todos_os_restaurantes(con: Connection = Depends(bd.obter_conexão)) -> list[Restaurante]:
    """Listar todos os restaurantes"""
    restaurantes = bd.obter_restaurantes(con)
    return [
        Restaurante(
            id=id,
            nome=nome,
            localização=localização
        )
        for id, nome, localização, categoria in restaurantes
    ]


@app.post("/restaurantes",
         tags=["restaurantes"])
def criar_restaurante(restaurante: Restaurante, con: Connection = Depends(bd.obter_conexão)) -> Restaurante:
    """Criar restaurante"""
    bd.inserir_restaurante(restaurante)
    return restaurante


@app.get("/restaurantes/{id}",
         tags=["restaurantes"])
def obter_informação_de_restaurante(id: str | None = None, nome: str | None = None, 
                                    con: Connection = Depends(bd.obter_conexão)):
    """Listar todos os restaurantes"""
    return bd.obter_restaurante(id, nome)
    
