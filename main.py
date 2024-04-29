from fastapi import FastAPI

app = FastAPI()

vendas ={
    1: {"item": "lata", "preco": 4.00},
    2: {"item": "livro", "preco": 40.00},
    3: {"item": "garrafa", "preco": 3.00}
}

@app.get("/")
def rodando():
    return "Minha Api esta Rodando"

@app.get("/venda/{id_venda}")
def pegar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return "Venda não encontrada"