from data.imports import *
from data.db_session import Base


# Card model.
class Card(Base, SerializerMixin):
    __tablename__ = 'cards'

    # Columns of table 'cards'.
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, index=True)
    number = sa.Column(sa.Text, nullable=False)
    # One account to single card.
    account_id = sa.Column(sa.Integer, sa.ForeignKey('accounts.id'), nullable=False)

    account = orm.relation('Account')
    # Relation between Card and Transaction. Many transactions to one card.
    transactions = orm.relation('Transaction', back_populates='card')
