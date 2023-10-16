from model import PokemonModel
#mongoDB driver
import motor.motor_asyncio

#testing database
"""client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
database = client.test
collection = database.pokemons"""

#live database
mongo_uri = "mongodb+srv://kat:urIQ2tDuTmDBRY6I@cluster0.sp6xasb.mongodb.net/Pokemon?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)
database = client.get_database("Pokemon")
collection = database.get_collection("pokemons")


async def fetch_one_pokemon(id: int):
    """Fetch one pokemon from the database"""
    document = await collection.find_one({"id": id})
    if document:
        # Deserialize the MongoDB document into a Python object using the Pydantic model
        pokemon = PokemonModel(**document)
        return pokemon
    return None


async def fetch_all_pokemon():
    """Fetch all pokemon from the database"""
    cursor = collection.find({})
    documents = await cursor.to_list(809)
    # Deserialize the list of documents into a list of Python objects
    pokemons = [PokemonModel(**document) for document in documents]
    return pokemons

async def create_pokemon(pokemon: PokemonModel):
    """Create a new pokemon in the database"""
    # Serialize the Python object into a dictionary
    document = pokemon.dict()
    result = await collection.insert_one(document)
    return result


async def update_pokemon(id: int, pokemon: PokemonModel):
    """Update a pokemon in the database"""
    # Serialize the Python object into a dictionary
    document = pokemon.dict()
    result = await collection.update_one({"id": id}, {"$set": document})
    return result

async def delete_pokemon(id: int):
    """Delete a pokemon in the database"""
    result = await collection.delete_one({"id": id})
    return result