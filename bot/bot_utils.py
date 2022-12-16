import json

from data.client import Client
from data.transaсtion_filter import get_transactions

# Constants
MONTHS = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}


# Get all clients as dict.
def get_clients_as_dict(session):
    clients = session.query(Client).all()

    clients_dict = {}
    for client in clients:
        clients_dict[client.name] = {'callback_data': f'client_{client.id}'}

    return clients_dict


# Get messages that were sent earlier.
def get_sent_messages(chat_id):
    with open('bot/sent_messages.json', 'r') as f:
        sent_messages = json.load(f)
    if chat_id != -1 and str(chat_id) not in sent_messages:
        return []
    elif str(chat_id) in sent_messages:
        clear_chat_messages(chat_id)
        return sent_messages[str(chat_id)]
    return sent_messages


# Clear all previous messages in the chat.
def clear_chat_messages(chat_id):
    sent_messages = get_sent_messages(-1)
    if str(chat_id) in sent_messages:
        sent_messages[str(chat_id)] = []
    with open('bot/sent_messages.json', 'w') as f:
        json.dump(sent_messages, f)


# Add new message to the list of sent messages.
def add_sent_message(chat_id, message_id):
    sent_messages = get_sent_messages(-1)
    if str(chat_id) not in sent_messages:
        sent_messages[str(chat_id)] = []
    if message_id not in sent_messages[str(chat_id)]:
        sent_messages[str(chat_id)].append(message_id)
    with open('bot/sent_messages.json', 'w') as f:
        json.dump(sent_messages, f)


# Get all months from transactions.
def get_possible_months(session, object_type, object_id):
    if object_type == 'client':
        transactions = get_transactions(session, object_id)
    elif object_type == 'account':
        transactions = get_transactions(session, account_id=object_id)
    else:
        transactions = get_transactions(session, card_id=object_id)
    possible_months = []
    for transaction in transactions:
        if transaction.datetime.month not in possible_months:
            possible_months.append(transaction.datetime.month)

    return sorted(possible_months)


# Get all cities from transactions.
def get_possible_cities(session, object_type, object_id):
    if object_type == 'client':
        transactions = get_transactions(session, object_id)
    elif object_type == 'account':
        transactions = get_transactions(session, account_id=object_id)
    else:
        transactions = get_transactions(session, card_id=object_id)
    possible_cities = []
    for transaction in transactions:
        if transaction.merchant.city not in possible_cities:
            possible_cities.append(transaction.merchant.city)

    return sorted(possible_cities)


# Get all categories from transactions.
def get_possible_categories(session, object_type, object_id):
    if object_type == 'client':
        transactions = get_transactions(session, object_id)
    elif object_type == 'account':
        transactions = get_transactions(session, account_id=object_id)
    else:
        transactions = get_transactions(session, card_id=object_id)
    possible_categories = []
    for transaction in transactions:
        if transaction.merchant.mcc.type not in possible_categories:
            possible_categories.append(transaction.merchant.mcc.type)

    return sorted(possible_categories)


# Get all merchants from transactions.
def get_possible_merchants(session, object_type, object_id):
    if object_type == 'client':
        transactions = get_transactions(session, object_id)
    elif object_type == 'account':
        transactions = get_transactions(session, account_id=object_id)
    else:
        transactions = get_transactions(session, card_id=object_id)
    possible_merchants = []
    for transaction in transactions:
        if transaction.merchant.name not in possible_merchants:
            possible_merchants.append(transaction.merchant.name)

    return sorted(possible_merchants)


# Get transactions filtered by some parameters.
def get_transactions_by_filter(session, object_type, object_id, filter_type, filter_value):
    if object_type == 'client':
        transactions = get_transactions(session, client_id=object_id)
    elif object_type == 'account':
        transactions = get_transactions(session, account_id=object_id)
    else:
        transactions = get_transactions(session, card_id=object_id)

    if filter_type == 'month':
        transactions = [transaction for transaction in transactions if transaction.datetime.month == int(filter_value)]
    elif filter_type == 'category':
        transactions = [transaction for transaction in transactions if transaction.merchant.mcc.type == filter_value]
    elif filter_type == 'city':
        transactions = [transaction for transaction in transactions if transaction.merchant.city == filter_value]
    elif filter_type == 'merchant':
        transactions = [transaction for transaction in transactions if transaction.merchant.name == filter_value]

    return transactions
