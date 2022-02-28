"""
Module with the Response model data
"""
# pylint: disable=no-name-in-module
from datetime import datetime
from typing import Optional, Union, Generic, TypeVar
from pydantic import BaseModel
from pydantic.generics import GenericModel



TR = TypeVar("TR", bound=BaseModel)
class Response(GenericModel, Generic[TR]):
    """
    Class with the Response model data
    """
    results: Optional[Union[list[TR], TR]] = None
    status_code: int
class NamedResponse(BaseModel):
    """
    Model with name
    """
    name: str
    class Config:
        """
        Model configuration
        """
        extra = "ignore"
class PokemonResponse(BaseModel):
    """
    Pokemon response model data
    """
    name: str
    weight: int
    location_area_encounters: str
    last_consulted: datetime
    stats: list[NamedResponse]
    abilities: list[NamedResponse]
    types: list[NamedResponse]
    



class PokemonType(BaseModel):
    """
    Response pokemon type
    """
    name: str
    pokemons: list[str]

class GetAbilityPokemonListIResponse(BaseModel):
    """
    Response model data from the interactor GetAbilityPokemonListInteractor
    """
    ability: str
    results: list[PokemonType]