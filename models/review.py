#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review classto store review information
        Inherits from SQLAlchemy Base and links to the MySQL table reviews.
    """
    __tablename__ = "reviews"
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("user.id"), nullable=False, )
        text = Column(String(1024), nullable=False)
