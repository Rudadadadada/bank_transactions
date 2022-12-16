from data.imports import *
from data.db_session import Base


# Mcc model.
class Mcc(Base, SerializerMixin):
    __tablename__ = 'mccs'

    # Columns of table 'mccs'.
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, index=True)
    type = sa.Column(sa.Text, nullable=False)
    code = sa.Column(sa.Integer, nullable=False)

    # Relation between Mcc and Merchant. Many merchants to one mcc.
    merchants = orm.relation('Merchant', back_populates='mcc')
