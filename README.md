# Smart Feature Flags API

Smart Feature Flags é uma API de **feature flags** construída com **Python** + **FastAPI**, preparada para evoluir decisões de liberação com suporte de **aprendizado de máquina (ML)**.

## Quickstart

Por padrão, a aplicação usa **SQLite** em `./db.sqlite3` (as tabelas são criadas automaticamente ao iniciar).

```bash
python3 -m venv .venv
source .venv/bin/activate
cp .env.example .env
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Documentação interativa:

- `/docs`
- `/redoc`

Rodar testes:

```bash
pytest
```

Configuração do banco (opcional):

```bash
export DATABASE_URL="sqlite:///./db.sqlite3"
```

Configurações adicionais (segurança/execução):

```bash
export ENVIRONMENT=development
export LOG_LEVEL=INFO
export ENABLE_DOCS=true
export TRUSTED_HOSTS='["localhost","127.0.0.1"]'
export CORS_ALLOWED_ORIGINS='["http://localhost:3000"]'
```

## Arquitetura

O projeto segue uma **Arquitetura em Camadas** (Layered Architecture), inspirada em **DDD “lite”**:

- **Domain (`app/domain/`)**
  - **Entidades** (`entities/`): estruturas de dados do domínio (dataclasses).
  - **Contratos** (`repositories/`): interfaces de repositório (o domínio depende de abstrações).
  - **Services** (`services/`): regras de negócio e orquestração (sem FastAPI/SQLAlchemy).

- **Infrastructure (`app/infrastructure/`)**
  - **Persistência** (`models.py`, `db.py`): modelos SQLAlchemy e sessão/engine.
  - **Repositórios concretos** (`repositories/`): implementação SQLite dos contratos do domínio.

- **API (`app/api/` + `app/schemas/`)**
  - **Rotas** FastAPI (HTTP) e **schemas** Pydantic (I/O).
  - Rotas chamam services; services chamam repositórios via contratos.

### Fluxo do CRUD (padrão do projeto)

Quando for adicionar/alterar operações de CRUD, a regra é manter as camadas alinhadas:

1. **Contrato** no domínio (`app/domain/repositories/*`)
2. **Regra/validação** no service (`app/domain/services/*`)
3. **Implementação** no repositório SQLite (`app/infrastructure/repositories/*`)
4. **Exposição HTTP** na rota (`app/api/v1/routes/*`)

## Endpoints principais

- **Features**: `POST/GET/GET by id/PUT/DELETE` em `/features`
- **Events**: `POST/GET/GET by id/PUT/DELETE` em `/events` (com filtros via query params em `GET /events`)
- **Evaluation**: `POST /evaluate`
- **Training**: `POST /train`, `GET /model/status`
- **Simulation**: `POST /simulate/users`, `POST /simulate/events`

## Segurança da API

- **Trusted Host** com allowlist configurável (`TRUSTED_HOSTS`).
- **CORS restritivo** com allowlist configurável (`CORS_ALLOWED_ORIGINS`).
- **Headers de segurança** em todas as respostas:
  - `X-Content-Type-Options: nosniff`
  - `X-Frame-Options: DENY`
  - `Referrer-Policy: no-referrer`
  - `Permissions-Policy` restritiva
- **Tratamento global de exceções** retorna payload genérico em erro inesperado:
  - `{"detail": "Internal server error."}`
- **Docs OpenAPI desabilitáveis** em ambientes sensíveis (`ENABLE_DOCS=false`).

## Como citar

Este repositório inclui um arquivo `CITATION.cff` compatível com o GitHub ("Cite this repository").
