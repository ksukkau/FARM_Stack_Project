"""
This module provides functions for performing database operations with Pokémon
    data using Pydantic models.

It includes functions for fetching, creating, updating, and deleting Pokémon
    records in a MongoDB database.

Author: Kat Sukkau
Date: Oct 2023
"""
from decouple import config
from backend.model import PokemonModel
#mongoDB driver
import motor.motor_asyncio


#testing database
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
database = client.test
collection = database.pokemons

#live database
mongo_uri = config('DB_URL')
"""
client = motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)
database = client.get_database("Pokemon")
collection = database.get_collection("pokemons")"""


async def fetch_one_pokemon(p_id: int):
    """Fetch one Pokémon from the database"""
    document = await collection.find_one({"id": {"$eq": p_id}})
    if document:
        # Deserialize the MongoDB document into a Python object using the Pydantic model
        pokemon = PokemonModel(**document)
        return pokemon
    return None


async def fetch_all_pokemon():
    """Fetch all Pokémon from the database"""
    cursor = collection.find({})
    documents = []
    while True:
        document = await cursor.to_list(100)
        if document:
            documents.extend(document)
        else:
            break
    # Deserialize the list of documents into a list of Python objects
    pokemons = [PokemonModel(**document) for document in documents]
    return pokemons

async def create_pokemon(pokemon: PokemonModel):
    """Create a new Pokémon in the database"""
    result = await collection.insert_one(pokemon.dump())
    inserted_id = result.inserted_id
    created_pmon = await collection.find_one({"_id": inserted_id})
    return created_pmon


async def update_pokemon(p_id: int, pokemon: PokemonModel):
    """Update a Pokémon in the database"""
    result = await collection.update_one({"id": {"$eq": p_id}}, {"$set": pokemon.dump()})

    return result

async def upsert_pokemon_db(p_id: int, pokemon: PokemonModel):
    """Update if exists insert if not"""
    result = await collection.update_one(filter={"id": {"$eq": p_id}}, update={"$set": pokemon.dump()},upsert=True)
    return result

async def delete_pokemon_from_db(p_id: int):
    """Delete a Pokémon in the database"""
    result = await collection.delete_one({"id": {"$eq": p_id}})
    if result.deleted_count == 1:
        return {"message": f"Deletion of Pokemon {p_id} successful"}
    else:
        return {"message": "No document found for deletion"}
