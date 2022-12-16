from data.__all_models import *
from datetime import date, timedelta


# Function returns list of Transactions class objects according to filtering.
def get_transactions(session, client_id: int, account_id: int = None, card_id: int = None, month: int = None,
                     mcc_type: str = None, city: str = None, merchant_name: str = None):
    # First filter makes select by using query which returns objects of class Transaction according to client_id.
    transactions = session.query(transaction.Transaction). \
        outerjoin(card.Card, transaction.Transaction.card_id == card.Card.id). \
        outerjoin(account.Account, transaction.Transaction.card_id == account.Account.id). \
        outerjoin(client.Client, account.Account.client_id == client.Client.id). \
        outerjoin(merchant.Merchant, transaction.Transaction.merchant_id == merchant.Merchant.id). \
        outerjoin(mcc.Mcc, merchant.Merchant.mcc_id == mcc.Mcc.id).filter(client.Client.id == client_id)
    # Second filter makes filtering according to account_id if account_id is not None.
    transactions = transactions.filter(account.Account.id == account_id) if account_id else transactions
    # Third filter makes filtering according to card_id if card_id is not None.
    transactions = transactions.filter(card.Card.id == card_id) if card_id else transactions
    # Fourth filter returns filtered transactions for any month if month is not None.
    transactions = transactions.filter(date(2022, month, 1) <= transaction.Transaction.datetime,
                                       transaction.Transaction.datetime <= timedelta(days=1)) if month else transactions
    # Fifth filter returns filtered transactions for any categories if mcc_type is not None.
    transactions = transactions.filter(mcc.Mcc.type == mcc_type) if mcc_type else transactions
    # Sixth filter returns filtered transactions for any city if city is not None.
    transactions = transactions.filter(merchant.Merchant.city == city) if city else transactions
    # Seventh filter returns filtered transactions for any store name if merchant_name is not None.
    transactions = transactions.filter(
        merchant.Merchant.name == merchant_name) if merchant_name else transactions
    return list(transactions)
