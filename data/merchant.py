from data.imports import *
from data.db_session import Base


# Merchant model.
class Merchant(Base, SerializerMixin):
    __tablename__ = 'merchants'

    # Columns of table 'merchants'.
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, index=True)
    name = sa.Column(sa.Text, nullable=False)
    country = sa.Column(sa.Text, nullable=False)
    city = sa.Column(sa.Text, nullable=False)
    address = sa.Column(sa.Text, nullable=False)
    # One mcc to single merchant.
    mcc_id = sa.Column(sa.Integer, sa.ForeignKey('mccs.id'), nullable=False)

    mcc = orm.relation('Mcc')
    # Relation between Merchant and Transaction. Many transactions to one merchant.
    transactions = orm.relation('Transaction', back_populates='merchant')
