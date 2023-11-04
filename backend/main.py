"""
Pokémon API Module

This module defines a FastAPI-based API for interacting with a database of Pokémon.
It includes endpoints for retrieving Pokémon, creating new Pokémon, updating existing Pokémon,
and deleting Pokémon records.

Endpoints:
- GET /api/v1/pokemon/{id}: Retrieve a Pokémon by its ID.
- GET /api/v1/allpokemon: Retrieve all Pokémon records.
- POST /api/v1/pokemon/: Create a new Pokémon record.
- PUT /api/v1/pokemon/{id}: Update an existing Pokémon record.
- DELETE /api/v1/pokemon/{id}: Delete a Pokémon record.

The module also incorporates CORS (Cross-Origin Resource Sharing) to allow requests from
a specific origin (http://localhost:3000 in this case).

Author: Kat Sukkau
Date: Oct 2023
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import fetch_one_pokemon, fetch_all_pokemon, create_pokemon, update_pokemon, delete_pokemon_from_db, upsert_pokemon_db
from model import PokemonModel


app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.get("/api/v1/pokemon/{id}")
async def get_pokemon_by_id(p_id:int):
  if not p_id:
    raise HTTPException(status_code=400, detail="Please enter an integer")
  response = await fetch_one_pokemon(p_id)
  if response:
    return response
  raise HTTPException(status_code=404, detail=f"Pokémon with ID {p_id} not found")

@app.get("/api/v1/allpokemon")
async def get_all_pokemon():
  response = await fetch_all_pokemon()
  if response:
    return response
  raise HTTPException(status_code=400, detail="Oops something went wrong / Bad Request")

@app.post("/api/v1/pokemon/", response_model=PokemonModel)
async def post_pokemon(pokemon: PokemonModel):
  try:
    result = await create_pokemon(pokemon)
    print(type(result))
    if result:
      return result
    raise HTTPException(status_code=500, detail="Failed to create the Pokémon")
  except Exception as e:
    raise HTTPException(status_code=400, detail=str(e))

@app.put("/api/v1/pokemon/{id}", response_model=PokemonModel)
async def put_pokemon(p_id: int, pokemon: PokemonModel):
  if not p_id:
    raise HTTPException(status_code=400, detail="Please enter an integer ID")

  try:
    # Attempt to update the Pokemon in the database
    result = await update_pokemon(p_id, pokemon)

    # Check if the update was acknowledged and return the updated Pokemon
    if result.acknowledged:
      updated_pokemon = await fetch_one_pokemon(p_id)
      if updated_pokemon:
        return updated_pokemon
    raise HTTPException(status_code=404, detail=f"Pokemon with ID {p_id} not found")

  except Exception as e:
    raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/v1/pokemon/{id}", response_model=PokemonModel)
async def upsert_pokemon(p_id: int, pokemon: PokemonModel):
  if not p_id:
    raise HTTPException(status_code=400, detail="Please enter an integer ID")
  try:
    result = await upsert_pokemon_db(p_id, pokemon)
    if result.acknowledged:
      updated_pokemon = await fetch_one_pokemon(p_id)
      if updated_pokemon:
        return updated_pokemon
    raise HTTPException(status_code=404, detail=f"Pokemon with ID {p_id} not found")

  except Exception as e:
    raise HTTPException(status_code=400, detail=str(e))



@app.delete("/api/v1/pokemon/{id}")
async def delete_pokemon(p_id: int):
  if not p_id:
    raise HTTPException(status_code=400, detail="Please enter an integer ID")

  try:
    response = await delete_pokemon_from_db(p_id)
    if response:
      return response
    raise HTTPException(status_code=404, detail=f"Pokemon with ID {p_id} not found")
  except Exception as e:
    raise HTTPException(status_code=400, detail=str(e))
