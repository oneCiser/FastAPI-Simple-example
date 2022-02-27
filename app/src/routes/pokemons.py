"""
The routes of the pokemos query
"""
from fastapi import APIRouter
from ..api.models.response import Response, GetAbilityPokemonListIResponse
from ..factories.interactors import InteractorsFactory

routes = APIRouter(prefix="/pokemons", tags=["pokemons"])

@routes.post("/{pokemon}/ability/same",
    response_model=Response[GetAbilityPokemonListIResponse])
async def get_pokemons_with_the_same_ability(pokemon:str, abilitie_index:int=0):
    """
    Get the pokemons with the same ability and return in groups of type
    """
    interactor = InteractorsFactory.get("GetAbilityPokemonListInteractor")
    interactor.set_parameters(pokemon=pokemon, abilitie_index=abilitie_index)
    await interactor.execute()
    response_raw_data = interactor.get_data()
    results = GetAbilityPokemonListIResponse(**response_raw_data)
    response = Response(results=results, status_code=200)
    return response
