from sqlalchemy.orm import Session
from app.models.sale import Sale
from app.schemas.sale_schema import SaleCreate

def create_sale(db: Session, sale: SaleCreate):
    db_sale = Sale(**sale.dict())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale

def get_sales(db: Session):
    return db.query(Sale).all()

def get_sale(db: Session, sale_id: int):
    return db.query(Sale).filter(Sale.id == sale_id).first()

def delete_sale(db: Session, sale_id: int):
    db_sale = get_sale(db, sale_id)
    if db_sale:
        db.delete(db_sale)
        db.commit()
