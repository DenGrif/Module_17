from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from app.models import *
from app.models.category import Category



class Product(Base):
    __tablename__ ="products"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String, unique=True, index=True)
    description = Column(String)
    price = Column(Integer)
    image_url = Column(String)
    stock = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))
    rating = Column(Float)
    is_active = Column(Boolean, default=True)

    category = relationship('Category', back_populates='products')



#     parent_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
#
#     products = relationship("Product", back_populates="category")
#
from sqlalchemy.schema import CreateTable
print(CreateTable(Category.__table__))