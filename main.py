from datetime import time
from fastapi  import FastAPI
from pydantic import BaseModel
from typing   import Optional

# Item Model
class Item(BaseModel):
  name: str
  price: float
  is_offer: Optional[bool] = None
  created_in: Optional[time] = None

# Core Application Instance
app = FastAPI()

# API Routes
@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
  return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
