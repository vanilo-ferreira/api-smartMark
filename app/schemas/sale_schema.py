from pydantic import BaseModel
from datetime import date

class SaleCreate(BaseModel):
    product_id: int
    quantity: int
    total_price: float
    date: date

class Sale(BaseModel):
    id: int
    product_id: int
    quantity: int
    total_price: float
    date: date

    class Config:
        orm_mode = True