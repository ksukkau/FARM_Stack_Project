import pytest
import os
import sys

# Get the current directory of the script
current_dir = os.path.dirname(os.path.realpath(__file__))

# Get the project root by going two directories up from the current directory
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))

# Add the project root to the Python path
sys.path.append(project_root)
from backend.model import NameTranslations, PokemonModel

class TestModel:

    @staticmethod
    def test_pokemon_model_validation():

        valid_pokemon_data = {
            "_id": {"$oid": "123456"},
            "id": 25,
            "name": {"english": "Pikachu", "japanese": "ピカチュウ", "chinese": "皮卡丘", "french": "Pikachu"},
            "type": ["Electric"],
            "base": {"HP": 35, "Attack": 55, "Defense": 40, "Speed": 90, "Special Attack": 50, "Special Defense": 50},
            "__v": 0
        }

        invalid_pokemon_data = {
            "id": 25,
            "type": ["Electric"],
            "base": {"HP": 35, "Attack": 55, "Defense": 40, "Speed": 90, "Special Attack": 50, "Special Defense": 50},
            "__v": 0
        }

        assert PokemonModel(**valid_pokemon_data)

        with pytest.raises(Exception):
            PokemonModel(**invalid_pokemon_data)

    @staticmethod
    def test_pokemon_model_serialization():
        # Create an instance of PokemonModel
        pokemon = PokemonModel(
            _id={"$oid": "123456"},
            id=25,
            name={"english": "Pikachu", "japanese": "ピカチュウ", "chinese": "皮卡丘", "french": "Pikachu"},
            type=["Electric"],
            base={"HP": 35, "Attack": 55, "Defense": 40, "Speed": 90, "Special Attack": 50, "Special Defense": 50},
            __v=1
        )
        # Test serialization and deserialization
        serialized_pokemon = pokemon.dump()
        print(serialized_pokemon)
        deserialized_pokemon = PokemonModel(**serialized_pokemon)
        print(deserialized_pokemon)
        assert pokemon == deserialized_pokemon

    @staticmethod
    def test_name_translation_accessible():
        name_translations = NameTranslations(english="Pikachu", japanese="ピカチュウ", chinese="皮卡丘", french="Pikachu")
        assert name_translations.english == "Pikachu"
        assert name_translations.japanese == "ピカチュウ"
        assert name_translations.chinese == "皮卡丘"
        assert name_translations.french == "Pikachu"

    @staticmethod
    def test_base_stats_accessible():
        pokemon = PokemonModel(
            _id={"$oid": "123456"},
            id=25,
            name={"english": "Pikachu", "japanese": "ピカチュウ", "chinese": "皮卡丘", "french": "Pikachu"},
            type=["Electric"],
            base={"HP": 35, "Attack": 55, "Defense": 40, "Speed": 90, "Special Attack": 50, "Special Defense": 50},
            __v=1
        )
        assert pokemon.base.HP == 35
        assert pokemon.base.Attack == 55
        assert pokemon.base.Defense == 40
        assert pokemon.base.Speed == 90
        assert pokemon.base.SpecialAttack == 50
        assert pokemon.base.SpecialDefense == 50