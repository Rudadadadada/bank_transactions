<h1><img align="center" src="https://github.com/Rudadadadada/rudadadadada/blob/master/icons/Telegram.svg" alt="rudadadadada" height="30" width="40" /> Bank transactions chatbot</h1>

<a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.11-brightgreen"></a>
<a href="https://postgresql.org"><img src="https://img.shields.io/badge/Powered%20by-PostgreSQL-blue.svg"/></a>
<a href="https://pypi.org/project/pyTelegramBotAPI/"><img src="https://img.shields.io/badge/Powered%20by-telebot-blue"></a>
<a href="https://www.sqlalchemy.org/"><img src="https://img.shields.io/badge/Powered%20by-SQLAlchemy-red"></a>

## ✒ Project description

- This is a Telegram ***chatbot that outputs client transactions.*** The client has accounts, the accounts have cards. To view transactions, ***you need to select the necessary parameters and then click on the "view transactions" button.***

- It is an ***educational project*** made within the framework of the subject of ***OOP***. 

## 🎬 Demo

![video of working](https://user-images.githubusercontent.com/57627872/210226228-2594a53a-e7e9-40ce-b33e-dac2fbb0e702.gif)

## ❗️Assamption

- Assume that ***you are the administrator of the bank***, all transactions for all customers on all accounts and on all cards are available to you. 

- There is no full-fledged authorization in the project, since the newly registered users do not have completed transactions.

- ***This project just emulates the work of the "Spending" service in the Tinkoff application.***

## 🧩 Functionality

### 1️⃣ Chat

The chat consists of buttons, each of which is a parameter for filtering.

### 2️⃣ Filter

The main filter consists of 4 sub-filters by: product category, month, store, city.

## 🛠️ Tools
- <a href="https://www.postgresql.org/">Database PostgreSQL <img src="https://user-images.githubusercontent.com/57627872/213761059-d18cd77b-29b9-4e20-8f14-3efb384594de.png" height="20" width="20"></a>
- <a href="https://pypi.org/project/pyTelegramBotAPI/">Library telebot <img src="https://user-images.githubusercontent.com/57627872/213766820-75929ee4-6ec0-449e-9d6a-93615fbadb52.png" height="20" width="20"></a>
- <a href="https://www.sqlalchemy.org/">SQLAlchemy <img src="https://user-images.githubusercontent.com/57627872/213767906-ed3861b2-dd7b-4fa4-b626-4808e3b67a13.png" height= "20" width="20"></a>

## 🧮 How data is stored in the database?
***Here are two data storage schemes and the relationships between the models.***

### 📊 First scheme:

There is an admin at the top of everything, he can view information about clients. ***Let's take some client, he has lots of accounts, accounts have lots of cards, cards have lots of transactions.***

<img src="https://user-images.githubusercontent.com/57627872/212759769-a12e421f-786b-4426-a3fb-6176452d8265.png" height="350" width="500">


### 📊 Second scheme:

***The transaction stores information about how much money was spent, at what time and date, the id of the card number and the id of the store where the purchase was made.*** 

The store has a parameter ***merchant category code***, by which we determine which category this store belongs to.

<img src="https://user-images.githubusercontent.com/57627872/212759935-a8ffbf1b-a6e2-475b-8c5f-fbaab46a546f.png" height="150" width="400">

## 📄 What development patterns were used?

### 👀 The observer pattern.

A chatbot is ***a state tree*** where each ***button click is a transition between these states***. The ***administrator*** of the bank in this case ***is an observer***.

### 🪧 The query builder.

When transitions between states are made, ***parameters are also selected to form a query*** to the database.

## ⚙️ Contributors
There are two contributors:

<a href = "https://github.com/rudadadadada/bank_transactions/graphs/contributors">
<img src = "https://contrib.rocks/image?repo=rudadadadada/bank_transactions"/>
</a>
