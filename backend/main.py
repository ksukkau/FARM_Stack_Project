from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import fetch_one_pokemon, fetch_all_pokemon
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