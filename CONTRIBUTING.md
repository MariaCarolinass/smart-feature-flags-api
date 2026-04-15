# Como contribuir

Obrigado por contribuir com o **Smart Feature Flags API**.

## Requisitos

- Python 3.12+

## Setup local

```bash
python3 -m venv .venv
source .venv/bin/activate
cp .env.example .env
pip install -r requirements.txt
```

Rodar a API:

```bash
uvicorn app.main:app --reload
```

## Testes

Antes de abrir PR, rode:

```bash
source .venv/bin/activate
pytest
python3 -m compileall -q app tests
```

## Padrões do projeto (obrigatório)

Siga o `AGENT.md`. Resumo:

- **Arquitetura**: camadas `domain` → `infrastructure` → `api`
- **CRUD**: contrato → service → repo → rota (+ schema)
- **Erros**: use exceções tipadas em `app/core/exceptions.py` e mapeie com `to_http_exception()`
- **Segurança**: não vazar detalhes internos em `500`, respeitar `TRUSTED_HOSTS` e `CORS_ALLOWED_ORIGINS`

## Pull Requests

- **Escopo pequeno**: PRs menores são mais fáceis de revisar
- **Checklist**:
  - [ ] testes passando (`pytest`)
  - [ ] `compileall` passando
  - [ ] sem endpoints “fantasmas” (rota sem suporte no service/repo)
  - [ ] docs atualizadas (`README.md`, `.env.example`) quando aplicável

## Issues

Ao abrir issue, inclua:

- passo a passo para reproduzir
- comportamento esperado vs atual
- versão do Python e comando usado (ex.: `uvicorn ...`)

