# PostgreSQL - Система управления базами данных (СУБД/DBMS)
# Это ряд программ и инструментов позволяющих создавать БД, управлять ею и манипулировать данными внутри(CRUD)
# Postgres - сама база данных, она объектно реляционная, то есть данные хранятся в виде таблиц, и таблицы имеют связи между собой

# SQL (Structured Query Language) - декларативный язык структурированных запросов, он применяется для создания и получения данных при помощи запросов в БД

# команда для входа в БД через юзеров postgres:
# sudo -u postgres psql

# команда для входа
# exit

# команда для входа в своего юзера
# psql

# команда для выхода
# \q

# создание суперюзера
# CREATE ROLE 'username' SUPERUSER LOGIN PASSWORD '1';

# # изменение пароля
# ALTER USER 'username' WITH PASSWORD '1';

# # создание БД
# CREATE DATABASE 'name';

# \l - список всех бд

# \du - все юзеры

# \dt - все таблицы(нужно подключиться к бд заранее)

# \d 'name' - подробная информация про таблицу (нужно подключиться к бд заранее)

# \c 'name' - команда для подключения к бд

# psql -U <username> -d <dbnsmr> - подключаемся под выбранным username к dbname


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Типы полей в Postgres

#Numeric Types(числовы типы)
    # a. smallint(2 bytes) -> -32767 to 32767
    # b. integer(4 bytes) -> -2.147... to 2.147...
    # c. bigint(8 bytes) -> ...
    # d. real (4 bytes) -> число с плавающей точкой, вещественное
    # f. double precsion (8 bytes) -> real, но только с двойной точностью
    # h. serial (4 bytes) -> integer, auto-increment

# Character types(Символьные типы(строковые)):
    # a.varchar(кол-во символов)-> если мы укажем 50 символов, а заполним только 10, то остальные будут свободны. Макс 255
    # b. char(кол-во символов) ->если мы укажем 50 символов, а заполним только 10, то остальные будут заполнены пробелом. Макс 255
    # c. text() -> неогр кол-во символов

# Boolean Type
    # a.boolean(1 types) -> True/False

#date -> календарная дата (год.месяц.день)

# location -> координатная точка (х, у) - (245, -12)

# enumerate types:
    # ('a', 'b', 'c')
    # CREATE TYPE <any name> AS ENUM ('Happy', 'Sad', 'Mad');

# Команда для создания таблицы
# CREATE TABLE <tablename>(
#     <column> <type>,
# )

# CREATE TABLE films (
# code char(5),
# title varchar(100),
# data date,
# genre varchar(50),
# budget integer,
# country varchar(50),
# id serial
# ;
# );

# DROP TABLE <name> - удаление таблицы

# Команда для добавления данных в таблицу
# INSERT INTO <tablename> [(columns)] VALUES (data), (data);

# INSERT INTO films (code, title, data, genre, budget, country) VALUES 
# ('AU56', 'Game of Thrones', '2015-05-31', 'Fantasy', 1000000, 'USA'),
# ('het5', 'Lord of The Rings', '2001-06-12', 'Fantasy', '1200000', 'USA');

# Команда для получения данных 
# SELECT (columns)* FROM <table>;

# Команда для обновления данных
# UPDATE <table> SET <column> = <new_value> WHERE <column> = <value>;

# Команда для удаления данных
# DELETE FROM <table> WHERE <column> = <value>;

# ORDER BY: Позволяет как сортировать выходящие данные по убыванию или возрастанию. ASC (по возрастанию) и DESC(по убыванию)
# Синтаксис: SELECT <row> FROM <tablename> ORDER BY <row> [ASC/DESC]

# WHERE: используется для фильтрации по полям, будут выводится только те данные которые соответсвуют условию оператора WHERE
# Синтаксис: SELECT <row> FROM <tablename> WHERE <row> = 'чему либо'

# BETWEEN: учловие между
# SELECT * FROM products WHERE id BETWEEN 3 and 8

# LIKE: Выводит результат который соответсвует введенному шаблону для строк.
# Чувствителен к регистру

# ILIKE: тоже самое, только не зависит от регистра
# Синтаксис: SELECT <row> FROM <tablename> WHERE <row> LIKE/ILIKE 'чему либо';

# AND оператор и, для множественных условий
# IN: WHERE <row> in (1, 2, 3, 4);


# Эксперт БД (дамп);
# pq_dump -U <username> -d 'dbname' > 'file.sql'

# Импорт:
# psql -U <username> -d <dbname> -f 'file.sql'