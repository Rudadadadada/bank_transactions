from data.imports import *
from data.db_session import Base


class Client(Base, SerializerMixin):
    __tablename__ = 'clients'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, index=True)
    surname = sa.Column(sa.Text, nullable=False)
    name = sa.Column(sa.Text, nullable=False)

    accounts = orm.relation('Account', back_populates='client')

    def get_accounts_as_dict(self):
        accounts_dict = {}
        for account in self.accounts:
            accounts_dict[account.name] = {'callback_data': f'account_{account.id}'}

        return accounts_dict

    def get_transactions_as_str(self):
        transactions_str = ''
        for account in self.accounts:
            transactions_str += account.get_transactions_as_str()

        return transactions_str
