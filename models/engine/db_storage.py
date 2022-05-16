#!/usr/bin/python3

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import os
from models.base_model import Base
from models.city import City
from models.state import State


class DBStorage:
    """Comentarios"""
    __engine = None
    __session = None

    def __init__(self):
        """constructor de clase"""
        my_host = os.environ.get("HBNB_MYSQL_HOST")
        usuario = os.environ.get("HBNB_MYSQL_USER")
        contrasena = os.environ.get("HBNB_MYSQL_PWD")
        entorno = os.environ.get("HBNB_ENV")
        base = os.environ.get("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                           .format(usuario, contrasena,
                                   my_host, base), pool_pre_ping=True)
        if entorno == 'test':
            Base.metadata.drop_all(self.__engine)
        else:
            Base.metadata.create_all(self.__engine)
            Session = sessionmaker(bind=self.__engine)
            self.__session = Session()

    def all(self, cls=None):
        """all method"""
        result = self.__session.query(cls).all()
        diccionario_retorno = {}
        for row in result:
            diccionario_retorno[row.__class__.__name__ + '.' + row.__dict__['id']] = row
        self.__session.close()
        return diccionario_retorno
    
    def new(self, obj):
        """nuevo objeto"""
        self.__session.add(obj.__class__.__name__(obj.__dict__))
    
    def save(self):
        """guardar cambios"""
        self.__session.commit()
        
    def delete(self, obj=None):
        """delete obj"""
        if obj:
            clase = obj.__class__.__name__
            self.__session = clase.delete().where(clase.id == obj.__dict__['id'])
    
    def reload(self):
        """recargar"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()