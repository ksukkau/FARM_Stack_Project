import os
import sys
import pytest_asyncio
import asyncio

import pytest
current_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.append(project_root)
from backend.database import fetch_one_pokemon, fetch_all_pokemon, create_pokemon, update_pokemon, upsert_pokemon_db, delete_pokemon_from_db
