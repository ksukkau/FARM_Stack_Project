from pydantic import BaseModel, Field


class BaseStats(BaseModel):
    HP: int
    Attack: int
    Defense: int
    Speed: int
    SpecialAttack: int = Field(..., alias="Special Attack")
    SpecialDefense: int = Field(..., alias="Special Defense")

class NameTranslations(BaseModel):
    english: str
    japanese: str
    chinese: str
    french: str

class PokemonModel(BaseModel):
    _id: dict
    id: int
    name: NameTranslations
    type: list[str]
    base: BaseStats
    __v: int

    class Config:
        fields = {
            '_id': "$oid"
        }