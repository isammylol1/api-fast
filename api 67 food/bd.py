import sqlite3

con = sqlite3.connect("67food.db")

conexao = None

def obter_conexão():
    if conexao is None:
        conexao =  sqlite3.connect("98food.db")
       
    return conexao

def criar_banco(con):
    con.execute("""
    CREATE TABLE IF NOT EXISTS restaurantes (
        id INTEGER PRIMARY KEY,
        nome VARCHAR(50),
        local VARCHAR(200),
        tipo INTEGER,
        FOREIGN KEY (tipo) REFERENCES CATEGORIAS (id)
    );
    """)


con.execute("""
    CREATE TABLE IF NOT EXISTS CATEGORIAS (
        id INTEGER PRIMARY KEY,
        nome VARCHAR(50),
        local VARCHAR(200)
    );
""")


con.execute("""
    CREATE TABLE IF NOT EXISTS restaurantes (
        id INTEGER PRIMARY KEY,
        nome VARCHAR(50),
        local VARCHAR(200),
        tipo INTEGER,
        FOREIGN KEY (tipo) REFERENCES CATEGORIAS (id)
    );
""")

con.commit()

def obter_restaurantes():
    cursor = con.execute("SELECT * FROM restaurantes")
    return cursor.fetchall()

def inserir_restaurantes(nome, local, tipo):
    con.execute("INSERT INTO restaurantes(nome, local, tipo) VALUES(?, ?, ?)", (nome, local, tipo))
    con.commit()

def obter_restaurante(id_restaurante, nome):
    cursor = con.execute(f"""SELECT * from RESTAURANTES
                             WHERE id = {id_restaurante} OR nome = {nome};""")
    return cursor.fetchall()
