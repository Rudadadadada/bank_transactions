from data.imports import *
from data.db_session import Base


class Mcc(Base, SerializerMixin):
    __tablename__ = 'mccs'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, index=True)
    type = sa.Column(sa.Text, nullable=False)
    code = sa.Column(sa.Integer, nullable=False)

    merchants = orm.relation('Merchant', back_populates='mcc')
