from data.imports import *
from data.db_session import Base


class Client(Base, SerializerMixin):
    __tablename__ = 'clients'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, index=True)
    surname = sa.Column(sa.Text, nullable=False)
    name = sa.Column(sa.Text, nullable=False)

    accounts = orm.relation('Account', back_populates='client')

    def __init__(self, _id, _surname, _name):
        self._id = _id
        self._surname = _surname
        self._name = _name

    def get_id(self):
        return self._id

    def get_surname(self):
        return self._surname

    def get_name(self):
        return self._name
