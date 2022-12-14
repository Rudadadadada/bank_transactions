import datetime
from data.__all_models import *


def get_transactions(session, client_id, account_id=None, card_info=None, month=None, mcc_type=None):
    temp_cards = list(card.Card.get_card(session, client_id, account_id=account_id)) if not card_info else [card_info]
    transactions = []
    for card_id, card_number in temp_cards:
        transactions += list((session.execute(f'select amount, datetime, merchant_id '
                                              f'from "transactions" where card_id = {card_id}')))

    if mcc_type:
        mcc_id = list(session.execute(f'select id from "mccs" where mcc_type = {mcc_type}'))[0][0]
        stores = list(map(lambda x: x[0], session.execute(f'select id from "merchants" where mcc_id = {mcc_id}')))
        transactions = list(filter(lambda x: x[2] in stores, transactions))

    if month:
        month_dict = {'January': [1, 31], 'February': [2, 28], 'March': [3, 31], 'April': [4, 30],
                      'May': [5, 31], 'June': [6, 30], 'July': [7, 31], 'August': [8, 31],
                      'September': [9, 30], 'October': [10, 31], 'November': [11, 30], 'December': [12, 31]}
        month_n, days = month_dict[month]
        start = datetime.datetime(2022, month_n, 1)
        end = datetime.datetime(2022, month_n, days)
        transactions = list(filter(lambda x: start <= x[1] <= end, transactions))
    return transactions
