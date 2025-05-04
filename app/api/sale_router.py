from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.sale_schema import Sale, SaleCreate
from app.crud import sale_crud
from app.database.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Sale)
def create(sale: SaleCreate, db: Session = Depends(get_db)):
    return sale_crud.create_sale(db, sale)

@router.get("/", response_model=list[Sale])
def read_all(db: Session = Depends(get_db)):
    return sale_crud.get_sales(db)
