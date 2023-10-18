"""
This module defines Pydantic models for representing Pokémon data.

The module includes three Pydantic models:
- BaseStats: Represents the base statistics of a Pokémon, including HP, Attack, Defense, Speed,
    Special Attack, and Special Defense.
- NameTranslations: Represents the translations of a Pokémon's name in different languages,
    including English, Japanese, Chinese, and French.
- PokemonModel: Combines the above models to represent a complete Pokémon, including an ID,
    name translations, types, base statistics, and a version field.

The models are used for data validation and serialization in Pokémon-related API endpoints.

Author: Kat Sukkau
Date: Oct 2023
"""

from pydantic import BaseModel, Field

class BaseStats(BaseModel):
    """
    Defines the 'base' stats of the Pokémon
    """
    HP: int
    Attack: int
    Defense: int
    Speed: int
    SpecialAttack: int = Field(..., alias="Special Attack")
    SpecialDefense: int = Field(..., alias="Special Defense")


class NameTranslations(BaseModel):
    """
    Defines list of included name translations
    """
    english: str
    japanese: str
    chinese: str
    french: str

class PokemonModel(BaseModel):
    """
    Defines Pokémon model
    """
    _id: dict
    id: int
    name: NameTranslations
    type: list[str]
    base: BaseStats
    __v: int

    class Config:
        """
        Creates unique id
        """
        fields = {
            '_id': "$oid"
        }