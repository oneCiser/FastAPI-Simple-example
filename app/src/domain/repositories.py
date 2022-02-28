"""
Poekmons repository
"""

class PokemonRespository:
    """
    Pokemon repository
    """

    def __init__(self, _db_repsitory) -> None:
        self._db_repsitory = _db_repsitory

    def save(self, **kwargs):
        """
        Save the pokemon
        """
        pokemon = self._db_repsitory.save(**kwargs)

        return pokemon
    def update(self, **kwargs):
        """
        update the pokemon
        """
        pokemon = self._db_repsitory.update(**kwargs)
        return pokemon
        
    def save_or_update(self, **kwargs):
        """
        save or update the pokemon
        """
        pokemon = self._db_repsitory.save_or_update(**kwargs)
        return pokemon

    def get(self, **kwargs):
        """
        Get the pokemon
        """
        pokemon = self._db_repsitory.get(**kwargs)
        return pokemon
    
    def get_all(self, **kwargs):
        """
        Get all the pokemons
        """
        pokemons = self._db_repsitory.get_all(**kwargs)
        return pokemons
