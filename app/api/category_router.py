from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.category_schema import Category, CategoryCreate
from app.crud import category_crud
from app.database.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Category)
def create(category: CategoryCreate, db: Session = Depends(get_db)):
    return category_crud.create_category(db, category)

@router.get("/", response_model=list[Category])
def read_all(db: Session = Depends(get_db)):
    return category_crud.get_categories(db)
