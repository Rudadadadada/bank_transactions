from telebot.async_telebot import AsyncTeleBot
import asyncio
from bot_utils import get_clients_as_dict, get_sent_messages, add_sent_message, get_possible_months, \
    MONTHS, get_transactions_by_filter, get_possible_cities, get_possible_categories, get_possible_merchants
from telebot.util import quick_markup
from data.account import Account
from data.card import Card
from data.client import Client
from config import TOKEN, DATABASE
from data.db_session import create_session, global_init

# Initialization of database and bot.
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


@bot.callback_query_handler(func=lambda call: call.data.startswith('client_'))
async def get_client(call):
    client_id = int(call.data.split('_')[1])
    client = session.query(Client).filter(Client.id == client_id).first()
    await bot.answer_callback_query(call.id, f'Getting client {client.name} accounts...')
    await asyncio.sleep(1)
    accounts_dict = client.get_accounts_as_dict()
    accounts_dict['View transactions'] = {'callback_data': f'getfilter_client_{client_id}'}
    accounts_dict['Back'] = {'callback_data': 'get_all_clients'}
    await bot.edit_message_text(f'Accounts of {client.name}:', call.message.chat.id, call.message.message_id,
                                reply_markup=quick_markup(accounts_dict, row_width=2))


@bot.callback_query_handler(func=lambda call: call.data.startswith('getfilter_'))
async def get_filters(call):
    object = call.data[call.data.find('_') + 1:]
    await bot.answer_callback_query(call.id, f"Getting available filters...")
    await asyncio.sleep(1)
    await bot.edit_message_text(f"Choose filter for transactions:", call.message.chat.id, call.message.message_id,
                                reply_markup=quick_markup({
                                    'Month': {'callback_data': f'filter_{object}_month'},
                                    'Category': {'callback_data': f'filter_{object}_category'},
                                    'City': {'callback_data': f'filter_{object}_city'},
                                    'Merchant': {'callback_data': f'filter_{object}_merchant'},
                                    'Back': {'callback_data': f'{object}'}
                                }, row_width=2))


@bot.callback_query_handler(func=lambda call: call.data.startswith('filter_') and (
        call.data.endswith('_month') or call.data.endswith('_category') or call.data.endswith(
    '_city') or call.data.endswith('_merchant')))
async def filter_transactions(call):
    _, object_type, object_id, filter_type = call.data.split('_')
    await bot.answer_callback_query(call.id, f"Getting available filters...")
    await asyncio.sleep(1)
    if filter_type == 'month':
        possible_months = get_possible_months(session, object_type, object_id)
        months_dict = {}
        for month in possible_months:
            months_dict[MONTHS[month]] = {'callback_data': f'transactions_{object_type}_{object_id}_month_{month}'}
        months_dict['Back'] = {'callback_data': f'getfilter_{object_type}_{object_id}'}
        await bot.edit_message_text(f"Choose month:", call.message.chat.id, call.message.message_id,
                                    reply_markup=quick_markup(months_dict, row_width=1))

    elif filter_type == 'city':
        possible_cities = get_possible_cities(session, object_type, object_id)
        cities_dict = {}
        for city in possible_cities:
            cities_dict[city] = {'callback_data': f'transactions_{object_type}_{object_id}_city_{city}'}
        cities_dict['Back'] = {'callback_data': f'getfilter_{object_type}_{object_id}'}
        await bot.edit_message_text(f"Choose city:", call.message.chat.id, call.message.message_id,
                                    reply_markup=quick_markup(cities_dict, row_width=1))

    elif filter_type == 'category':
        possible_categories = get_possible_categories(session, object_type, object_id)
        categories_dict = {}
        for category in possible_categories:
            categories_dict[category] = {'callback_data': f'transactions_{object_type}_{object_id}_category_{category}'}
        categories_dict['Back'] = {'callback_data': f'getfilter_{object_type}_{object_id}'}
        await bot.edit_message_text(f"Choose category:", call.message.chat.id, call.message.message_id,
                                    reply_markup=quick_markup(categories_dict, row_width=1))

    elif filter_type == 'merchant':
        possible_merchants = get_possible_merchants(session, object_type, object_id)
        merchants_dict = {}
        for merchant in possible_merchants:
            merchants_dict[merchant] = {'callback_data': f'transactions_{object_type}_{object_id}_merchant_{merchant}'}
        merchants_dict['Back'] = {'callback_data': f'getfilter_{object_type}_{object_id}'}
        await bot.edit_message_text(f"Choose merchant:", call.message.chat.id, call.message.message_id,
                                    reply_markup=quick_markup(merchants_dict, row_width=1))


@bot.callback_query_handler(func=lambda call: call.data.startswith('transactions_'))
async def get_transactions(call):
    _, object_type, object_id, filter_type, filter_value = call.data.split('_')
    await bot.answer_callback_query(call.id, f"Getting transactions...")
    await asyncio.sleep(1)
    transactions = get_transactions_by_filter(session, object_type, object_id, filter_type, filter_value)
    transactions_str = '\n'.join([str(transaction) for transaction in transactions])
    await bot.edit_message_text(transactions_str, call.message.chat.id, call.message.message_id,
                                reply_markup=quick_markup(
                                    {'Back': {'callback_data': f'filter_{object_type}_{object_id}_{filter_type}'}}))


@bot.callback_query_handler(func=lambda call: call.data.startswith('account_'))
async def get_account(call):
    account_id = int(call.data.split('_')[1])
    account = session.query(Account).filter(Account.id == account_id).first()
    await bot.answer_callback_query(call.id, f'Getting account {account.name} cards...')
    await asyncio.sleep(1)
    cards_dict = account.get_cards_as_dict()
    cards_dict['Back'] = {'callback_data': f'client_{account.client_id}'}
    cards_dict['View transactions'] = {'callback_data': f'getfilter_account_{account_id}'}
    await bot.edit_message_text(f'Cards of account: {account.name}', call.message.chat.id, call.message.message_id,
                                reply_markup=quick_markup(cards_dict, row_width=2))


@bot.callback_query_handler(func=lambda call: call.data.startswith('card_'))
async def get_card(call):
    card_id = int(call.data.split('_')[1])
    card = session.query(Card).filter(Card.id == card_id).first()
    call.data = f'account_{card.account_id}'
    await get_account(call)


# Start polling
asyncio.run(bot.polling())
