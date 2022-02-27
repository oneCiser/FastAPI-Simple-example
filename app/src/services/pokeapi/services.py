"""
Module with the pokeapi services
"""
import requests

class PokeAPIService:
    """
    Consume de poke api
    """

    _host_url: str = "https://pokeapi.co/"
    _api_url: str = "api/"
    _api_version: str = "v2/"
    session = None
    def set_session(self, session = None) -> None:
        """
        Set the session
        """
        self.session = session
    def get_pokemon(self, pokemon_name:str=None, pokemon_id:int=None) -> dict:
        """
        Get the pokemon data
        """
        if self.session:
            get = self.session.get
        else:
            get = requests.get
        query = None
        if pokemon_name:
            query = pokemon_name
        elif pokemon_id:
            query = pokemon_id

        if query:
            url = f"{self._host_url}{self._api_url}{self._api_version}pokemon/{query}"
            response = get(url)
            if response.status_code == 200:
                return response.json()
                
            else:
                raise Exception(f"Error getting the pokemon data: {response.status_code}")
        else:
            raise ValueError("The pokemon name or id is required")

    def get_ability(self, ability_name:str=None) -> dict:
        """
        Get the ability data
        """
        if self.session:
            get = self.session.get
        else:
            get = requests.get
        if ability_name:
            url = f"{self._host_url}{self._api_url}{self._api_version}ability/{ability_name}"
            response = get(url)
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f"Error getting the ability data: {response.status_code}")
        else:
            raise ValueError("The ability name is required")