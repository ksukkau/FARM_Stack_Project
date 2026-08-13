# FARM Stack Pokémon API

A full-stack Pokémon application built with **FastAPI**, **React**, and **MongoDB**.

---

## Overview

This project is a custom REST API for storing and managing Pokémon data, backed by MongoDB and served through FastAPI, with a React frontend.

## Tech Stack

**Backend**
- FastAPI 0.65.1
- Motor 2.4.0 (async MongoDB driver)
- Pydantic (v1.x)
- python-decouple (environment config)
- httpx (used to pull seed data from an external Pokémon JSON source)
- Uvicorn

**Frontend**
- React 18
- React Router 6
- React Bootstrap / Bootstrap 5
- Axios

**Database**
- MongoDB (Atlas or local)

## Challenges

Faced significant challenges getting the data to match the source data, specifically around the space in the `Special Attack` and `Special Defense` field names. Using a Pydantic alias wasn't inserting into the database correctly. This was resolved by editing the dictionaries before insertion — the alias correctly handles reading the data back out, but insertion required the pre-edited dict.

---

## Prerequisites

- Python 3.10
- [pipenv](https://pipenv.pypa.io/)
- Node.js and npm
- A MongoDB instance (local or Atlas)

## Installation & Setup

### Backend

```bash
cd backend
pipenv install
pipenv shell
```

Create a `.env` file inside `backend/` with your MongoDB connection string:

```env
DB_URL=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/Pokemon?retryWrites=true&w=majority
```

Start the API:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`, with interactive docs at `http://localhost:8000/docs`.

### Frontend

```bash
cd frontend
npm install
npm start
```

The app will be available at `http://localhost:3000`.

### Running Tests

```bash
pytest tests/model_test.py -v
```

(Also see `tests/database_test.py` and `tests/main_test.py`.)

---

## Pokémon Schema

| Field | Type | Notes |
|---|---|---|
| `id` | Number | |
| `name` | Object | see below |
| `name.english` | String | |
| `name.japanese` | String | |
| `name.chinese` | String | |
| `name.french` | String | |
| `type` | List[String] | |
| `base` | Object | see below |
| `base.HP` | Integer | |
| `base.Attack` | Integer | |
| `base.Defense` | Integer | |
| `base.Speed` | Integer | |
| `base.Special Attack` | Integer | note the space in the field name |
| `base.Special Defense` | Integer | note the space in the field name |

---

## API Routes

### Get All Pokémon

Retrieves all database records.

- **URL:** `/api/v1/allpokemon`
- **Method:** `GET`
- **URL Params:** none
- **Body Params:** none

**Success Response**
- Code: `200`
- Content: `{List of all Pokemon}`

**Sample Request**
```
{{URL}}allpokemon
```

---

### Create a New Pokémon

Adds a new Pokémon to the database.

- **URL:** `/api/v1/pokemon/`
- **Method:** `POST`
- **Body Params (required, JSON):**
  - `id`: Integer
  - `name`: Object
    - `english`: String
    - `japanese`: String
    - `chinese`: String
    - `french`: String
  - `type`: List[String]
  - `base`: Object
    - `HP`: Integer
    - `Attack`: Integer
    - `Defense`: Integer
    - `Speed`: Integer
    - `Special Attack`: Integer
    - `Special Defense`: Integer

**Responses**
- Success — Code: `200` — Content: the created Pokémon document
- Error — Code: `400` — Content: `{"detail": "<error message>"}` (e.g. on a validation failure or duplicate key)

**Sample Request**
```
{{URL}}/api/v1/pokemon

body:
{
  "name": {
    "english": "New Pokemon",
    "japanese": "フシギバナ",
    "chinese": "妙蛙花",
    "french": "Florizarre"
  },
  "base": {
    "HP": 80,
    "Attack": 82,
    "Defense": 83,
    "Speed": 80,
    "Special Attack": 100,
    "Special Defense": 100
  },
  "id": 9000,
  "type": ["Grass", "Poison"]
}
```

---

### Get a Pokémon by ID

Fetches a single record using the Pokémon id.

- **URL:** `/api/v1/pokemon/:id`
- **Method:** `GET`
- **URL Params (required):** `id=[integer]`
- **Body Params:** none

**Responses**
- Success — Code: `200` — Content: the matching Pokémon document
- Error — Code: `404` — Content: `{"detail": "Pokémon with ID <id> not found"}`
- Error — Code: `422` — if `id` is not a valid integer

**Sample Request**
```
{{URL}}pokemon/3
```

---

### Upsert Pokémon Document

Inserts or updates a Pokémon; requires the full Pokémon document.

- **URL:** `/api/v1/pokemon/:id`
- **Method:** `POST`
- **URL Params (required):** `id=[integer]`
- **Body Params (required, JSON):** same shape as *Create a New Pokémon*

**Responses**
- Success — Code: `200` — Content: the upserted Pokémon document
- Error — Code: `400` — Content: `{"detail": "<error message>"}`
- Error — Code: `404` — Content: `{"detail": "Pokemon with ID <id> not found"}` (if the upsert didn't return a document)

**Sample Request**
```
{{URL}}/api/v1/pokemon/3

body:
{
  "name": {
    "english": "New Pokemon",
    "japanese": "フシギバナ",
    "chinese": "妙蛙花",
    "french": "Florizarre"
  },
  "base": {
    "HP": 80,
    "Attack": 82,
    "Defense": 83,
    "Speed": 80,
    "Special Attack": 100,
    "Special Defense": 100
  },
  "id": 9000,
  "type": ["Grass", "Poison"]
}
```

---

### Update Pokémon Document

Updates a Pokémon; does not require the full document.

- **URL:** `/api/v1/pokemon/:id`
- **Method:** `PUT`
- **URL Params (required):** `id=[integer]`
- **Body Params (required, JSON):** full Pokémon document (same shape as *Create a New Pokémon*)

**Responses**
- Success — Code: `200` — Content: the updated Pokémon document
- Error — Code: `400` — Content: `{"detail": "<error message>"}`
- Error — Code: `404` — Content: `{"detail": "Pokemon with ID <id> not found"}` (if no matching record)

**Sample Request**
```
{{URL}}/api/v1/pokemon/3

body:
{
  "name": {
    "english": "New Pokemon",
    "japanese": "フシギバナ",
    "chinese": "妙蛙花",
    "french": "Florizarre"
  },
  "base": {
    "HP": 80,
    "Attack": 82,
    "Defense": 83,
    "Speed": 80,
    "Special Attack": 100,
    "Special Defense": 100
  },
  "id": 9000,
  "type": ["Grass", "Poison"]
}
```

---

### Delete Pokémon by ID

Deletes a single record using the Pokémon id.

- **URL:** `/api/v1/pokemon/:id`
- **Method:** `DELETE`
- **URL Params (required):** `id=[integer]`
- **Body Params:** none

**Responses**
- Success — Code: `200` — Content: `{"message": "Database update successful"}`
- Error — Code: `404` — Content: `{"detail": "Pokemon with ID <id> not found"}`

**Sample Request**
```
{{URL}}pokemon/3
```

---

### Reload Pokémon Database

Wipes the collection and reloads it fresh from the [pokemon.json](https://github.com/fanzeyi/pokemon.json) source data.

- **URL:** `/api/v1/pokemon/reload`
- **Method:** `POST`
- **URL Params:** none
- **Body Params:** none

**Responses**
- Success — Code: `200` — Content: `{"message": "Insert operation successful"}`
- Error — Code: `500` — Content: `{"detail": "Failed to reload the Pokémon"}`
- Error — Code: `400` — Content: `{"detail": "<error message>"}`

**Sample Request**
```
{{URL}}/api/v1/pokemon/reload
```

---

### Health Check

- **URL:** `/`
- **Method:** `GET`

**Responses**
- Success — Code: `200` — Content: `{"Hello": "World"}`

---
