"""
Modulo to define the use cases od the domain layer.
"""

import asyncio
import functools
from fastapi import HTTPException
from concurrent.futures import ThreadPoolExecutor
from abc import ABCMeta, abstractmethod
from typing import TypeVar, Generic, Union
from requests import Session
from ..persistence.schemas import PokemonSchema

TK = TypeVar("TK")
TR = TypeVar("TR")


class BaseClassInteractor(Generic[TK, TR],metaclass=ABCMeta):
    """
    Abstract class to define the base class of all interactors.

    ...

    Attributes
    ----------
    respository : Repository
        repository to be used by the interactor
        default: None
    """
    repository: TR = None
    _data: Union[TK, None] = None
    _query: Union[dict, None] = None

    @abstractmethod
    async def execute(self) -> None:
        """
        Abstract method to define the execution of the interactor.
        """

    @abstractmethod
    def set_parameters(self, *args, **kwargs) -> None:
        """
        Abstract method to define the parameters of the interactor.

        ...

        Parameters
        ----------
        *args :
            positional arguments
        **kwargs :
            named arguments
        """

    @abstractmethod
    def get_data(self) -> Union[TK, None]:
        """
        Abstract method to define the data returned by the interactor.

        ...

        Returns
        -------
        TK
            data returned by the interactor
        """

class GetAbilityPokemonListInteractor(BaseClassInteractor[TK, TR]):
    """
    Get abilitys from pokemon to consume poke api.
    """

    def __init__(self, repository: TR, service = None):
        self.repository = repository
        self.service = service


    async def execute(self):
        """
        Logic of the use case.
        """
        pokemons_types = {}
        try:

            with Session() as session:
                self.service.set_session(session)
                query_pokemon = self._query.get("pokemon", None)
                query_abilitie_index = self._query.get("abilitie_index", 0)
                pokemon = self.service.get_pokemon(pokemon_name=query_pokemon)
                abilities_list = pokemon.get("abilities", [])
                if len(abilities_list) <= query_abilitie_index:
                    abilitie_index = len(abilities_list) - 1
                else:
                    abilitie_index = query_abilitie_index
                abilitie = abilities_list[abilitie_index].get("ability").get("name")
                ability = self.service.get_ability(ability_name=abilitie)
                
                response_pokemons = []
                with ThreadPoolExecutor(max_workers=10) as executor:
                    loop = asyncio.get_event_loop()
                    tasks = [
                        loop.run_in_executor(
                            executor,
                            functools.partial(self.service.get_pokemon,
                                pokemon_name=pokemon.get("pokemon").get("name"))
                        )
                        for pokemon in ability.get("pokemon")
                    ]
                    for response in await asyncio.gather(*tasks):
                        response_pokemons.append(response)
            save_tasks = []
            for tmp_pokemon in response_pokemons:#ability.get("pokemon"):
                # pokemon_name = pokemon_from_ability.get("pokemon").get("name")
                pokemon_name = tmp_pokemon.get("name")
                # tmp_pokemon = self.service.get_pokemon(pokemon_name=pokemon_name)

                data_to_save = {
                    "name":tmp_pokemon["name"],
                    "weight":tmp_pokemon["weight"],
                    "location_area_encounters":tmp_pokemon["location_area_encounters"],
                    "types":tmp_pokemon["types"],
                    "stats":tmp_pokemon["stats"],
                    "abilities":tmp_pokemon["abilities"],
                }
                save_task = asyncio.ensure_future(self.repository.save_or_update(**data_to_save))
                save_tasks.append(save_task)

                for type_item in tmp_pokemon.get("types", []):
                    type_name = type_item.get("type").get("name")
                    if type_name in pokemons_types:
                        pokemons_types[type_name].append(pokemon_name)
                    else:
                        pokemons_types[type_name] = [pokemon_name]
            await asyncio.gather(*save_tasks, return_exceptions=True)
            self._data = {
                "ability": abilitie,
                "results":[{"name":key,"pokemons":value}
                    for key, value in pokemons_types.items()]
                }
        except ValueError as error:
            raise HTTPException(status_code=400, detail=str(error)) from error
        except Exception as error:
            print(error)
            raise HTTPException(status_code=404, detail="Pokemon not found") from error



    def set_parameters(self, *args, **kwargs):
        self._query = kwargs

    def get_data(self):
        return self._data

class GetAllSavedPokemonInteractor(BaseClassInteractor[TK, TR]):
    """
    Get all saved pokemon from database.
    """

    def __init__(self, repository: TR):
        self.repository = repository

    async def execute(self):
        """
        Logic of the use case.
        """
        try:
            self._data = [PokemonSchema.from_orm(item) for item in self.repository.get_all(**self._query)]
        except Exception as error:
            print(error)
            raise HTTPException(status_code=500, detail="Internal server error") from error

    def set_parameters(self, *args, **kwargs):
        self._query = kwargs

    def get_data(self):
        return self._data

class GetSavedPokemonInteractor(BaseClassInteractor[TK, TR]):
    """
    Get a pokemon from database.
    """

    def __init__(self, repository: TR):
        self.repository = repository

    async def execute(self):
        """
        Logic of the use case.
        """
        try:
            self._data = PokemonSchema.from_orm(self.repository.get(**self._query))
        except Exception as error:
            raise HTTPException(status_code=500, detail="Internal server error") from error

    def set_parameters(self, *args, **kwargs):
        self._query = kwargs

    def get_data(self):
        return self._data