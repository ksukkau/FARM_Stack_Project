from model import PokemonModel
#mongoDB driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
database = client.PokemonList
collection = database.pokemon


async def fetch_one_pokemon(id: int):
    """Fetch one pokemon from the database"""
    document = await collection.find_one({"id": id})
    return document

async def fetch_all_pokemon():
    """Fetch all pokemon from the database"""
    cursor = collection.find({})
    documents = await cursor.to_list()
    return documents

async def create_pokemon(pokemon: PokemonModel):
    """Create a new pokemon in the database"""
    document = pokemon.dict()
    result = await collection.insert_one(document)
    return document

async def update_pokemon(id: int, pokemon: PokemonModel):
    """Update a pokemon in the database"""
    document = pokemon.dict()
    result = await collection.update_one({"id": id}, {"$set": document})
    return document

async def delete_pokemon(id: int):
    """Delete a pokemon in the database"""
    result = await collection.delete_one({"id": id})
    return result