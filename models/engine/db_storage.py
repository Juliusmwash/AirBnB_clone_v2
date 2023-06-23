#!/usr/bin/python3
"""
mysql database storage engine
"""
from os import getenv
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import reflection
from sqlalchemy.exc import OperationalError


class DBStorage:
    """
    Storage engine
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        instanciates the storage class
        """

        db_url = "mysql+mysqldb://{}:{}@{}/{}".format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB"))
        self.__engine = create_engine(db_url, pool_pre_ping=True)
        self.create_database()

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the curret database session all
          objects of the given class.
        If cls is None, queries all types of objects.

        Return:
            Dict of queried classes in the format <class name>.<obj id> = obj.
        """
        objs = None

        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            #objs.extend(self.__session.query(User).all())
            #objs.extend(self.__session.query(Place).all())
            #objs.extend(self.__session.query(Review).all())
            #objs.extend(self.__session.query(Amenity).all())
        else:
            try:
                cls = globals()[cls]
                objs = self.__session.query(cls).all()
            except Exception as e:
                objs = []

        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def setup_database(self):
        """Create the engine"""
        db_url = "mysql+mysqldb://{}:{}@{}/{}".format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB"))
        self.__engine = create_engine(db_url, pool_pre_ping=True)

        try:
            # Execute a sample query to test the connection
            with self.__engine.connect() as connection:
                result = connection.execute("SELECT 1")

        except OperationalError as e:
            # Catch and handle the SQLAlchemy OperationalError
            if e.orig.args and e.orig.args[0] == 1049:
                # Recreate the database dynamically
                self.create_database()

                # Reattempt to connect to the newly created database
                self.__engine.dispose()
                self.__engine = create_engine(db_url, pool_pre_ping=True)
            else:
                print("Error:", e)

    def create_database(self):
        inspector = reflection.Inspector.from_engine(self.__engine)
        if getenv('HBNB_ENV') == "dev":
            database_exists = inspector.has_database('hbnb_dev_db')
            if not database_exists:
                with open('setup_mysql_dev.sql', 'r') as script_file:
                    sql_script = script_file.read()
                    print("sql_script :\n{}".format(sql_script))
                    self.__engine.execute(sql_script)
                self.__engine.dispose()
                self.__engine = create_engine(db_url, pool_pre_ping=True)
            else:
                print("database hbnb_dev_db exists")
        else:
            database_exists = inspector.has_database('hbnb_test_db')
            if not database_exists:
                with open('setup_mysql_test.sql', 'r') as script_file:
                    sql_script = script_file.read()
                    print("sql_script :\n{}".format(sql_script))
                    self.__engine.execute(sql_script)
                self.__engine.dispose()
                self.__engine = create_engine(db_url, pool_pre_ping=True)
            else:
                print("database hbnb_test_db exists")

    def new(self, obj):
        """Add obj to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        make_session = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(make_session)
        self.__session = Session()

    def close(self):
        """Close the SQLAlchemy session."""
        self.__session.close()
