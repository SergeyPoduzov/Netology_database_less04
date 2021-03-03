import sqlalchemy


#Импорт ключа к базе  'postgresql://postgres:xxxx@localhost:5432/pagila'
link_to_database=''
with open('files/link.txt') as f:
    link_to_database=f.read()
print(link_to_database)


# создаем engine
engine = sqlalchemy.create_engine(link_to_database)
print(engine)

# Усстановим соединение
connection = engine.connect()

#Посмотетм какие есть таблицы
print(engine.table_names())

# Вывести всех ID и имена исполнителей
sel1 = connection.execute("""SELECT  id, nickname FROM Musician
""").fetchall()
print(sel1)

# Вывести всех ID и названия жанров
sel1 = connection.execute("""SELECT  id, name_style FROM style
""").fetchall()
print(sel1)

# Вывести всех musician_id, style_id из StyleMusician
sel1 = connection.execute("""SELECT  musician_id, style_id FROM StyleMusician
""").fetchall()
print(sel1)

# Вывести всех id, name_album, year_bithday из Альбомов
sel1 = connection.execute("""SELECT  id, name_album, year_bithday FROM Album
""").fetchall()
print(sel1)

# Вывести всех id, name_record, length, album_id  из Треков
sel1 = connection.execute("""SELECT  id, name_record, length, album_id FROM Record
""").fetchall()
print(sel1)

# Вывести всех id, name_collection, year_bithday  из Сборников
sel1 = connection.execute("""SELECT  id, name_collection, year_bithday FROM Collection
""").fetchall()
print(sel1)

# Вывести всех id, collection_id, record_id  из СollectionRecord
sel1 = connection.execute("""SELECT  id, collection_id, record_id FROM СollectionRecord
""").fetchall()
print(sel1)

#Запросы по домашней работе
# название и год выхода альбомов, вышедших в 2018 году;
print('\nНазвание и год выхода альбомов, вышедших в 2018 году:')
sel1 = connection.execute("""SELECT  name_album, year_bithday FROM Album
    WHERE year_bithday = 2018
""").fetchall()
print(sel1)

# название и продолжительность самого длительного трека;
print('\nНазвание и продолжительность самого длительного трека:')
sel2 = connection.execute("""SELECT  name_record, length FROM Record
    ORDER BY length DESC
    LIMIT 1;
""").fetchall()
print(sel2)


#название треков, продолжительность которых не менее 3,5 минуты;
print('\nНазвание треков, продолжительность которых не менее 3,5 минуты:')
sel3 = connection.execute("""SELECT  name_record FROM Record
    WHERE length >=210;
    """).fetchall()
print(sel3)

# названия сборников, вышедших в период с 2018 по 2020 год включительно;
print('\nНазвания сборников, вышедших в период с 2018 по 2020 год включительно:')
sel4 = connection.execute("""SELECT  name_collection FROM Collection
     WHERE year_bithday BETWEEN 2018 AND 2020;
    """).fetchall()
print(sel4)

# исполнители, чье имя состоит из 1 слова;
print('\nИсполнители, чье имя состоит из 1 слова:')
sel5 = connection.execute("""SELECT  nickname FROM Musician
     WHERE nickname NOT LIKE '%% %%'
    """).fetchall()
print(sel5)

# название треков, которые содержат слово "мой"/"my".
print('\nНазвание треков, которые содержат слово "мой"/"my":')
sel6 = connection.execute("""SELECT  name_record FROM Record
     WHERE name_record  LIKE '%%мой%%' OR name_record  LIKE '%%my%%' OR name_record LIKE '%%Мой%%' OR name_record  LIKE '%%My%%'
    """).fetchall()
print(sel6)