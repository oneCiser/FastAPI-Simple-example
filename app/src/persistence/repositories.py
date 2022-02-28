"""
Module with the repositories from the persistence layer
"""
from datetime import datetime
from sqlalchemy.orm import exc, noload,  subqueryload
from sqlalchemy import or_
from fastapi import HTTPException
from .database import SessionLocal
from .models import Pokemon, Stat, Ability, Types

class PokemonRepositoryDB:
    """
    data access layer
    """
    def __init__(self) -> None:
        self.db_sesssion = SessionLocal
    def get(self, **kwargs):
        """
        Get the pokemon
        """
        with self.db_sesssion() as database:
            try:
                name = kwargs.get('name', "")
                id = kwargs.get('id', 0)
                query_response = database.query(Pokemon).options(
                    subqueryload(Pokemon.abilities),
                    subqueryload(Pokemon.types),
                    subqueryload(Pokemon.stats)
                    ).filter(or_(Pokemon.name==name, Pokemon.id==id)).first()
            except exc.NoResultFound as error:
                raise HTTPException(status_code=404, detail="Pokemon not found") from error
            except Exception as error:
                raise HTTPException(status_code=500, detail="Error getting the pokemon") from error
            return query_response
    def get_all(self, **kwargs):
        """
        Get all the pokemons
        """
        with self.db_sesssion() as database:
            limit = kwargs.get('limit', None)
            offset = kwargs.get('offset', 0)
            result = database.query(Pokemon).options(
                 subqueryload(Pokemon.abilities),
                 subqueryload(Pokemon.types),
                 subqueryload(Pokemon.stats)
            )
            result = result.offset(offset)
            if limit:
                result = result.limit(limit)
            return result.all()
    def save(self, **kwargs):
        """
        Save the pokemon
        """
        with self.db_sesssion() as database:
            database.begin()
            try:
                kwargs["last_consulted"] = datetime.now()
                abilities = kwargs.pop('abilities', [])
                types = kwargs.pop('types', [])
                stats = kwargs.pop('stats', [])
                pokemon = Pokemon(**kwargs)
                for abilitie in abilities:
                    abilty_dict = {
                        "name": abilitie["ability"]["name"]
                    }
                    exist_ability = database.query(Ability) \
                        .filter(Ability.name==abilty_dict["name"]).first()
                    if exist_ability:
                        pokemon.abilities.append(exist_ability)
                    else:
                        tmp_ability = Ability(**abilty_dict)
                        pokemon.abilities.append(tmp_ability)
                for typev in types:
                    type_dict = {
                        "name": typev["type"]["name"]
                    }
                    exist_type = database.query(Types).filter(Types.name==type_dict["name"]).first()
                    if exist_type:
                        pokemon.types.append(exist_type)
                    else:
                        tmp_type = Types(**type_dict)
                        pokemon.types.append(tmp_type)
                for stat in stats:
                    stat_dict = {
                        "name": stat["stat"]["name"]
                    }
                    exist_stat = database.query(Stat).filter(Stat.name==stat_dict["name"]).first()
                    if exist_stat:
                        pokemon.stats.append(exist_stat)
                    else:
                        tmp_stat = Stat(**stat_dict)
                        pokemon.stats.append(tmp_stat)

                database.add(pokemon)
            except Exception as error:
                database.rollback()
                raise HTTPException(status_code=500, detail="Error saving the pokemon") from error
            else:
                database.commit()
                database.refresh(pokemon)
                return pokemon

    def update(self, **kwargs):
        """
        update the pokemon
        """
        with self.db_sesssion() as database:
            try:
                query_name = kwargs.pop('name',"")
                query_id = kwargs.pop('id',0)
                query = or_(Pokemon.id == query_id, Pokemon.name == query_name)
                pokemon = database.query(Pokemon).options(
                    noload(Pokemon.types),
                    noload(Pokemon.abilities),
                    noload(Pokemon.stats)
                    ).filter(query).first()
                pokemon.last_consulted = datetime.now()
                if pokemon.location_area_encounters != kwargs.get('location_area_encounters', None):
                    pokemon.location_area_encounters = kwargs.get('location_area_encounters', None)
                if pokemon.weight != kwargs.get('weight', None):
                    pokemon.weight = kwargs.get('weight', None)
                database.commit()
            except exc.NoResultFound as error:
                raise HTTPException(status_code=404, detail="Pokemon not found") from error
            except Exception as error:
                raise HTTPException(status_code=500, detail="Error updating the pokemon") from error
            else:
                return pokemon
    async def save_or_update(self, **kwargs):
        """
        save or update the pokemon
        """
        with self.db_sesssion() as database:
            try:
                query_name = kwargs.get('name', None)
                query_id = kwargs.get('id', None)
                query_dict = {}
                if query_name:
                    query_dict['name'] = query_name
                    pokemon = database.query(Pokemon).filter(Pokemon.name==query_dict['name']).first()
                else:
                    query_dict['id'] = query_id
                    pokemon = database.query(Pokemon).filter(Pokemon.id==query_dict['id']).first()
                if pokemon:
                    current_pokemon = self.update(**kwargs)
                else:
                    current_pokemon = self.save(**kwargs)
            except Exception as error:
                raise HTTPException(status_code=500, detail="Error saving or updating the pokemon") \
                    from error
            else:
                return current_pokemon
                