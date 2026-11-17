from datetime import date

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def _nova_familia():
    r = client.post(
        "/familias",
        json={"nome_responsavel": "Familia Teste", "num_pessoas": 3, "consentimento_lgpd": True},
    )
    assert r.status_code == 201
    return r.json()["id_familia"]


def test_cadastro_exige_consentimento():
    r = client.post(
        "/familias",
        json={"nome_responsavel": "Familia Teste", "num_pessoas": 3, "consentimento_lgpd": False},
    )
    assert r.status_code == 422


def test_segunda_cesta_no_mes_retorna_conflito():
    id_familia = _nova_familia()
    hoje = date.today().isoformat()
    assert client.post(f"/familias/{id_familia}/entregas", json={"data_entrega": hoje}).status_code == 201
    assert client.post(f"/familias/{id_familia}/entregas", json={"data_entrega": hoje}).status_code == 409
