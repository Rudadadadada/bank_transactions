from data.__all_models import *
from datetime import datetime


def get_transactions(session, client_id, account_id=None, card_id=None, month=None,
                     mcc_type=None, city=None, merchant_name=None):
    transactions = session.query(transaction.Transaction). \
        outerjoin(card.Card, transaction.Transaction.card_id == card.Card.id). \
        outerjoin(account.Account, transaction.Transaction.card_id == account.Account.id). \
        outerjoin(client.Client, account.Account.client_id == client.Client.id). \
        outerjoin(merchant.Merchant, transaction.Transaction.merchant_id == merchant.Merchant.id). \
        outerjoin(mcc.Mcc, merchant.Merchant.mcc_id == mcc.Mcc.id).filter(client.Client.id == client_id)
    transactions = transactions.filter(account.Account.id == account_id) if account_id else transactions
    transactions = transactions.filter(card.Card.id == card_id) if card_id else transactions
    # transactions = transactions.filter()
    transactions = transactions.filter(mcc.Mcc.mcc_type == mcc_type) if mcc_type else transactions
    transactions = transactions.filter(merchant.Merchant.merchant_city == city) if city else transactions
    transactions = transactions.filter(
        merchant.Merchant.merchant_name == merchant_name) if merchant_name else transactions
    # if month:
    #     date = transaction.Transaction.datetime
    #     transactions = transactions.filter(datetime(2022, 11, 1) <= date) \
    #         .filter(date <= datetime(2022, 12, 1))
    # return list(transactions)
