from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import bd
from schemas import Restaurante

from schemas.restaurante import Restaurante
from models.cliente import Cliente


from fastapi.staticfiles import StaticFiles

app = FastAPI(title="67food")
app.mount("/static", StaticFiles(directory="./static"))

app.add_middleware(
CORSMiddleware,
allow_origins=["*"], # Explicit origins
allow_credentials=True, # Allow cookies/auth headers
allow_methods=["*"], # Allow all HTTP methods
allow_headers=["*"], # Allow all headers
)


clientes = []

@app.post("/clientes",
            tags=["clientes"])
def cria_conta(cliente: Cliente) -> Cliente:
    """Criar conta do cliente"""
    clientes.append(cliente)
    return cliente

@app.get("/clientes",
            tags=["clientes"])
def listar_contas() -> list[Cliente]:
    """Criar conta do cliente"""
    return clientes


@app.post("/estabelecimento",
            tags=["estabelecimento"])
def cria_estabelecimento(restaurante: Restaurante):
    """Criar conta do estabelecimento"""
    bd.inserir_restaurantes(restaurante.nome, restaurante.local, None)


@app.post("/produtos",
            tags=["produtos"])
def cadastra_produto():
    """Cadastrar produtos"""
    pass

@app.get(/restaurante_especifico)

def obter_restaurante(id_restaurante, nome):
    cursor = con.execute(f"""SELECT * from RESTAURANTES
                             WHERE id = {id_restaurante} OR nome = {nome};""")
    return cursor.fetchall()


@app.get("/estabelecimento",
         tags=["estabelecimento"])
def obter_todos_os_restaurantes() -> list[Restaurante]:
    """Listar todos os restaurantes"""
    restaurantes = bd.obter_restaurantes()
    return [
        Restaurante(
            id=id,
            nome=nome,
            localização=localização
        )
        for id, nome, localização, categoria in restaurantes
    ]



@app.get("/consulta_produtos", 
         tags=["consulta_produtos"])
def consultar_produtos():
    """Listar todos os restaurantes"""


    return []

@app.put("/atualizar",
         tags=["atualizar"])
def atualizar_cadastro():
    """Atualiza o cadastro do cliente"""
    return []
    