from fastapi import FastAPI
from app.api.v1.router import api_router
from fastapi.responses import RedirectResponse

app = FastAPI(
    title="Adaptive Flags API",
    version="0.1.0",
    description="MVP de sistema de feature flags com suporte a avaliação por ML."
)

app.include_router(api_router)


@app.get("/", tags=["root"])
def root():
    return {"message": "Adaptive Flags API"}

@app.get("/health", tags=["health"])
def healthcheck():
    return {"status": "ok"}