import pytest
from fastapi.testclient import TestClient
import json
import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.append(project_root)
from backend.model import NameTranslations, PokemonModel
from backend.main import get_pokemon_by_id, get_all_pokemon, post_pokemon, put_pokemon, delete_pokemon, app
class TestGet:
    VALID_DATA = {"id": 25,
            "name": {"english": "Pikachu", "japanese": "ピカチュウ", "chinese": "皮卡丘", "french": "Pikachu"},
            "type": ["Electric"],
            "base": {"HP": 35, "Attack": 55, "Defense": 40, "Speed": 90, "Special Attack": 50, "Special Defense": 50}}

    VALID_PMON = PokemonModel(**VALID_DATA)
    @staticmethod
    def test_get_all_pokemon():
        pass

    @staticmethod
    def test_get_pokemon_by_id():
        pass

class TestPost:

    @staticmethod
    def test_post_one_pokemon():
        pass

class TestPut:

    @staticmethod
    def test_put_one_pokemon():
        pass

class TestDelete:

    @staticmethod
    def test_delete_one_pokemon():
        pass