from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

#@app.get("/items/{item_id}")
#def read_item(item_id: int):
#    return {"item_id": item_id}

class Item(BaseModel):
    id: int
    name: str
    description: str
    price: float
    is_available: bool
    discount: Optional[float] = None

items = [
    {"id": 1, "name": "Item 1", "description": "Desc 1", "price": 10.5, "is_available": True},
]

#@app.get("/items/{item_id}")
#def read_item(item_id: int):
#    for item in items:
#        if item["id"] == item_id:
#            return item
#        return "404 Item not found"


@app.get("/items/{item_id}")
def read_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
