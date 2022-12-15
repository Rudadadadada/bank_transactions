from data.imports import *
from data.db_session import Base


class Account(Base, SerializerMixin):
    __tablename__ = 'accounts'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, index=True)
    name = sa.Column(sa.Text, nullable=False)
    client_id = sa.Column(sa.Integer, sa.ForeignKey('clients.id'), nullable=False)

    client = orm.relation('Client')
    cards = orm.relation('Card', back_populates='account')