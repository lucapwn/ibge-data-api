from fastapi import FastAPI
from api import endpoints

app = FastAPI(
    title="IBGE Data API",
    description="API para consumir e disponibilizar dados dos municípios brasileiros fornecidos pelo IBGE.",
    version="1.0.0",
)

app.include_router(endpoints.router, prefix="/api/v1")
