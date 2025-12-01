from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import uvicorn

from database import engine, get_db, Base
from models import Item
from schemas import ItemCreate, ItemUpdate, ItemResponse

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="REST API with FastAPI and PostgreSQL", version="1.0.0")


# Healthcheck endpoint
@app.get("/health")
async def healthcheck():
    """Health check endpoint to verify the service is running"""
    return {
        "status": "healthy",
<<<<<<< HEAD
        "service": "FastAPI REST Server with PostgreSQL",
=======
        "service": "FastAPI REST Server",
>>>>>>> health
        "version": "1.0.0"
    }


# GET - Retrieve all items
<<<<<<< HEAD
@app.get("/items", response_model=List[ItemResponse])
async def get_items(db: Session = Depends(get_db)):
    """Get all items from database"""
    items = db.query(Item).all()
    return items


# GET - Retrieve a specific item by ID
@app.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int, db: Session = Depends(get_db)):
    """Get a specific item by ID"""
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


# POST - Create a new item
@app.post("/items", response_model=ItemResponse, status_code=201)
async def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    """Create a new item in database"""
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# PUT - Update an existing item
@app.put("/items/{item_id}", response_model=ItemResponse)
async def update_item(
    item_id: int,
    item_update: ItemUpdate,
    db: Session = Depends(get_db)
):
    """Update an existing item"""
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # Update only provided fields
    update_data = item_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_item, field, value)
    
    db.commit()
    db.refresh(db_item)
    return db_item
=======
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
>>>>>>> health


# DELETE - Delete an item
@app.delete("/items/{item_id}")
<<<<<<< HEAD
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    """Delete an item by ID"""
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted successfully", "deleted_item_id": item_id}
=======
async def delete_item(item_id: int):
    """Delete an item by ID"""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    deleted_item = items_db.pop(item_id)
    return {"message": "Item deleted successfully", "deleted_item": deleted_item}
>>>>>>> health


# Root endpoint
@app.get("/")
async def root():
    """Root endpoint"""
    return {
<<<<<<< HEAD
        "message": "Welcome to FastAPI REST Server with PostgreSQL",
=======
        "message": "Welcome to FastAPI REST Server",
>>>>>>> health
        "endpoints": {
            "GET /health": "Health check endpoint",
            "GET /items": "Get all items",
            "GET /items/{item_id}": "Get item by ID",
            "POST /items": "Create new item",
            "PUT /items/{item_id}": "Update item",
            "DELETE /items/{item_id}": "Delete item"
        }
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
