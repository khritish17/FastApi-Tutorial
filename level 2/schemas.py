from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(..., examples=["Gamming Laptop"])
    price: float = Field(..., gt=0)
    tax: float | None = None