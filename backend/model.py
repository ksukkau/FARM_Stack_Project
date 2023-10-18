from pydantic import BaseModel, Field

class BaseStats(BaseModel):
    HP: int
    Attack: int
    Defense: int
    Speed: int
    SpecialAttack: int = Field(..., serialization_alias="Special Attack")
    SpecialDefense: int = Field(..., serialization_alias="Special Defense")
    SpecialAttack: int = Field(..., validation_alias="Special Attack")
    SpecialDefense: int = Field(..., validation_alias="Special Defense")

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