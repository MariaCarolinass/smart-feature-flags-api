# Smart Feature Flags API — Project Rules

## Architecture (must follow)

* **Layered + DDD lite**: `domain` -> `infrastructure` -> `api`.
* `domain` must **not** import FastAPI/SQLAlchemy.
* Business rules belong in `services`; data access via contracts in `domain/repositories`.

## Code organization

* `app/domain/`: entities, contracts, services.
* `app/infrastructure/`: `models.py`, `db.py`, SQLite repositories.
* `app/api/` + `app/schemas/`: HTTP routes + request/response schemas.
* `app/core/`: config, logging, exceptions.

## Flow for any CRUD

1. Define/adjust contract in `app/domain/repositories/*`.
2. Apply validation and business rules in `app/domain/services/*`.
3. Implement persistence in `app/infrastructure/repositories/*`.
4. Expose via route in `app/api/v1/routes/*` with schema in `app/schemas/*`.

## API rules

* Do not create endpoints without real support in service/repository.
* Use typed exceptions from `app/core/exceptions.py`.
* Map domain errors to HTTP via `to_http_exception()`.
* Standard status codes:

  * `404`: not found
  * `409`: conflict
  * `204`: delete with no body
  * `500`: unexpected error without leaking internal details

## Database and initialization

* Single persistence layer: **SQLAlchemy + SQLite**.
* Default URL: `sqlite:///./db.sqlite3` (via `DATABASE_URL`).
* `init_db()` runs on **lifespan startup** in `app/main.py`.
* UUID stored as `String(36)`; dictionary fields as `JSON`.

## Security and runtime

* Respect `.env` configuration (`Settings`):

  * `ENVIRONMENT`, `LOG_LEVEL`, `ENABLE_DOCS`
  * `TRUSTED_HOSTS`, `CORS_ALLOWED_ORIGINS`
* Keep security middlewares and generic internal error responses.
* Logging via `app/core/logging.py` (do not reconfigure root logger unnecessarily).

## Tests (mandatory when changing code)

* Structure:

  * `tests/services/`
  * `tests/infrastructure/repositories/`
  * `tests/api/`
* Run:

```bash
source .venv/bin/activate
pytest
python3 -m compileall -q app tests
```

## PR checklist

* Layers are consistent and properly decoupled.
* Routes, services, and repositories aligned.
* No “ghost” endpoints.
* README and `.env.example` updated if setup/config changes.