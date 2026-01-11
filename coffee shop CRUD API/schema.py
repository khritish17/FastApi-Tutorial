from pydantic import BaseModel

class OrderCreate(BaseModel):
    customer_name : str
    coffee_type: str
    sugar: bool 
    milk: bool
    ice: bool
    cream: bool

class Order(OrderCreate):
    id: int
    status: str = "Pending"