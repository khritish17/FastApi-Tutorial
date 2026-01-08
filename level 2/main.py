from fastapi import FastAPI
from schemas import Item

app = FastAPI()

@app.post("/create")
def create(item: Item):
    total_price = item.price + (item.tax or 0)
    return {"item_name": item.name, "total": total_price}