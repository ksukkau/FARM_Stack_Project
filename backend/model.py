from pydantic import BaseModel, Field
import enum


class PType(str, enum.Enum):
    """Pokemon type"""
    normal = "normal"
    fire = "fire"
    water = "water"
    electric = "electric"
    grass = "grass"
    ice = "ice"
    fighting = "fighting"
    poison = "poison"
    ground = "ground"
    flying = "flying"
    psychic = "psychic"
    bug = "bug"
    rock = "rock"
    ghost = "ghost"
    dragon = "dragon"
    dark = "dark"
    steel = "steel"
    fairy = "fairy"

class Base(BaseModel):
    """Base stats"""
    HP: int
    Attack: int
    Defense: int
    Speed: int
    SpecialAttack: int
    SpecialDefense: int

class PokemonModel(BaseModel):
    """Main Pokemon model"""
    id: int
    name: str
    type: list
    base: Base = Field(
      alias="base",
      title="Base stats",
      description="Base stats for the Pokemon",
    )

