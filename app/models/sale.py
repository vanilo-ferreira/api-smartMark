from sqlalchemy import Column, Integer, Float, ForeignKey, Date
from app.database.session import Base
import datetime

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    total_price = Column(Float)
    date = Column(Date, default=datetime.date.today)
