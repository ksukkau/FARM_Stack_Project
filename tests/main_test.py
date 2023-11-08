import pytest
from fastapi.testclient import TestClient
import os
import sys
from unittest.mock import AsyncMock, patch

current_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.append(project_root)
from backend.main import app

client = TestClient(app)

class TestPokemonAPI:

    @pytest.fixture
    def mock_fetch_one_pokemon(self):
        async def fetch_one_pokemon_mock(p_id: int):
            if p_id == 1:
                return {"id": 1, "name": "Pikachu", "type": "Electric"}
            return None
        return fetch_one_pokemon_mock

    @pytest.fixture
    def mock_fetch_all_pokemon(self):
        async def fetch_all_pokemon_mock():
            return [{"id": 1, "name": "Pikachu", "type": "Electric"}]
        return fetch_all_pokemon_mock

    @pytest.fixture
    def mock_create_pokemon(self):
        async def create_pokemon_mock(pokemon_data):
            return pokemon_data
        return create_pokemon_mock

    @pytest.fixture
    def mock_update_pokemon(self):
        async def update_pokemon_mock(p_id, pokemon_data):
            return pokemon_data
        return update_pokemon_mock

    @pytest.fixture
    def mock_delete_pokemon(self):
        async def delete_pokemon_mock(p_id):
            return f"Pokemon {p_id} deleted successfully"
        return delete_pokemon_mock

    def test_get_pokemon_by_id(self, mock_fetch_one_pokemon):
        with patch('backend.main.app.get_pokemon_by_id', new=mock_fetch_one_pokemon):
            response = client.get("/api/v1/pokemon/1")
            assert response.status_code == 200
            assert response.json() == {"id": 1, "name": "Pikachu", "type": "Electric"}

    def test_get_all_pokemon(self, mock_fetch_all_pokemon):
        with patch('backend.main.app.get_all_pokemon', new=mock_fetch_all_pokemon):
            response = client.get("/api/v1/allpokemon")
            assert response.status_code == 200
            assert len(response.json()) == 1

    def test_create_pokemon(self, mock_create_pokemon):
        with patch('backend.main.app.post_pokemon', new=mock_create_pokemon):
            new_pokemon = {"id": 2, "name": "Bulbasaur", "type": "Grass"}
            response = client.post("/api/v1/pokemon/", json=new_pokemon)
            assert response.status_code == 200
            assert response.json() == new_pokemon

    def test_update_pokemon(self, mock_update_pokemon):
        with patch('backend.main.app.put_pokemon', new=mock_update_pokemon):
            updated_pokemon = {"id": 1, "name": "Pikachu", "type": "Electric", "power": 100}
            response = client.put("/api/v1/pokemon/1", json=updated_pokemon)
            assert response.status_code == 200
            assert response.json() == updated_pokemon

    def test_delete_pokemon(self, mock_delete_pokemon):
        with patch('backend.main.app.delete_pokemon', new=mock_delete_pokemon):
            response = client.delete("/api/v1/pokemon/1")
            assert response.status_code == 200
            assert response.json() == "Pokemon 1 deleted successfully"

# class MockEndpoints:
#
#     @staticmethod
#     @pytest.mark.asyncio
#     async def mock_get_one_pokemon(p_id: int):
#         # Return a dummy Pokemon for testing
#         if p_id == 1:
#             return {"id": 1, "name": "Pikachu", "type": ["Electric"]}
#         else:
#             return None
#     @staticmethod
#     def mock_collection():
#         # Mock the 'collection' and its 'find' method to return a specified number of documents
#         documents = [{'id': 1}, {'id': 2}, {'id': 3}]  # Add example documents for testing
#         mock_cursor = AsyncMock()
#         mock_cursor.to_list = AsyncMock(return_value=documents)
#         mock_collection = AsyncMock()
#         mock_collection.find = AsyncMock(return_value=mock_cursor)
#         return mock_collection, documents
#
# class TestGet:
#     VALID_DATA = {
#         "id": 25,
#         "name": {"english": "Pikachu", "japanese": "ピカチュウ", "chinese": "皮卡丘", "french": "Pikachu"},
#         "type": ["Electric"],
#         "base": {"HP": 35, "Attack": 55, "Defense": 40, "Speed": 90, "Special Attack": 50, "Special Defense": 50}
#     }
#
#     VALID_PMON = PokemonModel(**VALID_DATA)
#
#     INVALID_DATA = {
#             "id": 25,
#             "type": ["Electric"],
#             "base": {"HP": 35, "Attack": 55, "Defense": 40, "Speed": 90, "Special Attack": 50, "Special Defense": 50},
#     }
#
#     class TestGet:
#         @staticmethod
#         @pytest.mark.asyncio
#         async def test_get_all_pokemon_status():
#             response = client.get("/api/v1/allpokemon")
#             assert response.status_code == 200
#
#         @staticmethod
#         @pytest.mark.asyncio
#         async def test_get_all_pokemon_count():
#             response = client.get("/api/v1/allpokemon")
#             data = response.json()
#             assert isinstance(data, list)
#
#         @staticmethod
#         @pytest.mark.asyncio
#         async def test_get_pokemon_by_id_status():
#             response = client.get("/api/v1/pokemon/{id}?p_id=10")
#             assert response.status_code == 200
#
#         @staticmethod
#         def test_get_pokemon_by_id_content():
#             response = client.get("/api/v1/pokemon/{id}?p_id=10")
#             data = response.json()
#             expected_keys = ['id', 'name', 'type']
#             for key in expected_keys:
#                 assert key in data
#

# class TestPost:
#
#     @staticmethod
#     def test_post_one_pokemon():
#         pass
#
# class TestPut:
#
#     @staticmethod
#     def test_put_one_pokemon():
#         pass
#
# class TestDelete:
#
#     @staticmethod
#     def test_delete_one_pokemon():
#         pass