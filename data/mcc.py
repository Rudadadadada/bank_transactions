from data.imports import *
from data.db_session import Base


class Mcc(Base, SerializerMixin):
    __tablename__ = 'mccs'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, index=True)
    mcc_type = sa.Column(sa.Text, nullable=False)
    mcc_code = sa.Column(sa.Integer, nullable=False)

    merchants = orm.relation('Merchant', back_populates='mcc')
