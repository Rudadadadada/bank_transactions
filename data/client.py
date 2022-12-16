from data.imports import *
from data.db_session import Base


# Client model.
class Client(Base, SerializerMixin):
    __tablename__ = 'clients'

    # Columns of table 'clients'.
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, index=True)
    surname = sa.Column(sa.Text, nullable=False)
    name = sa.Column(sa.Text, nullable=False)

    # Relation between Client and Account. Many accounts to one client.
    accounts = orm.relation('Account', back_populates='client')

    # Get all accounts of client as dict.
    def get_accounts_as_dict(self):
        accounts_dict = {}
        for account in self.accounts:
            accounts_dict[account.name] = {'callback_data': f'account_{account.id}'}

        return accounts_dict
