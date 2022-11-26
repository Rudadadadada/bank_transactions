from data.imports import *
from data.db_session import Base


class Transaction(Base, SerializerMixin):
    __tablename__ = 'transactions'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, index=True)
    amount = sa.Column(sa.Integer, nullable=False)
    # currency = None
    datetime = sa.Column(sa.DateTime, nullable=False)

    card = orm.relation('Card')
    merchant = orm.relation('Merchant')


