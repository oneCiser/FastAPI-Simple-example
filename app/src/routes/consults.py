"""
The routes of the pokemos consulted
"""
from fastapi import APIRouter
from ..api.models.response import Response, PokemonResponse
from ..factories.interactors import InteractorsFactory
routes = APIRouter(prefix="/consults", tags=["consults"])

@routes.get("/pokemon/all", response_model=Response[PokemonResponse])
async def get_all_pokemons(offset:int=0, limit:int=None):
    """
    Get all the pokemons
    """
    interactor = InteractorsFactory.get("GetAllSavedPokemonInteractor")
    interactor.set_parameters(offset=offset, limit=limit)
    await interactor.execute()
    response_raw_data = interactor.get_data()
    results = [PokemonResponse(**item.dict()) for item in response_raw_data]
    return Response(results=results, status_code=200)

@routes.get("/pokemon/{name}", response_model=Response[PokemonResponse])
async def get_pokemon(name:str):
    """
    Get one pokemon by name
    """
    interactor = InteractorsFactory.get("GetSavedPokemonInteractor")
    interactor.set_parameters(name=name)
    await interactor.execute()
    response_raw_data = interactor.get_data()
    results = PokemonResponse(**response_raw_data.dict())
    return Response(results=results, status_code=200)
