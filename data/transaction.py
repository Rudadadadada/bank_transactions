from data.imports import *
from data.db_session import Base


class Transaction(Base, SerializerMixin):
    __tablename__ = 'transactions'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, index=True)
    amount = sa.Column(sa.Integer, nullable=False)
    datetime = sa.Column(sa.DateTime, nullable=False)
    card_id = sa.Column(sa.Integer, sa.ForeignKey('cards.id'), nullable=False)
    merchant_id = sa.Column(sa.Integer, sa.ForeignKey('merchants.id'), nullable=False)

    card = orm.relation('Card')
    merchant = orm.relation('Merchant')

    def __str__(self):
        return f'{self.datetime} {self.card.card_number} {self.amount}₽   {self.merchant.merchant_name}'
