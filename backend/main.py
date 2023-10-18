import json

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import fetch_one_pokemon, fetch_all_pokemon, create_pokemon, update_pokemon
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
async def get_pokemon_by_id(id):
  if not id.isdigit():
    raise HTTPException(status_code=400, detail=f"Please enter an integer")
  response = await fetch_one_pokemon(int(id))
  if response:
    return response
  raise HTTPException(status_code=404, detail=f"Pokemon with ID {id} not found")

@app.get("/api/v1/allpokemon")
async def get_all_pokemon():
  response = await fetch_all_pokemon()
  if response:
    return response
  raise HTTPException(status_code=400, detail="Oops something went wrong / Bad Request")


from fastapi import HTTPException


@app.post("/api/v1/pokemon/", response_model=PokemonModel)
async def post_pokemon(pokemon: PokemonModel):
  try:
    result = await create_pokemon(pokemon)
    if result:
      return result
    else:
      raise HTTPException(status_code=500, detail="Failed to create the Pokémon")
  except Exception as e:
    raise HTTPException(status_code=400, detail=str(e))

@app.put("/api/v1/pokemon/{id}", response_model=PokemonModel)
async def put_pokemon(id: int, pokemon: PokemonModel):
  if not id:
    raise HTTPException(status_code=400, detail="Please enter an integer ID")

  try:
    # Attempt to update the Pokemon in the database
    result = await update_pokemon(id, pokemon)

    # Check if the update was acknowledged and return the updated Pokemon
    if result.acknowledged:
      updated_pokemon = await fetch_one_pokemon(id)
      if updated_pokemon:
        return updated_pokemon
      raise HTTPException(status_code=404, detail=f"Pokemon with ID {id} not found")

    # If the update was not acknowledged, return a 404 error
    raise HTTPException(status_code=404, detail=f"Pokemon with ID {id} not found")
  except Exception as e:
    raise HTTPException(status_code=400, detail=str(e))

@app.delete("/api/v1/pokemon/{id}")
async def delete_pokemon(id: str):
  if not id.isdigit():
    raise HTTPException(status_code=400, detail="Please enter an integer ID")

  try:
    response = await delete_pokemon(int(id))
    if response:
      return response
    raise HTTPException(status_code=404, detail=f"Pokemon with ID {id} not found")
  except Exception as e:
    raise HTTPException(status_code=400, detail=str(e))
