"""
The schema estructure of the entities.
"""
# pylint: disable=no-name-in-module
from pydantic import BaseModel
from datetime import datetime

class EntitySchema(BaseModel):
    """
    Abstract class for all schemas that have a name and id.
    """
    id: int
    name: str

class TypeSchema(EntitySchema):
    """
    Type model of a Pokémon.
    """

    class Config:
        """
        Aceppt ORM models
        """
        orm_mode = True

class StatSchema(EntitySchema):
    """
    Stat model of a Pokémon.
    """

    class Config:
        """
        Aceppt ORM models
        """
        orm_mode = True

class AbilitySchema(EntitySchema):
    """
    The ability of a Pokémonm, is no the same as pokemon move.
    """

    class Config:
        """
        Aceppt ORM models
        """
        orm_mode = True

class PokemonSchema(EntitySchema):
    """
    A pokemon schema
    """
    weight: int
    location_area_encounters: str
    types: list[TypeSchema] = []
    stats: list[StatSchema] = []
    abilities: list[AbilitySchema] = []
    last_consulted: datetime

    class Config:
        """
        Aceppt ORM models
        """
        orm_mode = True
