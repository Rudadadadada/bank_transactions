from telebot.async_telebot import AsyncTeleBot
import asyncio
from bot_utils import get_clients_as_dict, get_sent_messages, add_sent_message, COLUMNS_STR
from data.transaсtion_filter import get_transactions
from telebot.util import quick_markup
from data.account import Account
from data.card import Card
from data.client import Client
from config import TOKEN, DATABASE
from data.db_session import create_session, global_init

global_init(DATABASE)
session = create_session()
session.execute(open("data/initial_data.sql", "r").read())
bot = AsyncTeleBot(TOKEN)


@bot.message_handler(commands=['start'])
async def send_welcome(message):
    sent_messages = get_sent_messages(message.chat.id)
    for message_id in sent_messages:
        await bot.delete_message(message.chat.id, message_id)
    bot_message = await bot.send_message(message.chat.id,
                                         """Welcome to the Bank Transactions Bot!\nMade by @Rudadadadada & @rekhlov""",
                                         reply_markup=quick_markup(
                                             {'Get all clients': {'callback_data': 'get_all_clients'}}))
    add_sent_message(message.chat.id, bot_message.message_id)
    add_sent_message(message.chat.id, message.message_id)


@bot.message_handler(content_types=['text', 'document', 'audio', 'photo', 'sticker', 'video', 'video_note', 'voice'])
async def user_messages(message):
    sent_messages = get_sent_messages(message.chat.id)
    for message_id in sent_messages:
        await bot.delete_message(message.chat.id, message_id)
    bot_message = await bot.send_message(message.chat.id, 'Sorry, I don\'t understand you :(')
    await send_welcome(message)
    add_sent_message(message.chat.id, bot_message.message_id)


@bot.callback_query_handler(func=lambda call: call.data == 'start')
async def start(call):
    await bot.edit_message_text("""Welcome to the Bank Transactions Bot!\nMade by @Rudadadadada & @rekhlov""",
                                call.message.chat.id,
                                call.message.message_id,
                                reply_markup=quick_markup({'Get all clients': {'callback_data': 'get_all_clients'}}))


@bot.callback_query_handler(func=lambda call: call.data == 'get_all_clients')
async def get_all_clients(call):
    await bot.answer_callback_query(call.id, 'Getting all clients...')
    await asyncio.sleep(1)
    clients_dict = get_clients_as_dict(session)
    clients_dict['Back'] = {'callback_data': 'start'}
    await bot.edit_message_text('All clients:', call.message.chat.id, call.message.message_id,
                                reply_markup=quick_markup(clients_dict, row_width=1))


@bot.callback_query_handler(
    func=lambda call: call.data.startswith('client_') and not call.data.endswith('_transactions'))
async def get_client(call):
    client_id = int(call.data.split('_')[1])
    client = session.query(Client).filter(Client.id == client_id).first()
    await bot.answer_callback_query(call.id, f'Getting client {client.name} accounts...')
    await asyncio.sleep(1)
    accounts_dict = client.get_accounts_as_dict()
    accounts_dict['View transactions'] = {'callback_data': f'client_{client.id}_transactions'}
    accounts_dict['Back'] = {'callback_data': 'get_all_clients'}
    await bot.edit_message_text(f'Accounts of {client.name}:', call.message.chat.id, call.message.message_id,
                                reply_markup=quick_markup(accounts_dict, row_width=2))


@bot.callback_query_handler(func=lambda call: call.data.startswith('client_') and call.data.endswith('_transactions'))
async def get_client_transactions(call):
    client_id = int(call.data.split('_')[1])
    client = session.query(Client).filter(Client.id == client_id).first()
    await bot.answer_callback_query(call.id, f'Getting client {client.name} transactions...')
    await asyncio.sleep(1)
    transactions = get_transactions(session, client_id)
    transactions_str = COLUMNS_STR + '\n'.join([str(transaction) for transaction in transactions])
    await bot.edit_message_text(transactions_str, call.message.chat.id, call.message.message_id,
                                reply_markup=quick_markup({'Back': {'callback_data': f'client_{client_id}'}}))


@bot.callback_query_handler(
    func=lambda call: call.data.startswith('account_') and not call.data.endswith('_transactions'))
async def get_account(call):
    account_id = int(call.data.split('_')[1])
    account = session.query(Account).filter(Account.id == account_id).first()
    await bot.answer_callback_query(call.id, f'Getting account {account.name} cards...')
    await asyncio.sleep(1)
    cards_dict = account.get_cards_as_dict()
    cards_dict['Back'] = {'callback_data': f'client_{account.client_id}'}
    cards_dict['View transactions'] = {'callback_data': f'account_{account.id}_transactions'}
    await bot.edit_message_text(f'Cards of account {account.name}', call.message.chat.id, call.message.message_id,
                                reply_markup=quick_markup(cards_dict, row_width=2))


@bot.callback_query_handler(func=lambda call: call.data.startswith('account_') and call.data.endswith('_transactions'))
async def get_account_transactions(call):
    account_id = int(call.data.split('_')[1])
    account = session.query(Account).filter(Account.id == account_id).first()
    await bot.answer_callback_query(call.id, f'Getting account {account.name} transactions...')
    await asyncio.sleep(1)
    transactions = get_transactions(session, client_id=account.client_id, account_id=account_id)
    transactions_str = COLUMNS_STR + '\n'.join([str(transaction) for transaction in transactions])
    await bot.edit_message_text(transactions_str, call.message.chat.id, call.message.message_id,
                                reply_markup=quick_markup({'Back': {'callback_data': f'account_{account_id}'}}))


@bot.callback_query_handler(func=lambda call: call.data.startswith('card_') and not call.data.endswith('_transactions'))
async def get_card_transactions(call):
    card_id = int(call.data.split('_')[1])
    card = session.query(Card).filter(Card.id == card_id).first()
    await bot.answer_callback_query(call.id, f'Getting card {card.number} transactions...')
    await asyncio.sleep(1)
    transactions = get_transactions(session, client_id=card.account.client_id, card_id=card_id)
    transactions_str = COLUMNS_STR + '\n'.join([str(transaction) for transaction in transactions])
    await bot.edit_message_text(transactions_str, call.message.chat.id, call.message.message_id,
                                reply_markup=quick_markup({'Back': {'callback_data': f'account_{card.account_id}'}}))


asyncio.run(bot.polling())
