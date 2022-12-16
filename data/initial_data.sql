--Debugging data to fill the database.

DELETE FROM public."transactions";
DELETE FROM public."merchants";
DELETE FROM public."mccs";
DELETE FROM public."cards";
DELETE FROM public."accounts";
DELETE FROM public."clients";


--clients
INSERT INTO public."clients" ("id", "surname", "name") VALUES (1, 'Rekhlov', 'Lev');
INSERT INTO public."clients" ("id", "surname", "name") VALUES (2, 'Kuybida', 'Vsevolod');
INSERT INTO public."clients" ("id", "surname", "name") VALUES (3, 'Rudakov', 'Nikita');

--accounts
INSERT INTO public."accounts" ("id", "name", "client_id") VALUES (1, '40817810800038292000', 1);
INSERT INTO public."accounts" ("id", "name", "client_id") VALUES (2, '40817810800038292001', 1);
INSERT INTO public."accounts" ("id", "name", "client_id") VALUES (3, '40817810800038292002', 2);
INSERT INTO public."accounts" ("id", "name", "client_id") VALUES (4, '40817810800038292003', 2);
INSERT INTO public."accounts" ("id", "name", "client_id") VALUES (5, '40817810800038292004', 3);
INSERT INTO public."accounts" ("id", "name", "client_id") VALUES (6, '40817810800038292005', 3);

--cards
INSERT INTO public."cards" ("id", "number", "account_id") VALUES (1, '1234567891234500', 1);
INSERT INTO public."cards" ("id", "number", "account_id") VALUES (2, '1234567891234501', 2);
INSERT INTO public."cards" ("id", "number", "account_id") VALUES (3, '1234567891234502', 3);
INSERT INTO public."cards" ("id", "number", "account_id") VALUES (4, '1234567891234503', 4);
INSERT INTO public."cards" ("id", "number", "account_id") VALUES (5, '1234567891234504', 5);
INSERT INTO public."cards" ("id", "number", "account_id") VALUES (6, '1234567891234505', 6);

--mccs
INSERT INTO public."mccs" ("id", "type", "code") VALUES (1, 'Products', 5411);
INSERT INTO public."mccs" ("id", "type", "code") VALUES (2, 'Internet store', 5300);
INSERT INTO public."mccs" ("id", "type", "code") VALUES (3, 'Electronic store', 5722);
INSERT INTO public."mccs" ("id", "type", "code") VALUES (4, 'Cinema', 7832);

--merchants
--products
INSERT INTO public."merchants" ("id", "name", "mcc_id", "country", "city", "address")
VALUES (1, 'Pyatorochka', 1, 'Russia', 'Balashikha', 'Kosinskoe Highway, 6, New Pavlino microdistrict');
INSERT INTO public."merchants" ("id", "name", "mcc_id", "country", "city", "address")
VALUES (2, 'Magnit', 1, 'Russia', 'Balashikha', 'Kosinskoe Highway, 10, New Pavlino microdistrict');
INSERT INTO public."merchants" ("id", "name", "mcc_id", "country", "city", "address")
VALUES (3, 'Lenta', 1, 'Russia', 'Balashikha', 'Prigorodnaya Street, c90, Savvino microdistrict');
--online_stores
INSERT INTO public."merchants" ("id", "name", "mcc_id", "country", "city", "address")
VALUES (4, 'Ozon', 2, 'Russia', 'Balashikha', 'Boyarinov Street, 9, New Pavlino microdistrict');
INSERT INTO public."merchants" ("id", "name", "mcc_id", "country", "city", "address")
VALUES (5, 'Wildberries', 2, 'Russia', 'Balashikha', 'Kosinskoe Highway, 5/7, New Pavlino microdistrict');
--electronics_stores
INSERT INTO public."merchants" ("id", "name", "mcc_id", "country", "city", "address")
VALUES (6, 'DNS', 3, 'Russia', 'Moscow', 'Generala Kuznetsova Street, 22');
INSERT INTO public."merchants" ("id", "name", "mcc_id", "country", "city", "address")
VALUES (7, 'M.Video', 3, 'Russia', 'Lyubertsy', 'October Avenue, 112');
--cinema
INSERT INTO public."merchants" ("id", "name", "mcc_id", "country", "city", "address")
VALUES (8, 'Pyat zvezd', 4, 'Russia', 'Moscow', 'Bolshoy Ovchinnikovsky lane, 16');
INSERT INTO public."merchants" ("id", "name", "mcc_id", "country", "city", "address")
VALUES (9, 'KARO 10', 4, 'Russia', 'Reutov', 'Nosovikhinskoe Highway, 45');

--transactions
INSERT INTO public."transactions" ("id", "amount", "datetime", "card_id", "merchant_id")
VALUES (1, 4999, '2022-12-21 15:23:54', 2, 4);
INSERT INTO public."transactions" ("id", "amount", "datetime", "card_id", "merchant_id")
VALUES (2, 675, '2022-11-17 13:52:33', 3, 6);
INSERT INTO public."transactions" ("id", "amount", "datetime", "card_id", "merchant_id")
VALUES (3, 100, '2022-10-30 17:20:12', 6, 1);
INSERT INTO public."transactions" ("id", "amount", "datetime", "card_id", "merchant_id")
VALUES (4, 2500, '2022-09-02 16:29:23', 4, 5);
INSERT INTO public."transactions" ("id", "amount", "datetime", "card_id", "merchant_id")
VALUES (5, 799, '2022-10-05 13:41:46', 1, 7);
INSERT INTO public."transactions" ("id", "amount", "datetime", "card_id", "merchant_id")
VALUES (6, 19999, '2022-11-27 12:08:23', 2, 4);
INSERT INTO public."transactions" ("id", "amount", "datetime", "card_id", "merchant_id")
VALUES (7, 3299, '2022-12-28 09:43:57', 5, 4);
INSERT INTO public."transactions" ("id", "amount", "datetime", "card_id", "merchant_id")
VALUES (8, 7500, '2022-10-12 09:40:43', 5, 5);
INSERT INTO public."transactions" ("id", "amount", "datetime", "card_id", "merchant_id")
VALUES (9, 899, '2022-07-14 13:05:33', 1, 5);
INSERT INTO public."transactions" ("id", "amount", "datetime", "card_id", "merchant_id")
VALUES (10, 720, '2022-10-29 11:03:12', 3, 8);
INSERT INTO public."transactions" ("id", "amount", "datetime", "card_id", "merchant_id")
VALUES (11, 329, '2022-12-30 15:01:17', 4, 3);
INSERT INTO public."transactions" ("id", "amount", "datetime", "card_id", "merchant_id")
VALUES (12, 49, '2022-11-12 08:48:00', 6, 1);
INSERT INTO public."transactions" ("id", "amount", "datetime", "card_id", "merchant_id")
VALUES (13, 179880, '2022-09-15 13:16:47', 5, 6);
INSERT INTO public."transactions" ("id", "amount", "datetime", "card_id", "merchant_id")
VALUES (14, 599, '2022-08-12 11:26:38', 2, 2);
INSERT INTO public."transactions" ("id", "amount", "datetime", "card_id", "merchant_id")
VALUES (15, 100, '2022-12-08 10:23:52', 3, 3);