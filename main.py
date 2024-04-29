from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()

vendas ={
    1: {"item": "lata", "preco": 4.00},
    2: {"item": "livro", "preco": 40.00},
    3: {"item": "garrafa", "preco": 3.00}
}

class Inputs(BaseModel):
    i1: int
    i2: str

@app.get("/")
def rodando():
    return "Minha Api esta Rodando"

@app.get("/venda/{id_venda}")
def pegar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return "Venda não encontrada"
    
@app.post("/nova")
def nova(inputs: Inputs) -> str:
    return inputs.i2


if __name__ == "__main__":
    uvicorn.run(app, port=8000)