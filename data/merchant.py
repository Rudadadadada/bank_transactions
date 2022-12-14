from data.imports import *
from data.db_session import Base


class Merchant(Base, SerializerMixin):
    __tablename__ = 'merchants'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, index=True)
    merchant_name = sa.Column(sa.Text, nullable=False)
    merchant_country = sa.Column(sa.Text, nullable=False)
    merchant_city = sa.Column(sa.Text, nullable=False)
    merchant_address = sa.Column(sa.Text, nullable=False)
    mcc_id = sa.Column(sa.Integer, sa.ForeignKey('mccs.id'), nullable=False)

    mcc = orm.relation('Mcc')
    transactions = orm.relation('Transaction', back_populates='merchant')
