"""
Module with the interactors factories
"""
from ..domain.interactors import GetAbilityPokemonListInteractor, GetAllSavedPokemonInteractor, GetSavedPokemonInteractor
from .repositories import RepositoryFactory
from ..services.pokeapi.services import PokeAPIService
from ..domain.interactors import BaseClassInteractor

class InteractorsFactory:
    """
    Class with the interactors factories
    """

    @staticmethod
    def get(interactor_name) -> BaseClassInteractor:
        """
        Get the pokemon interactor
        """
        if interactor_name == "GetAbilityPokemonListInteractor":
            repository = RepositoryFactory.get()
            return GetAbilityPokemonListInteractor(repository, service=PokeAPIService())
        elif interactor_name == "GetAllSavedPokemonInteractor":
            repository = RepositoryFactory.get()
            return GetAllSavedPokemonInteractor(repository)
        elif interactor_name == "GetSavedPokemonInteractor":
            repository = RepositoryFactory.get()
            return GetSavedPokemonInteractor(repository)
        else:
            raise ValueError("Interactor name invalid")
