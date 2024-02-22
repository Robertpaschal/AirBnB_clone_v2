import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """A class representing the database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database engine"""
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST", default="localhost")
        db = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def all(self, cls=None):
        """Query all objects from the current database session"""
        objects = {}
        classes = [User, State, City, Amenity, Place, Review]

        if cls:
            classes = [cls]

        for cls in classes:
            query = self.__session.query(cls)
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj

        return objects

    def new(self, obj):
        """Add the objects to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create the session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)
