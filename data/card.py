from data.imports import *
from data.db_session import Base


class Card(Base, SerializerMixin):
    __tablename__ = 'cards'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, index=True)
    card_number = sa.Column(sa.Text, nullable=False)
    account_id = sa.Column(sa.Integer, sa.ForeignKey('accounts.id'), nullable=False)

    account = orm.relation('Account')
    transactions = orm.relation('Transaction', back_populates='card')
