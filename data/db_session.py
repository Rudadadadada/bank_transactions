import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.engine import URL, Engine
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec

Base = dec.declarative_base()

__factory = None


def global_init(db_params: dict):
    global __factory

    if __factory:
        return

    if not db_params:
        raise Exception("Database params should be specified.")

    engine: Engine = sa.create_engine(URL(**db_params), echo=False)
    __factory = orm.sessionmaker(bind=engine)

    from . import __all_models

    Base.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()
