"""
This module provides functions for performing database operations with Pokémon
    data using Pydantic models.

It includes functions for fetching, creating, updating, and deleting Pokémon
    records in a MongoDB database.

Author: Kat Sukkau
Date: Oct 2023
"""
from model import PokemonModel
#mongoDB driver
import motor.motor_asyncio

#testing database
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
database = client.test
collection = database.pokemons


async def fetch_one_pokemon(p_id: int):
    """Fetch one Pokémon from the database"""
    document = await collection.find_one({"id": p_id})
    if document:
        # Deserialize the MongoDB document into a Python object using the Pydantic model
        pokemon = PokemonModel(**document)
        return pokemon
    return None


async def fetch_all_pokemon():
    """Fetch all Pokémon from the database"""
    cursor = collection.find({})
    documents = await cursor.to_list(809)
    # Deserialize the list of documents into a list of Python objects
    pokemons = [PokemonModel(**document) for document in documents]
    return pokemons

async def create_pokemon(pokemon: PokemonModel):
    """Create a new Pokémon in the database"""
    # Serialize the Python object into a dictionary

    document = pokemon.dict()
    spatk = document['base']['SpecialAttack']
    spdef = document['base']['SpecialDefense']
    del document['base']['SpecialAttack']
    del document['base']['SpecialDefense']
    document['base']['Special Attack'] = spatk
    document['base']['Special Defense'] = spdef
    result = await collection.insert_one(document)
    inserted_id = result.inserted_id
    created_pmon = await collection.find_one({"_id": inserted_id})
    return created_pmon


async def update_pokemon(p_id: int, pokemon: PokemonModel):
    """Update a Pokémon in the database"""
    # Serialize the Python object into a dictionary
    document = pokemon.dict()
    spatk = document['base']['SpecialAttack']
    spdef = document['base']['SpecialDefense']
    del document['base']['SpecialAttack']
    del document['base']['SpecialDefense']
    document['base']['Special Attack'] = spatk
    document['base']['Special Defense'] = spdef
    result = await collection.update_one({"id": p_id}, {"$set": document})

    return result

async def delete_pokemon(p_id: int):
    """Delete a Pokémon in the database"""
    result = await collection.delete_one({"id": p_id})
    return result
