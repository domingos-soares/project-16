from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict
import uvicorn

app = FastAPI(title="REST API with FastAPI", version="1.0.0")

# In-memory database
items_db: Dict[int, dict] = {}
item_id_counter = 1


# Pydantic models for request/response
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int


class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None


# GET - Retrieve all items
@app.get("/items")
async def get_items():
    """Get all items"""
    return {"items": list(items_db.values())}


# GET - Retrieve a specific item by ID
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    """Get a specific item by ID"""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]


# POST - Create a new item
@app.post("/items", status_code=201)
async def create_item(item: Item):
    """Create a new item"""
    global item_id_counter
    
    new_item = {
        "id": item_id_counter,
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "quantity": item.quantity
    }
    
    items_db[item_id_counter] = new_item
    item_id_counter += 1
    
    return new_item


# PUT - Update an existing item
@app.put("/items/{item_id}")
async def update_item(item_id: int, item_update: ItemUpdate):
    """Update an existing item"""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    stored_item = items_db[item_id]
    
    # Update only provided fields
    if item_update.name is not None:
        stored_item["name"] = item_update.name
    if item_update.description is not None:
        stored_item["description"] = item_update.description
    if item_update.price is not None:
        stored_item["price"] = item_update.price
    if item_update.quantity is not None:
        stored_item["quantity"] = item_update.quantity
    
    items_db[item_id] = stored_item
    return stored_item


# DELETE - Delete an item
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    """Delete an item by ID"""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    deleted_item = items_db.pop(item_id)
    return {"message": "Item deleted successfully", "deleted_item": deleted_item}


# Root endpoint
@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to FastAPI REST Server",
        "endpoints": {
            "GET /items": "Get all items",
            "GET /items/{item_id}": "Get item by ID",
            "POST /items": "Create new item",
            "PUT /items/{item_id}": "Update item",
            "DELETE /items/{item_id}": "Delete item"
        }
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
