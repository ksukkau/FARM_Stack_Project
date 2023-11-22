"""
This module provides functions for performing database operations with Pokémon
    data using Pydantic models.

It includes functions for fetching, creating, updating, and deleting Pokémon
    records in a MongoDB database.

Author: Kat Sukkau
Date: Oct 2023
"""
from decouple import config
from model import PokemonModel
import httpx
#mongoDB driver
import motor.motor_asyncio
POKE_URL = "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/pokedex.json"

#testing database
# client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
# database = client.test
# collection = database.pokemons

#live database
mongo_uri = config('DB_URL')
client = motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)
database = client.get_database("Pokemon")
collection = database.get_collection("pokemons")


async def fetch_one_pokemon(p_id: int):
    """Fetch one Pokémon from the database"""
    document = await collection.find_one({"id": {"$eq": p_id}})
    if document:
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

async def reload_pokemon_db():
    """Delete all pokemon reload fresh data from source"""
    deleted = await collection.delete_many({})
    if deleted:
        data = await fetch_data_from_url(POKE_URL)
        if data:
            validated_data = validate_data(data)
            try:
                await collection.insert_many(validated_data)
                return "Insert operation successful"
            except Exception as e:
                return f"Insert operation failed with error: {str(e)}"
    return "No data to insert"

async def fetch_data_from_url(url):
    """Fetch Pokemon List from Source"""
    async with httpx.AsyncClient() as client2:
        response = await client2.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        response.raise_for_status()

def rename_keys(document):
    """Rename Keys to match model"""
    if "Sp. Attack" in document["base"]:
        document["base"]["Special Attack"] = document["base"].pop("Sp. Attack")
    if "Sp. Defense" in document["base"]:
        document["base"]["Special Defense"] = document["base"].pop("Sp. Defense")

def validate_data(data):
    """Validate data against model"""
    for doc in data:
        rename_keys(doc)
    validated_data = [PokemonModel(**item) for item in data]
    if validated_data:
        # convert back to dict to insert into database
        validated_data = [item.dump() for item in validated_data]
    return validated_data