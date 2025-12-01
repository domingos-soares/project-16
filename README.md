# project-16 - FastAPI REST Server with PostgreSQL

A REST API server built with Python, FastAPI, and PostgreSQL supporting all CRUD operations (GET, POST, PUT, DELETE) plus a healthcheck endpoint.

**Created:** 01/12/2025

## Features

- ✅ Full CRUD operations (Create, Read, Update, Delete)
- ✅ PostgreSQL database with SQLAlchemy ORM
- ✅ Health check endpoint
- ✅ Automatic API documentation (Swagger UI & ReDoc)
- ✅ Docker Compose for easy database setup
- ✅ Pydantic validation

## Prerequisites

- Python 3.10+
- Docker and Docker Compose (for PostgreSQL)
- Or a local PostgreSQL installation

## Quick Start

### 1. Start PostgreSQL Database

Using Docker Compose (recommended):
```bash
docker-compose up -d
```

Or use your own PostgreSQL instance and update the `DATABASE_URL` in `.env`

### 2. Install Python Dependencies

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Database (Optional)

Copy `.env.example` to `.env` and update if needed:
```bash
cp .env.example .env
```

Default connection: `postgresql://postgres:postgres@localhost:5432/fastapi_db`

### 4. Run the Server

```bash
# Method 1: Direct
python main.py

# Method 2: With auto-reload (development)
uvicorn main:app --reload
```

The server will start at `http://localhost:8000`

## Project Structure

```
project-16/
├── main.py              # FastAPI application and routes
├── database.py          # Database connection and session
├── models.py            # SQLAlchemy ORM models
├── schemas.py           # Pydantic schemas for validation
├── requirements.txt     # Python dependencies
├── docker-compose.yml   # PostgreSQL container setup
├── .env.example         # Environment variables template
└── README.md           # This file
```

## API Endpoints

- **GET** `/health` - Health check endpoint (returns service status)
- **GET** `/` - Root endpoint with API documentation
- **GET** `/items` - Get all items from database
- **GET** `/items/{item_id}` - Get a specific item by ID
- **POST** `/items` - Create a new item in database
- **PUT** `/items/{item_id}` - Update an existing item
- **DELETE** `/items/{item_id}` - Delete an item from database

## Interactive API Documentation

FastAPI provides automatic interactive API documentation:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Example Usage

### Health Check (GET)
```bash
curl "http://localhost:8000/health"
```

Response:
```json
{
  "status": "healthy",
  "service": "FastAPI REST Server with PostgreSQL",
  "version": "1.0.0"
}
```

### Create an item (POST)
```bash
curl -X POST "http://localhost:8000/items" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Laptop",
    "description": "Gaming laptop",
    "price": 1299.99,
    "quantity": 5
  }'
```

Response:
```json
{
  "id": 1,
  "name": "Laptop",
  "description": "Gaming laptop",
  "price": 1299.99,
  "quantity": 5
}
```

### Get all items (GET)
```bash
curl "http://localhost:8000/items"
```

### Get specific item (GET)
```bash
curl "http://localhost:8000/items/1"
```

### Update an item (PUT)
```bash
curl -X PUT "http://localhost:8000/items/1" \
  -H "Content-Type: application/json" \
  -d '{
    "price": 1199.99,
    "quantity": 10
  }'
```

### Delete an item (DELETE)
```bash
curl -X DELETE "http://localhost:8000/items/1"
```

Response:
```json
{
  "message": "Item deleted successfully",
  "deleted_item_id": 1
}
```

## Database Schema

### Items Table

| Column      | Type    | Constraints          |
|-------------|---------|----------------------|
| id          | Integer | Primary Key, Auto    |
| name        | String  | Not Null             |
| description | String  | Nullable             |
| price       | Float   | Not Null             |
| quantity    | Integer | Not Null             |

## Environment Variables

| Variable      | Description                    | Default                                          |
|---------------|--------------------------------|--------------------------------------------------|
| DATABASE_URL  | PostgreSQL connection string   | postgresql://postgres:postgres@localhost:5432/fastapi_db |

## Development

### Stop PostgreSQL Database
```bash
docker-compose down
```

### Stop and Remove Data
```bash
docker-compose down -v
```

### View Database Logs
```bash
docker-compose logs -f postgres
```

## Troubleshooting

**Database connection error:**
- Ensure PostgreSQL is running: `docker-compose ps`
- Check database URL in `.env` file
- Verify PostgreSQL is accessible on port 5432

**Import errors:**
- Make sure virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`


