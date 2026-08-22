from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from models.restaurante import Restaurante
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
def cria_estabelecimento():
    """Criar conta do estabelecimento"""
    pass


@app.post("/produtos",
            tags=["produtos"])
def cadastra_produto():
    """Cadastrar produtos"""
    pass


@app.get("/restaurantes", 
         tags=["restaurantes"])
def obter_todos_restaurantes():
    """Listar todos os restaurantes"""
    pass


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
    