import pytest
from fastapi.testclient import TestClient
import json
import os
import sys
# Assuming the test file is located in the tests directory
current_dir = os.path.dirname(os.path.realpath(__file__))

# Go up two directories to reach the project root
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))

# Add the project root to the Python path
sys.path.append(project_root)
from backend.model import PokemonModel
from backend.main import get_pokemon_by_id, get_all_pokemon, post_pokemon, put_pokemon, delete_pokemon, app


client = TestClient(app)
class TestGet:
    VALID_DATA = {
        "id": 25,
        "name": {"english": "Pikachu", "japanese": "ピカチュウ", "chinese": "皮卡丘", "french": "Pikachu"},
        "type": ["Electric"],
        "base": {"HP": 35, "Attack": 55, "Defense": 40, "Speed": 90, "Special Attack": 50, "Special Defense": 50}
    }

    VALID_PMON = PokemonModel(**VALID_DATA)

    INVALID_DATA = {
            "id": 25,
            "type": ["Electric"],
            "base": {"HP": 35, "Attack": 55, "Defense": 40, "Speed": 90, "Special Attack": 50, "Special Defense": 50},
    }

    @staticmethod
    def test_get_all_pokemon():
        response = client.get("/api/v1/allpokemon")
        assert response.status_code == 200
        assert response.json().count() == 808

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