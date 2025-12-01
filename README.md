# project-16 - FastAPI REST Server

A REST API server built with Python and FastAPI supporting all CRUD operations (GET, POST, PUT, DELETE).

## Installation

```bash
pip install -r requirements.txt
```

## Running the Server

```bash
python main.py
```

Or use uvicorn directly:

```bash
uvicorn main:app --reload
```

The server will start at `http://localhost:8000`

## API Endpoints

- **GET** `/` - Root endpoint with API documentation
- **GET** `/items` - Get all items
- **GET** `/items/{item_id}` - Get a specific item by ID
- **POST** `/items` - Create a new item
- **PUT** `/items/{item_id}` - Update an existing item
- **DELETE** `/items/{item_id}` - Delete an item

## Interactive API Documentation

FastAPI provides automatic interactive API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Example Usage

### Create an item (POST)
```bash
curl -X POST "http://localhost:8000/items" \
  -H "Content-Type: application/json" \
  -d '{"name": "Laptop", "description": "Gaming laptop", "price": 1299.99, "quantity": 5}'
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
  -d '{"price": 1199.99, "quantity": 10}'
```

### Delete an item (DELETE)
```bash
curl -X DELETE "http://localhost:8000/items/1"
```
