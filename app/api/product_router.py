from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.product_schema import Product, ProductCreate, ProductUpdate
from app.crud import product_crud
from app.database.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Product)
def create(product: ProductCreate, db: Session = Depends(get_db)):
    return product_crud.create_product(db, product)

@router.get("/", response_model=list[Product])
def read_all(db: Session = Depends(get_db)):
    return product_crud.get_products(db)

@router.patch("/{product_id}", response_model=Product)
def partial_update(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    return product_crud.partial_update_product(db, product_id, product)