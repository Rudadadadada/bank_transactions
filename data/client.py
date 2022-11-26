from data.imports import *
from data.db_session import Base


class Client(Base, SerializerMixin):
    __tablename__ = 'clients'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, index=True)
    surname = sa.Column(sa.String, nullable=False)
    name = sa.Column(sa.String, nullable=False)

    accounts = orm.relation('Account', back_populates='client')