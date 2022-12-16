from data.imports import *
from data.db_session import Base


# Account model.
class Account(Base, SerializerMixin):
    __tablename__ = 'accounts'

    # Columns of table 'accounts'.
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, index=True)
    name = sa.Column(sa.Text, nullable=False)
    # One client to single account.
    client_id = sa.Column(sa.Integer, sa.ForeignKey('clients.id'), nullable=False)

    client = orm.relation('Client')
    # Relation between Account and Card. Many cards to one account.
    cards = orm.relation('Card', back_populates='account')

    def get_cards_as_dict(self):
        cards_dict = {}
        for card in self.cards:
            cards_dict[card.number] = {'callback_data': f'card_{card.id}'}

        return cards_dict

    def get_transactions_as_str(self):
        transactions_str = ''
        for card in self.cards:
            transactions_str += card.get_transactions_as_str()

        return transactions_str
