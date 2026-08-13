# FARM Stack Pokémon API

## A Full-Stack Pokémon Application Built with FastAPI, React, and MongoDB

---

## 📋 Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Frontend Overview](#frontend-overview)
- [Database Schema](#database-schema)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## 🌟 Overview

The **FARM Stack Pokémon API** is a full-stack web application that allows users to explore, search, and manage Pokémon data. It leverages the power of the **FARM stack** — **F**astAPI, **A**sync MongoDB (Motor), **R**eact, and **M**ongoDB — to deliver a high-performance, scalable, and modern web experience.

Data is fetched and synchronized from the public [PokéAPI](https://pokeapi.co/), stored in a local MongoDB database for fast retrieval, and served through a custom-built RESTful FastAPI backend. The React frontend provides a clean, responsive interface for users to browse their favorite Pokémon.

> 🎯 **Goal:** Demonstrate a production-ready FARM stack application with real-world features like authentication, pagination, caching, and async data handling.

---

## 🛠️ Tech Stack

### Backend
| Technology | Purpose |
|---|---|
| **FastAPI** | High-performance Python web framework for building APIs |
| **Motor** | Async MongoDB driver for Python |
| **Pydantic v2** | Data validation and serialization |
| **Beanie ODM** | Async ODM (Object Document Mapper) for MongoDB |
| **Python-Jose** | JWT token creation and verification |
| **Passlib** | Password hashing (bcrypt) |
| **HTTPX** | Async HTTP client for PokéAPI requests |
| **Uvicorn** | ASGI server for running FastAPI |

### Frontend
| Technology | Purpose |
|---|---|
| **React 18** | UI component library |
| **TypeScript** | Type-safe JavaScript |
| **Vite** | Fast frontend build tool |
| **React Router v6** | Client-side routing |
| **TanStack Query** | Server-state management and caching |
| **Axios** | HTTP client for API requests |
| **Tailwind CSS** | Utility-first CSS framework |
| **Shadcn/UI** | Accessible and reusable UI components |
| **Zustand** | Lightweight state management |

### Database & Infrastructure
| Technology | Purpose |
|---|---|
| **MongoDB** | NoSQL document database |
| **MongoDB Atlas** | Cloud-hosted MongoDB (optional) |
| **Docker** | Containerization |
| **Docker Compose** | Multi-container orchestration |
| **Redis** | Optional caching layer |

---

## ✨ Features

### Core Features
- 🔍 **Search & Filter** — Search Pokémon by name, type, generation, or ability
- 📄 **Pagination** — Efficiently browse through 1000+ Pokémon with cursor-based pagination
- ⚡ **Async Architecture** — Fully async backend for maximum performance
- 🔄 **Data Sync** — Seed and sync Pokémon data from PokéAPI into MongoDB
- 📊 **Detailed Pokémon Profiles** — Stats, moves, abilities, evolutions, and sprites

### User Features
- 🔐 **Authentication** — JWT-based user registration and login
- ❤️ **Favorites** — Authenticated users can save favorite Pokémon
- 🏆 **Teams** — Build and manage custom Pokémon teams
- 🧩 **Compare Mode** — Compare stats between two Pokémon side-by-side

### Developer Features
- 📖 **Auto-Generated Docs** — Swagger UI and ReDoc available out of the box
- 🐳 **Docker Support** — Full Docker and Docker Compose configuration
- 🧪 **Test Suite** — Pytest for backend, Vitest for frontend
- 🔧 **Environment Configuration** — `.env`-based configuration management

---

## 📁 Project Structure

```
farm-stack-pokemon/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                  # FastAPI app entry point
│   │   ├── config.py                # App configuration & settings
│   │   ├── database.py              # MongoDB connection setup
│   │   │
│   │   ├── models/                  # Beanie/Pydantic models
│   │   │   ├── __init__.py
│   │   │   ├── pokemon.py           # Pokémon document model
│   │   │   ├── user.py              # User document model
│   │   │   └── team.py              # Team document model
│   │   │
│   │   ├── routers/                 # API route handlers
│   │   │   ├── __init__.py
│   │   │   ├── pokemon.py           # Pokémon CRUD routes
│   │   │   ├── auth.py              # Auth routes (login/register)
│   │   │   ├── users.py             # User profile routes
│   │   │   └── teams.py             # Team management routes
│   │   │
│   │   ├── services/                # Business logic layer
│   │   │   ├── __init__.py
│   │   │   ├── pokemon_service.py   # Pokémon data operations
│   │   │   ├── auth_service.py      # Auth logic (JWT, hashing)
│   │   │   └── pokeapi_service.py   # PokéAPI sync service
│   │   │
│   │   ├── schemas/                 # Request/Response Pydantic schemas
│   │   │   ├── __init__.py
│   │   │   ├── pokemon.py
│   │   │   ├── user.py
│   │   │   └── team.py
│   │   │
│   │   └── dependencies/            # FastAPI dependency injection
│   │       ├── __init__.py
│   │       └── auth.py              # get_current_user dependency
│   │
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── conftest.py
│   │   ├── test_pokemon.py
│   │   ├── test_auth.py
│   │   └── test_teams.py
│   │
│   ├── scripts/
│   │   └── seed_pokemon.py          # Script to seed DB from PokéAPI
│   │
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── public/
│   │   └── pokeball.svg
│   │
│   ├── src/
│   │   ├── main.tsx                 # React app entry point
│   │   ├── App.tsx                  # Root component with routing
│   │   │
│   │   ├── api/                     # Axios API client functions
│   │   │   ├── axiosClient.ts
│   │   │   ├── pokemon.ts
│   │   │   ├── auth.ts
│   │   │   └── teams.ts
│   │   │
│   │   ├── components/              # Reusable UI components
│   │   │   ├── ui/                  # Shadcn/UI base components
│   │   │   ├── PokemonCard.tsx
│   │   │   ├── PokemonGrid.tsx
│   │   │   ├── SearchBar.tsx
│   │   │   ├── TypeBadge.tsx
│   │   │   ├── StatBar.tsx
│   │   │   ├── Navbar.tsx
│   │   │   └── Pagination.tsx
│   │   │
│   │   ├── pages/                   # Page-level components
│   │   │   ├── HomePage.tsx
│   │   │   ├── PokemonDetailPage.tsx
│   │   │   ├── LoginPage.tsx
│   │   │   ├── RegisterPage.tsx
│   │   │   ├── ProfilePage.tsx
│   │   │   ├── TeamsPage.tsx
│   │   │   └── ComparePage.tsx
│   │   │
│   │   ├── hooks/                   # Custom React hooks
│   │   │   ├── usePokemon.ts
│   │   │   ├── useAuth.ts
│   │   │   └── useTeams.ts
│   │   │
│   │   ├── store/                   # Zustand global state
│   │   │   ├── authStore.ts
│   │   │   └── filterStore.ts
│   │   │
│   │   └── types/                   # TypeScript type definitions
│   │       ├── pokemon.ts
│   │       ├── user.ts
│   │       └── team.ts
│   │
│   ├── index.html
│   ├── vite.config.ts
│   ├── tailwind.config.ts
│   ├── tsconfig.json
│   ├── Dockerfile
│   └── package.json
│
├── docker-compose.yml
├── docker-compose.prod.yml
├── .gitignore
├── .env.example
└── README.md
```

---

## ✅ Prerequisites

Before you begin, ensure you have the following installed on your machine:

| Tool | Version | Notes |
|---|---|---|
| **Python** | 3.11+ | Backend runtime |
| **Node.js** | 18+ | Frontend runtime |
| **npm** or **pnpm** | Latest | Package manager |
| **MongoDB** | 6.0+ | Local or Atlas |
| **Docker** | Latest | Optional, for containerized setup |
| **Docker Compose** | v2+ | Optional, for containerized setup |
| **Git** | Latest | Version control |

---

## 🚀 Installation & Setup

### Option 1: Docker Compose (Recommended)

The fastest way to get the entire stack running.

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/farm-stack-pokemon.git
cd farm-stack-pokemon

# 2. Copy and configure environment variables
cp .env.example .env

# 3. Build and start all services
docker-compose up --build

# 4. (Optional) Seed the database with Pokémon data
docker-compose exec backend python scripts/seed_pokemon.py --limit 151

# 5. Access the application
# Frontend:       http://localhost:5173
# Backend API:    http://localhost:8000
# API Docs:       http://localhost:8000/docs
# MongoDB:        mongodb://localhost:27017
```

---

### Option 2: Manual Local Setup

#### Step 1 — Clone the Repository

```bash
git clone https://github.com/yourusername/farm-stack-pokemon.git
cd farm-stack-pokemon
```

#### Step 2 — Backend Setup

```bash
# Navigate to the backend directory
cd backend

# Create and activate a virtual environment
python -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env
# Edit .env with your configuration (see Environment Variables section)
```

#### Step 3 — Seed the Database

```bash
# Make sure MongoDB is running, then run the seed script
python scripts/seed_pokemon.py --limit 151

# To seed all Pokémon (1010+):
python scripts/seed_pokemon.py --all

# To seed a specific generation:
python scripts/seed_pokemon.py --generation 1
```

#### Step 4 — Start the Backend Server

```bash
# From the /backend directory
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Step 5 — Frontend Setup

```bash
# Open a new terminal and navigate to the frontend directory
cd frontend

# Install Node dependencies
npm install
# or with pnpm:
pnpm install

# Copy environment file
cp .env.example .env
# Edit .env with your configuration

# Start the development server
npm run dev
```

---

## 🔐 Environment Variables

### Backend — `backend/.env`

```env
# ─── Application ───────────────────────────────────────────────
APP_NAME="FARM Stack Pokémon API"
APP_VERSION="1.0.0"
DEBUG=True
ENVIRONMENT=development    # development | staging | production

# ─── MongoDB ───────────────────────────────────────────────────
MONGODB_URL=mongodb://localhost:27017
MONGODB_DB_NAME=pokemon_db

# ─── JWT Authentication ─────────────────────────────────────────
SECRET_KEY=your-super-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# ─── PokéAPI ────────────────────────────────────────────────────
POKEAPI_BASE_URL=https://pokeapi.co/api/v2
POKEAPI_RATE_LIMIT=100       # requests per minute

# ─── CORS ───────────────────────────────────────────────────────
ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000

# ─── Redis (Optional Caching) ───────────────────────────────────
REDIS_URL=redis://localhost:6379
USE_REDIS_CACHE=False
CACHE_TTL_SECONDS=3600
```

### Frontend — `frontend/.env`

```env
# ─── API Configuration ──────────────────────────────────────────
VITE_API_BASE_URL=http://localhost:8000/api/v1
VITE_APP_NAME="FARM Stack Pokémon"

# ─── Feature Flags ──────────────────────────────────────────────
VITE_ENABLE_COMPARE=true
VITE_ENABLE_TEAMS=true
```

---

## 🏃 Running the Application

### Development Mode

```bash
# Start all services with Docker Compose (with hot-reload)
docker-compose up

# Or run individually:
# Terminal 1 - Backend
cd backend && uvicorn app.main:app --reload

# Terminal 2 - Frontend
cd frontend && npm run dev
```

### Production Mode

```bash
# Use the production compose file
docker-compose -f docker-compose.prod.yml up --build -d
```

---

## 📖 API Documentation

Once the backend is running, interactive API documentation is automatically available:

| Interface | URL | Description |
|---|---|---|
| **Swagger UI** | `http://localhost:8000/docs` | Interactive API explorer |
| **ReDoc** | `http://localhost:8000/redoc` | Clean API reference docs |
| **OpenAPI JSON** | `http://localhost:8000/openapi.json` | Raw OpenAPI schema |

---

### 🔵 Pokémon Endpoints

| Method | Endpoint | Auth Required | Description |
|---|---|---|---|
| `GET` | `/api/v1/pokemon` | ❌ | List all Pokémon (paginated) |
| `GET` | `/api/v1/pokemon/{id_or_name}` | ❌ | Get a specific Pokémon |
| `GET` | `/api/v1/pokemon/types` | ❌ | List all Pokémon types |
| `GET` | `/api/v1/pokemon/search` | ❌ | Search Pokémon by query |
| `POST` | `/api/v1/pokemon/sync` | ✅ Admin | Sync data from PokéAPI |

#### Example: List Pokémon

```http
GET /api/v1/pokemon?page=1&limit=20&type=fire&generation=1
```

```json
{
  "data": [
    {
      "id": 4,
      "name": "charmander",
      "types": ["fire"],
      "base_stats": {
        "hp": 39,
        "attack": 52,
        "defense": 43,
        "special_attack": 60,
        "special_defense": 50,
        "speed": 65
      },
      "sprites": {
        "front_default": "https://raw.githubusercontent.com/...",
        "official_artwork": "https://raw.githubusercontent.com/..."
      },
      "generation": 1,
      "height": 6,
      "weight": 85
    }
  ],
  "total": 78,
  "page": 1,
  "limit": 20,
  "pages": 4
}
```

---

### 🔴 Authentication Endpoints

| Method | Endpoint | Auth Required | Description |
|---|---|---|---|
| `POST` | `/api/v1/auth/register` | ❌ | Register a new user |
| `POST` | `/api/v1/auth/login` | ❌ | Login and receive tokens |
| `POST` | `/api/v1/auth/refresh` | ❌ | Refresh access token |
| `POST` | `/api/v1/auth/logout` | ✅ | Logout (invalidate token) |

#### Example: Register User

```http
POST /api/v1/auth/register
Content-Type: application/json

{
  "username": "ashketchum",
  "email": "ash@pallet.town",
  "password": "pikachu123"
}
```

```json
{
  "message": "User registered successfully",
  "user": {
    "id": "64f1b2c3d4e5f6a7b8c9d0e1",
    "username": "ashketchum",
    "email": "ash@pallet.town",
    "created_at": "2024-01-15T10:30:00Z"
  }
}
```

---

### 🟢 User Endpoints

| Method | Endpoint | Auth Required | Description |
|---|---|---|---|
| `GET` | `/api/v1/users/me` | ✅ | Get current user profile |
| `PUT` | `/api/v1/users/me` | ✅ | Update current user profile |
| `GET` | `/api/v1/users/me/favorites` | ✅ | Get user's favorite Pokémon |
| `POST` | `/api/v1/users/me/favorites/{pokemon_id}` | ✅ | Add a favorite |
| `DELETE` | `/api/v1/users/me/favorites/{pokemon_id}` | ✅ | Remove a favorite |

---

### 🟡 Teams Endpoints

| Method | Endpoint | Auth Required | Description |
|---|---|---|---|
| `GET` | `/api/v1/teams` | ✅ | Get all teams for current user |
| `POST` | `/api/v1/teams` | ✅ | Create a new team |
| `GET` | `/api/v1/teams/{team_id}` | ✅ | Get a specific team |
| `PUT` | `/api/v1/teams/{team_id}` | ✅ | Update a team |
| `DELETE` | `/api/v1/teams/{team_id}` | ✅ | Delete a team |
| `POST` | `/api/v1/teams/{team_id}/pokemon/{pokemon_id}` | ✅ | Add Pokémon to team |
| `DELETE` | `/api/v1/teams/{team_id}/pokemon/{pokemon_id}` | ✅ | Remove Pokémon from team |

---

## 🗄️ Database Schema

### Pokémon Collection (`pokemon`)

```python
class Pokemon(Document):
    pokemon_id: int                    # National Pokédex number
    name: str
    types: List[str]                   # e.g., ["fire", "flying"]
    abilities: List[Ability]
    base_stats: BaseStats
    sprites: Sprites
    moves: List[str]                   # Move names
    evolution_chain_id: Optional[int]
    generation: int
    height: int                        # in decimetres
    weight: int                        # in hectograms
    flavor_text: Optional[str]         # Pokédex entry
    created_at: datetime
    updated_at: datetime

    class Settings:
        name = "pokemon"
        indexes = [
            IndexModel([("name", 1)], unique=True),
            IndexModel([("pokemon_id", 1)], unique=True),
            IndexModel([("types", 1)]),
            IndexModel([("generation", 1)]),
        ]
```

### User Collection (`users`)

```python
class User(Document):
    username: str
    email: EmailStr
    hashed_password: str
    is_active: bool = True
    is_admin: bool = False
    favorites: List[PydanticObjectId] = []   # References to Pokémon docs
    created_at: datetime
    updated_at: datetime

    class Settings:
        name = "users"
        indexes = [
            IndexModel([("email", 1)], unique=True),
            IndexModel([("username", 1)], unique=True),
        ]
```

### Teams Collection (`teams`)

```python
class Team(Document):
    name: str
    description: Optional[str]
    owner: PydanticObjectId             # Reference to User
    pokemon: List[PydanticObjectId]     # Max 6 Pokémon
    is_public: bool = False
    created_at: datetime
    updated_at: datetime

    class Settings:
        name = "teams"
        indexes = [
            IndexModel([("owner", 1)]),
        ]
```

---

## 🧪 Testing

### Backend Tests (Pytest)

```bash
cd backend

# Install test dependencies (included in requirements.txt)
pip install pytest pytest-asyncio httpx

# Run all tests
pytest

# Run with verbose output
pytest -v

# Run a specific test file
pytest tests/test_pokemon.py -v

# Run with coverage report
pytest --cov=app --cov-report=html

# Open coverage report
open htmlcov/index.html
```

### Frontend Tests (Vitest)

```bash
cd frontend

# Run all tests
npm run test

# Run in watch mode
npm run test:watch

# Run with UI
npm run test:ui

# Coverage report
npm run test:coverage
```

### Example Backend Test

```python
# tests/test_pokemon.py
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_get_pokemon_list():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/pokemon?limit=10")
    
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) <= 10
    assert "total" in data

@pytest.mark.asyncio
async def test_get_pokemon_by_name():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/pokemon/pikachu")
    
    assert response.status_code == 200
    pokemon = response.json()
    assert pokemon["name"] == "pikachu"
    assert "electric" in pokemon["types"]
```

---

## 🐳 Docker Configuration

### `docker-compose.yml`

```yaml
version: "3.9"

services:
  mongodb:
    image: mongo:6.0
    container_name: pokemon_mongodb
    restart: unless-stopped
    ports:
      - "27017:27017"
    volumes:
      - mongodb_data:/data/db
    environment:
      MONGO_INITDB_DATABASE: pokemon_db

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: pokemon_backend
    restart: unless-stopped
    ports:
      - "8000:8000"
    env_file:
      - ./backend/.env
    depends_on:
      - mongodb
    volumes:
      - ./backend:/app
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: pokemon_frontend
    restart: unless-stopped
    ports:
      - "5173:5173"
    env_file:
      - ./frontend/.env
    depends_on:
      - backend
    volumes:
      - ./frontend:/app
      - /app/node_modules

  redis:
    image: redis:7-alpine
    container_name: pokemon_redis
    restart: unless-stopped
    ports:
      - "6379:6379"

volumes:
  mongodb_data:
```

---

## 🚢 Deployment

### Deploying to a VPS (e.g., DigitalOcean, AWS EC2)

```bash
# 1. SSH into your server
ssh user@your-server-ip

# 2. Clone the repository
git clone https://github.com/yourusername/farm-stack-pokemon.git
cd farm-stack-pokemon

# 3. Configure production environment variables
cp .env.example .env
nano .env   # Set production values

# 4. Run with the production compose file
docker-compose -f docker-compose.prod.yml up -d --build

# 5. Seed the database
docker-compose exec backend python scripts/seed_pokemon.py --all
```

### Deploying to MongoDB Atlas

1. Create a free cluster at [mongodb.com/atlas](https://www.mongodb.com/atlas)
2. Get your connection string
3. Update your `MONGODB_URL` in `.env`:
   ```env
   MONGODB_URL=mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/pokemon_db?retryWrites=true&w=majority
   ```

### Frontend Deployment (Vercel / Netlify)

```bash
cd frontend

# Build the production bundle
npm run build

# The dist/ folder is ready to deploy
# Point your hosting provider to: frontend/dist
```

> ⚠️ **Important:** Update `VITE_API_BASE_URL` in your frontend `.env` to point to your production backend URL before building.

---

## 🤝 Contributing

Contributions are welcome and greatly appreciated! Here's how to get started:

1. **Fork** the repository
2. **Create** your feature branch:
   ```bash
   git checkout -b feature/add-pokemon-compare
   ```
3. **Commit** your changes following [Conventional Commits](https://www.conventionalcommits.org/):
   ```bash
   git commit -m "feat: add side-by-side Pokémon comparison page"
   ```
4. **Push** to your branch:
   ```bash
   git push origin feature/add-pokemon-compare
   ```
5. **Open** a Pull Request with a clear description of your changes

### Code Style

- **Python:** Follow [PEP 8](https://pep8.org/). Use `black` for formatting and `ruff` for linting.
- **TypeScript/React:** Follow the project's ESLint and Prettier configuration.
- **Commits:** Use Conventional Commits format (`feat:`, `fix:`, `docs:`, `chore:`, etc.)

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](./LICENSE) file for details.

---

## 🙏 Acknowledgements

- [PokéAPI](https://pokeapi.co/) — The fantastic free Pokémon data API
- [FastAPI](https://fastapi.tiangolo.com/) — The modern Python web framework
- [Beanie ODM](https://beanie-odm.dev/) — Async MongoDB ODM
- [Shadcn/UI](https://ui.shadcn.com/) — Beautiful UI components
- [TanStack Query](https://tanstack.com/query) — Powerful data synchronization

---

<div align="center">

**Made with ❤️ and lots of Pokéballs**

⭐ If you found this project helpful, please give it a star!

</div>
* #### SAMPLE REQUESTS
    `{{URL}}pokemon/3`
