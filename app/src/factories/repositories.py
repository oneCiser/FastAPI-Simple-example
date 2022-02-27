"""
Module with the repositories factories
"""
from ..persistence.repositories import PokemonRepositoryDB
from ..domain.repositories import PokemonRespository

class RepositoryFactory:
    """
    Class with the repositories factories
    """

    @staticmethod
    def get() -> object:
        """
        Get the pokemon repository
        """
        return PokemonRespository(PokemonRepositoryDB())