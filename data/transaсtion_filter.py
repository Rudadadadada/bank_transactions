from data.__all_models import *
from datetime import date, timedelta


def get_transactions(session, client_id: int, account_id: int = None, card_id: int = None, month: int = None,
                     mcc_type: str = None, city: str = None, merchant_name: str = None):
    transactions = session.query(transaction.Transaction). \
        outerjoin(card.Card, transaction.Transaction.card_id == card.Card.id). \
        outerjoin(account.Account, transaction.Transaction.card_id == account.Account.id). \
        outerjoin(client.Client, account.Account.client_id == client.Client.id). \
        outerjoin(merchant.Merchant, transaction.Transaction.merchant_id == merchant.Merchant.id). \
        outerjoin(mcc.Mcc, merchant.Merchant.mcc_id == mcc.Mcc.id).filter(client.Client.id == client_id)
    transactions = transactions.filter(account.Account.id == account_id) if account_id else transactions
    transactions = transactions.filter(card.Card.id == card_id) if card_id else transactions
    transactions = transactions.filter(date(2022, month, 1) <= transaction.Transaction.datetime,
                                       transaction.Transaction.datetime <= timedelta(days=1)) if month else transactions
    transactions = transactions.filter(mcc.Mcc.mcc_type == mcc_type) if mcc_type else transactions
    transactions = transactions.filter(merchant.Merchant.merchant_city == city) if city else transactions
    transactions = transactions.filter(
        merchant.Merchant.merchant_name == merchant_name) if merchant_name else transactions
    return list(transactions)
