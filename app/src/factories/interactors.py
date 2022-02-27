"""
Module with the interactors factories
"""
from ..domain.interactors import GetAbilityPokemonListInteractor
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
        else:
            raise ValueError("Interactor name invalid")
