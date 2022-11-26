from data.imports import *
from data.db_session import Base


class Account(Base, SerializerMixin):
    __tablename__ = 'accounts'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, index=True)

    client = orm.relation('Client')
    cards = orm.relation('Card', back_populates='account')