"""
Modulo to define the use cases od the domain layer.
"""

import asyncio
import functools
from concurrent.futures import ThreadPoolExecutor
from abc import ABCMeta, abstractmethod
from typing import TypeVar, Generic, Union
from requests import Session
from fastapi import BackgroundTasks

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
        def save_pokemon(repository, **kwargs):
            repository.save(**kwargs)
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
                pokemons_types = {}
                response_pokemons = []
                with ThreadPoolExecutor(max_workers=10) as executor:
                    loop = asyncio.get_event_loop()
                    
                    tasks = [
                        loop.run_in_executor(
                            executor,
                            functools.partial(self.service.get_pokemon, pokemon_name=pokemon.get("pokemon").get("name"))
                        )
                        for pokemon in ability.get("pokemon")
                    ]
                    for response in await asyncio.gather(*tasks):
                        response_pokemons.append(response)
            for tmp_pokemon in response_pokemons:#ability.get("pokemon"):
                # pokemon_name = pokemon_from_ability.get("pokemon").get("name")
                pokemon_name = tmp_pokemon.get("name")
                # tmp_pokemon = self.service.get_pokemon(pokemon_name=pokemon_name)
                BackgroundTasks().add_task(
                    save_pokemon,
                    self.repository,
                    **tmp_pokemon)

                for type_item in tmp_pokemon.get("types", []):
                    type_name = type_item.get("type").get("name")
                    if type_name in pokemons_types:
                        pokemons_types[type_name].append(pokemon_name)
                    else:
                        pokemons_types[type_name] = [pokemon_name]
            self._data = {
                "ability": abilitie,
                "results":[{"name":key,"pokemons":value}
                    for key, value in pokemons_types.items()]
                }
            
        except Exception as error:
            raise error


    def set_parameters(self, *args, **kwargs):
        self._query = kwargs

    def get_data(self):
        return self._data
