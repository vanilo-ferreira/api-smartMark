from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    category_id: int
    brand: str

class Product(ProductCreate):
    id: int

    class Config:
        orm_mode = True
        
class ProductUpdate(BaseModel):
    price: Optional[float] = None
