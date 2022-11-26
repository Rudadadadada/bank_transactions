from data.imports import *
from data.db_session import Base


class Merchant(Base, SerializerMixin):
    __tablename__ = 'merchants'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, index=True)
    # merchant_name = None
    # mcc = None
    # merchant_country = None
    # merchant_city = None
    # merchant_address = None

    transactions = orm.relation('Transaction', back_populates='merchant')