"""
The tabases models
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


Base = declarative_base()

class NamedEntity(Base):
    """
    Abstract class for all model that have a name and id.
    """
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, unique=True, index=True)


class Stat(NamedEntity):
    """
    Stat model of a Pokémon.
    """
    __tablename__ = 'stats'

class StatPokemon(Base):
    """
    Many to many relationship between Stat and Pokemon.
    """
    __tablename__ = 'stats_pokemons'
    stat_id = Column(Integer, ForeignKey('stats.id'), primary_key=True)
    pokemon_id = Column(Integer, ForeignKey('pokemons.id'), primary_key=True)

class Types(NamedEntity):
    """
    Type model of a Pokémon.
    """
    __tablename__ = 'types'

class TypePokemon(Base):
    """
    Many to many relationship between type and Pokemon.
    """
    __tablename__ = 'types_pokemons'
    type_id = Column(Integer, ForeignKey('types.id'), primary_key=True)
    pokemon_id = Column(Integer, ForeignKey('pokemons.id'), primary_key=True)

class Pokemon(NamedEntity):
    """
    A pokemon entity
    """
    __tablename__ = 'pokemons'
    weight = Column(Integer, nullable=False)
    location_area_encounters = Column(String(200), nullable=False)
    types = relationship('Types', secondary='types_pokemons')
    stats = relationship('Stat', secondary='stats_pokemons')
    abilities = relationship('Ability', secondary='abilities_pokemons')
    last_consulted = Column(DateTime, nullable=False)


class Ability(NamedEntity):
    """
    The ability of a Pokémonm, is no the same as pokemon move.
    """
    __tablename__ = 'abilities'

class AbilityPokemon(Base):
    """
    Many to many relationship between ability and Pokemon.
    """
    __tablename__ = 'abilities_pokemons'
    ability_id = Column(Integer, ForeignKey('abilities.id'), primary_key=True)
    pokemon_id = Column(Integer, ForeignKey('pokemons.id'), primary_key=True)