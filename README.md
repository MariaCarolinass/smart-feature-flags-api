# Adaptive Flags

Adaptive Flags é uma API de feature flags construída com **Python** e **FastAPI**, com foco em evolução para decisões inteligentes baseadas em **aprendizado de máquina**.

A proposta do projeto é permitir que features sejam liberadas não apenas por regras estáticas, mas também por análise de comportamento de usuários a partir de eventos do sistema.

## Objetivo

O MVP do projeto tem como foco:

- cadastrar e consultar features
- registrar eventos de usuários
- avaliar se uma feature deve ser liberada para um usuário
- treinar um modelo simples para suporte à decisão
- simular usuários e eventos para testes e experimentação

## Visão de arquitetura

O projeto segue uma separação em camadas para manter o código organizado, testável e preparado para crescer.

### Domain
Responsável pelas regras de negócio e contratos do sistema.

Contém:
- entidades de domínio
- interfaces de repositórios
- services com regras de negócio

### Infrastructure
Responsável pelas implementações concretas de acesso a dados e integrações externas.

Exemplos:
- repositórios em memória
- futuramente repositórios com SQLAlchemy/PostgreSQL
- persistência de modelo de ML

### API
Responsável pela exposição HTTP da aplicação.

Contém:
- rotas FastAPI
- schemas de request/response
- tratamento de erros HTTP

## Estrutura inicial sugerida

```text
app/
  api/
    v1/
      routes/
  domain/
    entities/
    repositories/
    services/
  infrastructure/
    repositories/
  schemas/
  main.py
````

## Endpoints do MVP

### Features

#### `POST /features`

Cria uma nova feature flag.

#### `GET /features`

Lista todas as features.

#### `GET /features/{feature_id}`

Retorna uma feature pelo identificador.

---

### Events

#### `POST /events`

Registra um evento de usuário relacionado a uma feature.

#### `GET /events`

Lista eventos, com possibilidade de filtros simples.

---

### Evaluation

#### `POST /evaluate`

Recebe dados do usuário e decide se a feature deve ser liberada.

A decisão pode seguir dois caminhos:

* rollout percentual
* modelo de ML, quando disponível e habilitado

---

### Training

#### `POST /train`

Executa o treinamento do modelo.

#### `GET /model/status`

Retorna o status atual do modelo treinado.

---

### Simulation

#### `POST /simulate/users`

Gera usuários sintéticos para testes.

#### `POST /simulate/events`

Gera eventos sintéticos para testes e treinamento.

## Decisão de feature no MVP

No estágio atual, a avaliação segue a estratégia abaixo:

1. se a feature não existir, a resposta será negativa
2. se a feature estiver desabilitada, a resposta será negativa
3. se a feature estiver com ML habilitado e existir modelo treinado, a decisão poderá usar o modelo
4. caso contrário, a decisão usa rollout percentual estável por usuário

Essa abordagem permite começar simples, com fallback seguro e previsível.

## Princípios adotados

* separação clara entre regra de negócio e persistência
* services sem responsabilidade de acesso direto a dados
* repositórios definidos como contratos no domínio
* implementação concreta dos repositórios fora do domínio
* rotas HTTP enxutas, delegando comportamento aos services
* base preparada para troca de persistência em memória por banco relacional

## Estado atual

Atualmente o projeto está em fase de MVP e usa repositórios em memória para acelerar a implementação inicial.

Próximos passos planejados:

* persistência com PostgreSQL
* SQLAlchemy + migrations
* testes automatizados
* treinamento real de modelo com scikit-learn
* versionamento de modelos
* observabilidade e logs estruturados

## Como rodar localmente

Exemplo com Uvicorn:

```bash
uvicorn app.main:app --reload
```

Após iniciar a aplicação, a documentação interativa estará disponível em:

* `/docs`
* `/redoc`

## Status

Projeto em construção.
O objetivo atual é consolidar uma base sólida de arquitetura antes de avançar para componentes mais sofisticados de machine learning e produção.