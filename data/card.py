from data.imports import *
from data.db_session import Base


class Card(Base, SerializerMixin):
    __tablename__ = 'cards'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, index=True)
    card_number = sa.Column(sa.Text, nullable=False)
    account_id = sa.Column(sa.Integer, sa.ForeignKey('accounts.id'), nullable=False)

    account = orm.relation('Account')
    transactions = orm.relation('Transaction', back_populates='card')

    @staticmethod
    def get_card(session, client_id=None, account_id=None):
        cards = []
        if client_id:
            account_select_condition = f' and account_id = {account_id}' if account_id else ''
            cards = list(
                session.execute(f'select cards.id, card_number from "cards" join "accounts" on cards.account_id '
                                f'= accounts.id where accounts.client_id = {client_id}' + account_select_condition))
        else:
            cards = list(session.execute(f'select cards.id, card_number from "cards" where account_id = {account_id})'))
        return cards
