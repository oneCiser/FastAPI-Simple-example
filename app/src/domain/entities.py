"""
Domain entities
"""
from dataclasses import dataclass
from abc import ABC
from datetime import datetime


class NamedEntity(ABC):
    """
    Abstract class for all entities that have a name.
    """
    name: str

@dataclass
class Stat(NamedEntity):
    """
    Stat of a Pokémon.
    """
    game_index: int
    is_battle_only: bool

@dataclass
class Types(NamedEntity):
    """
    Type of a Pokémon.
    """
    pokemon: list['Pokemon']

@dataclass
class Pokemon(NamedEntity):
    """
    A pokemon entity
    """
    weight: int
    location_area_encounters: str
    types: list[Types]
    stats: list[Stat]
    abilities: list['Ability']
    last_consulted: datetime

@dataclass
class Ability(NamedEntity):
    """
    The ability of a Pokémonm, is no the same as pokemon move.
    """
    is_main_series: bool
    pokemon: list[Pokemon]
    slot: int
    