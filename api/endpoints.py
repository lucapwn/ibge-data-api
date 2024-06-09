import requests
from typing import Optional
from fastapi import APIRouter, HTTPException
from api import settings

router = APIRouter()

@router.get("/municipalities")
async def get_municipalities(
    name: Optional[str] = None,
    region: Optional[str] = None,
    mesoregion: Optional[str] = None,
    microregion: Optional[str] = None,
    state: Optional[str] = None,
    order_by: Optional[str] = None,
    descending: Optional[bool] = False):
    
    response = requests.get(settings.IBGE_API_URL)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Erro ao obter dados do IBGE.")
    
    municipalities = response.json()

    if name:
        municipalities = [municipality for municipality in municipalities if name in municipality["nome"]]

    if region:
        municipalities = [municipality for municipality in municipalities if municipality["microrregiao"]["mesorregiao"]["UF"]["regiao"]["nome"] == region]

    if mesoregion:
        municipalities = [municipality for municipality in municipalities if municipality["microrregiao"]["mesorregiao"]["nome"] == mesoregion]

    if microregion:
        municipalities = [municipality for municipality in municipalities if municipality["microrregiao"]["nome"] == microregion]

    if state:
        municipalities = [municipality for municipality in municipalities if municipality["microrregiao"]["mesorregiao"]["UF"]["sigla"] == state]

    if order_by:
        keys = {
            "name": lambda x: x["nome"],
            "region": lambda x: x["microrregiao"]["mesorregiao"]["UF"]["regiao"]["nome"],
            "mesoregion": lambda x: x["microrregiao"]["mesorregiao"]["nome"],
            "microregion": lambda x: x["microrregiao"]["nome"],
            "state": lambda x: x["microrregiao"]["mesorregiao"]["UF"]["sigla"]
        }

        try:
            municipalities = sorted(municipalities, key=keys[order_by], reverse=descending)
        except KeyError:
            raise HTTPException(status_code=400, detail="Campo de ordenação inválido.")

    return municipalities

@router.get("/municipality/{id}")
async def get_municipality(id: int):
    response = requests.get(f"{settings.IBGE_API_URL}/{id}")

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Erro ao obter dados do IBGE.")
    
    return response.json()
