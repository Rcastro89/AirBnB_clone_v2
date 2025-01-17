#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """ method getter cities """
            from models import storage
            ciudades = storage.all(City)
            lista_retorno = []
            for k, v in ciudades.items():
                if self.id == v.state_id:
                    lista_retorno.append(v)
            return lista_retorno
