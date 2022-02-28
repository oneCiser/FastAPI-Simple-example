"""
Test PokeAPI Service
"""
import pytest
from src.services.pokeapi.services import PokeAPIService

@pytest.fixture
def get_pokeapi_service():
    """
    Fixture of pokea api service
    """
    return PokeAPIService()

def test_get_pokemon_data(get_pokeapi_service):
    """
    Test get pokemon data
    """
    pokemon_data = get_pokeapi_service.get_pokemon(pokemon_name="pikachu")
    assert pokemon_data["name"] == "pikachu"

def test_get_pokemon_not_name(get_pokeapi_service):
    """
    Test get exception when pokemon name is not found
    """
    with pytest.raises(ValueError):
        get_pokeapi_service.get_pokemon(pokemon_name=None)

def test_get_pokemon_no_exist(get_pokeapi_service):
    """
    Test get exception when pass invalid pokemon name
    """
    with pytest.raises(Exception):
        get_pokeapi_service.get_pokemon(pokemon_name="pikachu_not_exist")

def test_get_ability_data(get_pokeapi_service):
    """
    Test get ability data
    """
    ability_data = get_pokeapi_service.get_ability(ability_name="overgrow")
    assert ability_data["name"] == "overgrow"

def test_get_ability_not_name(get_pokeapi_service):
    """
    Test get exception when ability name is not found
    """
    with pytest.raises(ValueError):
        get_pokeapi_service.get_ability(ability_name=None)

def test_get_ability_no_exist(get_pokeapi_service):
    """
    Test get exception when pass invalid ability name
    """
    with pytest.raises(Exception):
        get_pokeapi_service.get_ability(ability_name="ability_not_exist")