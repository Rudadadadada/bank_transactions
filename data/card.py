from data.imports import *
from data.db_session import Base


class Card(Base, SerializerMixin):
    __tablename__ = 'cards'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, index=True)
    number = sa.Column(sa.Text, nullable=False)
    account_id = sa.Column(sa.Integer, sa.ForeignKey('accounts.id'), nullable=False)

    account = orm.relation('Account')
    transactions = orm.relation('Transaction', back_populates='card')

    def get_transactions_as_str(self):
        transactions_str = ''
        for transaction in self.transactions:
            transactions_str += str(transaction) + '\n'

        return transactions_str
