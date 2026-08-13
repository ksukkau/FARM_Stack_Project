# FARM Stack Pokémon API

A full-stack Pokémon application built with **FastAPI**, **React**, and **MongoDB**.

---

## Overview

This project is a custom REST API for storing and managing Pokémon data, backed by MongoDB and served through FastAPI, with a React frontend.

## Tech Stack

- **FastAPI** — backend framework
- **MongoDB** — database
- **React** — frontend

## Challenges

Faced significant challenges getting the data to match the source data, specifically around the space in the `Special Attack` and `Special Defense` field names. Using a Pydantic alias wasn't inserting into the database correctly. This was resolved by editing the dictionaries before insertion — the alias correctly handles reading the data back out, but insertion required the pre-edited dict.

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

- **URL:** `/api/v1/pokemon`
- **Method:** `POST`
- **URL Params (required):** `after=[integer]`, `count=[integer]`
- **Body Params (required, JSON):**
  - `id`: Number, unique
  - `name`: Object
    - `english`: String, max 20 characters
    - `japanese`: String
    - `chinese`: String
    - `french`: String
  - `type`: String, enum `possibleTypes`
  - `base`: Object
    - `HP`: Number
    - `Attack`: Number
    - `Defense`: Number
    - `Speed`: Number
    - `Special Attack`: Number
    - `Special Defense`: Number

**Responses**
- Success — Code: `200` — Content: `{Submitted pokemon Json}`
- Error — Code: `400` — Content: `{"msg": "Pokemon id 900000 already exists"}`
- Error — Code: `400` — Content: `{"msg": "error message"}`

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
- Success — Code: `200` — Content: `{Submitted id pokemon Json}`
- Success — Code: `200` — Content: `{"msg": "Pokemon id <id> does not exist"}`
- Error — Code: `400` — Content: `{"msg": "Request failed: Id should be a number"}`

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
- Success — Code: `200` — Content: `{Pokemon id <id> updated successfully}`
- Success — Code: `200` — Content: `{"msg": "Pokemon id <id> does not exist"}`
- Error — Code: `400` — Content: `{"msg": "Request failed: Id should be a number"}`

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
- **Body Params (optional, JSON):** any subset of the Pokémon schema fields

**Responses**
- Success — Code: `200` — Content: `{Pokemon id <id> updated successfully}`
- Success — Code: `200` — Content: `{"msg": "Pokemon id 9000909 does not exist, no update performed"}`
- Error — Code: `400` — Content: `{"msg": "Request failed: Id should be a number"}`

**Sample Request**
```
{{URL}}/api/v1/pokemon/3

body:
{
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
- Success — Code: `200` — Content: `{"msg": "Pokemon id <id> deleted successfully"}`
- Success — Code: `200` — Content: `{"msg": "Pokemon id <id> does not exist"}`
- Error — Code: `400` — Content: `{"msg": "Request failed: Id should be a number"}`

**Sample Request**
```
{{URL}}pokemon/3
```

---

## License

_Add your license here._
