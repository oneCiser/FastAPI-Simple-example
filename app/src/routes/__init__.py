from fastapi import APIRouter
from . import pokemons, consults

routes = APIRouter(prefix="/api/v1")
routes.include_router(pokemons.routes)
routes.include_router(consults.routes)