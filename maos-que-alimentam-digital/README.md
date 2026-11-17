# Mãos que Alimentam Digital

MVP para controle de entrega de cestas básicas da Associação Mãos que Alimentam.
Evita entregas duplicadas no mês, funciona offline e contribui para o ODS 2 (Fome Zero).

## Funcionalidades do MVP
- RF01 Cadastro de famílias
- RF02 Registro de cesta com aviso de entrega repetida
- RF05 Uso offline com sincronização
- RF06 Painel de totais mensais

## Tecnologias
Angular (PWA) · Python 3.12 + FastAPI · PostgreSQL

## Estrutura
- `backend/`  API em FastAPI (regras de negócio em `app/services.py`)
- `frontend/` PWA em Angular (será criado com o Angular CLI)
- `docs/`     requisitos, modelo de dados e telas

## Como executar o backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Documentação interativa da API: http://127.0.0.1:8000/docs

## Como rodar os testes
```bash
cd backend
pytest
```

## Autor
Seu nome — Projeto de Software, Experiência Prática III
