from datetime import date
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.services import ja_recebeu_no_mes

app = FastAPI(title="Mãos que Alimentam Digital")

familias: dict[UUID, dict] = {}
entregas: dict[UUID, list[date]] = {}


class FamiliaIn(BaseModel):
    nome_responsavel: str = Field(min_length=1, max_length=120)
    num_pessoas: int = Field(ge=1)
    consentimento_lgpd: bool


class EntregaIn(BaseModel):
    data_entrega: date


@app.get("/saude")
def saude():
    return {"status": "ok"}


@app.post("/familias", status_code=201)
def cadastrar_familia(dados: FamiliaIn):
    if not dados.consentimento_lgpd:
        raise HTTPException(422, "O consentimento é obrigatório.")
    id_familia = uuid4()
    familias[id_familia] = dados.model_dump()
    entregas[id_familia] = []
    return {"id_familia": str(id_familia), **dados.model_dump()}


@app.post("/familias/{id_familia}/entregas", status_code=201)
def registrar_entrega(id_familia: UUID, dados: EntregaIn):
    if id_familia not in familias:
        raise HTTPException(404, "Família não encontrada.")
    if dados.data_entrega > date.today():
        raise HTTPException(422, "A data não pode ser futura.")
    anterior = ja_recebeu_no_mes(entregas[id_familia], dados.data_entrega)
    if anterior:
        raise HTTPException(
            409, f"Esta família já recebeu cesta em {anterior.strftime('%d/%m/%Y')}."
        )
    entregas[id_familia].append(dados.data_entrega)
    return {"mensagem": "Cesta registrada.", "data_entrega": dados.data_entrega}
