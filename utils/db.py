from flask_sqlalchemy import SQLAlchemy


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):

    def __init__(self):
        self._alchemy = SQLAlchemy()
    
    def get_instance(self):
        return self._alchemy
