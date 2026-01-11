from fastapi import FastAPI, HTTPException, status
from schema import Order, OrderCreate


app = FastAPI()

orders_db = {}
id_counter = 1

@app.post("/order", response_model=Order)
def place_order(order_data: OrderCreate):
    global id_counter

    new_order = Order(
        id = id_counter,
        **order_data.model_dump()
    )

    orders_db[id_counter] = new_order
    id_counter += 1
    return new_order
@app.get("/all_orders")
def get_all_orders():
    return list(orders_db.values())

@app.delete("/cancel/{order_id}")
def cancel_order(order_id: int):
    if order_id not in orders_db:
        raise HTTPException(status_code=404, detail="Order ID not found")
    
    del orders_db[order_id]
    return {"message": f"Order {order_id} has been cancelled successfully"}



