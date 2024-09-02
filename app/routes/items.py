from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Item

router = APIRouter()

# In-memory database
items_db = []

@router.post("/items/", response_model=Item)
def create_item(item: Item):
    items_db.append(item)
    return item

@router.get("/items/", response_model=List[Item])
def get_items():
    return items_db

@router.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
