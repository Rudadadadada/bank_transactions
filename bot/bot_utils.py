import json

from data.client import Client

COLUMNS_STR = 'Date/time                    Card number             Amount Merchant\n'


def get_clients_as_dict(session):
    clients = session.query(Client).all()

    clients_dict = {}
    for client in clients:
        clients_dict[client.name] = {'callback_data': f'client_{client.id}'}

    return clients_dict


def get_sent_messages(chat_id):
    with open('bot/sent_messages.json', 'r') as f:
        sent_messages = json.load(f)
    if chat_id != -1 and str(chat_id) not in sent_messages:
        return []
    elif str(chat_id) in sent_messages:
        clear_chat_messages(chat_id)
        return sent_messages[str(chat_id)]
    return sent_messages


def clear_chat_messages(chat_id):
    sent_messages = get_sent_messages(-1)
    if str(chat_id) in sent_messages:
        sent_messages[str(chat_id)] = []
    with open('bot/sent_messages.json', 'w') as f:
        json.dump(sent_messages, f)


def add_sent_message(chat_id, message_id):
    sent_messages = get_sent_messages(-1)
    if str(chat_id) not in sent_messages:
        sent_messages[str(chat_id)] = []
    if message_id not in sent_messages[str(chat_id)]:
        sent_messages[str(chat_id)].append(message_id)
    with open('bot/sent_messages.json', 'w') as f:
        json.dump(sent_messages, f)
