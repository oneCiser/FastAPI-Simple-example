from fastapi import APIRouter
from . import pokemons

routes = APIRouter(prefix="/api/v1", tags=["api"])
routes.include_router(pokemons.routes)