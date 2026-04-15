from __future__ import annotations

from uuid import uuid4

from fastapi.testclient import TestClient

from app.main import app


def test_health_endpoint_returns_ok() -> None:
    with TestClient(app) as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}


def test_feature_retrieve_returns_not_found_with_typed_payload() -> None:
    with TestClient(app) as client:
        response = client.get(f"/features/{uuid4()}")
        assert response.status_code == 404
        payload = response.json()
        assert "detail" in payload
        assert payload["detail"]["code"] == "not_found"


def test_error_response_does_not_leak_internal_details(monkeypatch) -> None:
    from app.api.v1.routes import evaluate as evaluate_route

    def explode(*args, **kwargs):
        raise RuntimeError("segredo interno")

    monkeypatch.setattr(evaluate_route.evaluation_service, "evaluate", explode)

    with TestClient(app) as client:
        response = client.post("/evaluate", json={"feature_key": "missing", "user": {"user_id": "u1"}})
        assert response.status_code == 500
        assert response.json() == {"detail": "Internal server error."}


def test_security_headers_present() -> None:
    with TestClient(app) as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.headers.get("x-content-type-options") == "nosniff"
        assert response.headers.get("x-frame-options") == "DENY"
        assert response.headers.get("referrer-policy") == "no-referrer"

