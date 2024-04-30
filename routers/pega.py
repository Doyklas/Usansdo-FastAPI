from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/pega")

class ProdutosResponse(BaseModel):
    id: int
    desc: str
    valor: float
    tipo: str # disponivel,  indisponivel

class ProdutosRequest(BaseModel):
    desc: str
    valor: float
    tipo: str # disponivel,  indisponivel


@router.get("/", response_model=List[ProdutosResponse])
def listar_vendas():
    return [
        ProdutosResponse(
            id=1,
            desc ="tela",
            valor =4.09,
            tipo ="disponivel"
        ),
         ProdutosResponse(
            id=2,
            desc ="tela2",
            valor =4.99,
            tipo ="indisponivel"
        )
    ]

@router.post("/",  response_model=ProdutosResponse, status_code=201)
def criar_produto(produto: ProdutosRequest):
    return ProdutosResponse(
            id=3,
            desc =produto.desc,
            valor =produto.valor,
            tipo =produto.tipo
        )