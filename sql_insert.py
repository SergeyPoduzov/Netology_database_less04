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


#Вставляем стили

#Добавим новый стиль Rock
connection.execute("""INSERT  INTO style(id, name_style)
    VALUES(1, 'Rock');

""")

#Заменил Rock на Рок
connection.execute("""UPDATE   style
    SET name_style = 'Рок'
    WHERE id = 1;

""")



# Добавим новый стиль Рок-н-ролл
connection.execute("""INSERT  INTO style(id, name_style)
    VALUES(2, 'Рок-н-ролл');

""")

# Добавим новый стиль Блюз
connection.execute("""INSERT  INTO style(id, name_style)
    VALUES(3, 'Блюз');

""")

# Добавим новый стиль 	Фолк-музыка
connection.execute("""INSERT  INTO style(id, name_style)
    VALUES(4, 'Фолк-музыка');

""")

# Добавим новый стиль Кантри
connection.execute("""INSERT  INTO style(id, name_style)
    VALUES(5, 'Кантри');

""")

# Добавим новый стиль Джаз
connection.execute("""INSERT  INTO style(id, name_style)
    VALUES(6, 'Джаз');

""")

# Добавим новый стиль 	Поп-музыка
connection.execute("""INSERT  INTO style(id, name_style)
    VALUES(7, 'Поп-музыка');

""")

# Добавим новый стиль Хип-хоп
connection.execute("""INSERT  INTO style(id, name_style)
    VALUES(8, 'Хип-хоп');

""")

# Добавим новый стиль Шансон
connection.execute("""INSERT  INTO style(id, name_style)
    VALUES(9, 'Шансон');

""")
# Добавим новый стиль Электронная музыка
connection.execute("""INSERT  INTO style(id, name_style)
    VALUES(10, 'Электронная музыка');

""")

# Добавим новый стиль Рэп
connection.execute("""INSERT  INTO style(id, name_style)
    VALUES(11, 'Рэп');

""")

# Добавим новый стиль Диско
connection.execute("""INSERT  INTO style(id, name_style)
    VALUES(12, 'Диско');

""")
# Добавим новый стиль Опера
connection.execute("""INSERT  INTO style(id, name_style)
    VALUES(13, 'Опера');

""")

# Создаем исполнителей
# Добавим нового исполнителя Пол Маккартни
connection.execute("""INSERT  INTO Musician(id, nickname)
    VALUES(1, 'Пол Маккартни');

""")

# Добавим нового исполнителя Джон Леннон
connection.execute("""INSERT  INTO Musician(id, nickname)
    VALUES(2, 'Джон Леннон');

""")


# Добавим нового исполнителя Андрей Макаревич
connection.execute("""INSERT  INTO Musician(id, nickname)
    VALUES(3, 'Андрей Макаревич');

""")


# Добавим нового исполнителя Муслим Магомаев
connection.execute("""INSERT  INTO Musician(id, nickname)
    VALUES(4, 'Муслим Магомаев');

""")


# Добавим нового исполнителя Алла Пугачева
connection.execute("""INSERT  INTO Musician(id, nickname)
    VALUES(5, 'Алла Пугачева');

""")


# Добавим нового исполнителя Леонид Агутин
connection.execute("""INSERT  INTO Musician(id, nickname)
    VALUES(6, 'Леонид Агутин');

""")


# Добавим нового исполнителя Николай Фоменко
connection.execute("""INSERT  INTO Musician(id, nickname)
    VALUES(7, 'Николай Фоменко');

""")



# Добавим нового исполнителя Максим Леонидов
connection.execute("""INSERT  INTO Musician(id, nickname)
    VALUES(8, 'Максим Леонидов');

""")


# Добавим нового исполнителя Гаррик Сукачев
connection.execute("""INSERT  INTO Musician(id, nickname)
    VALUES(9, 'Гаррик Сукачев');

""")


# Добавим нового исполнителя моргенштерн
connection.execute("""INSERT  INTO Musician(id, nickname)
    VALUES(10, 'Моргенштерн');

""")



# Добавим нового исполнителя Мадонна
connection.execute("""INSERT  INTO Musician(id, nickname)
    VALUES(11, 'Мадонна');

""")




sel1 = connection.execute("""SELECT  id, nickname FROM Musician

""").fetchall()
print(sel1)

# Заполняем связь StyleMusician (Жанр-Исполнитель)
# Заполняем стили Пол-Пол Маккартни Рок

connection.execute("""INSERT  INTO StyleMusician(musician_id, style_id)
    VALUES(1, 1);

""")
# Заполняем стили Пол-Пол Маккартни Рок-н-ролл
connection.execute("""INSERT  INTO StyleMusician(musician_id, style_id)
    VALUES(1, 2);

""")

# Заполняем стили Джон Леннон Рок

connection.execute("""INSERT  INTO StyleMusician(musician_id, style_id)
    VALUES(2, 1);

""")
# Заполняем стили Джон Леннон Рок-н-ролл
connection.execute("""INSERT  INTO StyleMusician(musician_id, style_id)
    VALUES(2, 2);

""")

# Заполняем стили Андрей Макаревич Рок

connection.execute("""INSERT  INTO StyleMusician(musician_id, style_id)
    VALUES(3, 1);

""")
# Заполняем стили Андрей Макаревич Рок-н-ролл
connection.execute("""INSERT  INTO StyleMusician(musician_id, style_id)
    VALUES(3, 2);

""")
# Заполняем стили Андрей Макаревич Поп-музыка
connection.execute("""INSERT  INTO StyleMusician(musician_id, style_id)
    VALUES(3, 7);

""")

# Заполняем стили Муслим Магомаев Поп-музыка

connection.execute("""INSERT  INTO StyleMusician(musician_id, style_id)
    VALUES(4, 7);

""")
# Заполняем стили Муслим Магомаев Опера
connection.execute("""INSERT  INTO StyleMusician(musician_id, style_id)
    VALUES(4, 13);

""")

# Заполняем стили Алла Пугачева Поп-музыка

connection.execute("""INSERT  INTO StyleMusician(musician_id, style_id)
    VALUES(5, 7);

""")
# Заполняем стили Алла Пугачева Шансон
connection.execute("""INSERT  INTO StyleMusician(musician_id, style_id)
    VALUES(5, 12);

""")

# Заполняем стили Леонид Агутин Поп-музыка

connection.execute("""INSERT  INTO StyleMusician(musician_id, style_id)
    VALUES(6, 7);

""")
# Заполняем стили Леонид Агутин Хип-хоп
connection.execute("""INSERT  INTO StyleMusician(musician_id, style_id)
    VALUES(6, 8);

""")

# Заполняем стили Николай Фоменко Рок

connection.execute("""INSERT  INTO StyleMusician(musician_id, style_id)
    VALUES(7, 1);

""")
# Заполняем стили Николай Фоменко Рок-н-ролл
connection.execute("""INSERT  INTO StyleMusician(musician_id, style_id)
    VALUES(7, 2);

""")

# Заполняем стили Николай Фоменко Фолк-музыка
connection.execute("""INSERT  INTO StyleMusician(musician_id, style_id)
    VALUES(7, 4);

""")


# Заполняем стили Максим Леонидов Рок

connection.execute("""INSERT  INTO StyleMusician(musician_id, style_id)
    VALUES(8, 1);

""")
# Заполняем стили Максим Леонидов Рок-н-ролл
connection.execute("""INSERT  INTO StyleMusician(musician_id, style_id)
    VALUES(8, 2);

""")

# Заполняем стили Максим Леонидов Фолк-музыка
connection.execute("""INSERT  INTO StyleMusician(musician_id, style_id)
    VALUES(8, 4);

""")

# Заполняем стили Гаррик Сукачев Рок
connection.execute("""INSERT  INTO StyleMusician(musician_id, style_id)
    VALUES(9, 1);

""")

# Заполняем стили Моргенштерн Рэп
connection.execute("""INSERT  INTO StyleMusician(musician_id, style_id)
    VALUES(10, 11);

""")

# Заполняем стили Мадонна Диско
connection.execute("""INSERT  INTO StyleMusician(musician_id, style_id)
    VALUES(11, 12);

""")
# Заполняем стили Мадонна Поп-музыка
connection.execute("""INSERT  INTO StyleMusician(musician_id, style_id)
    VALUES(11, 7);

""")

# заполняем Альбомы

# Заполняем 	Rubber Soul - The Beatles 1965  (треки Michelle, Girl)
connection.execute("""INSERT  INTO Album(id, name_album, year_bithday )
    VALUES(1, 'Rubber Soul', 1965);
    """)

# Заполняем 	White Album - The Beatles 1968 (While My Guitar Gently Weeps, Back in the U.S.S.R.)
connection.execute("""INSERT  INTO Album(id, name_album, year_bithday )
    VALUES(2, 'White Album', 1968);
    """)

# Заполняем 	«Ты и я" - Секрет 1984 («Тысяча пластинок» и «Она не понимает», а также кавер-версию песни лидера «Зоопарка» Майка Науменко «Мажорный рок-н-ролл»)
connection.execute("""INSERT  INTO Album(id, name_album, year_bithday )
    VALUES(3, 'Ты и я', 1984);
    """)

# Заполняем 	«Бит-квартет „Секрет“" - Секрет 1987 («Твой папа был прав», «Сара Барабу», «Моя любовь на пятом этаже»)
connection.execute("""INSERT  INTO Album(id, name_album, year_bithday )
    VALUES(4, 'Бит-квартет Секрет', 1987);
    """)

# Заполняем 	"Отрываясь" - Машина-Времени 1997 (Однажды мир прогнётся под нас 03:14,
# Такие дела, ангел мой 02:23, Старая песня о главном (П. Подгородецкий — А. Макаревич) 04:10)
connection.execute("""INSERT  INTO Album(id, name_album, year_bithday )
    VALUES(5, 'Отрываясь', 1997);
    """)

# Заполняем 	"Картонные крылья любви" - Машина-Времени 1996
# (Спускаясь к великой реке (Александр Кутиков — Макаревич) — 3:38,Картонные крылья любви (Макаревич) — 4:28 )
connection.execute("""INSERT  INTO Album(id, name_album, year_bithday )
    VALUES(6, 'Картонные крылья любви', 1996);
    """)

# Заполняем 	"Внештатный командир Земли" - Машина-Времени 1993
# (Мой друг (лучше всех играет блюз) (музыкальная обработка Е. Маргулис — литературная обработка А. Макаревич) 04:09, )
# Когда я был большим (музыкальная обработка П. Подгородецкий — литературная обработка А. Макаревич) 03:08
connection.execute("""INSERT  INTO Album(id, name_album, year_bithday )
    VALUES(7, 'Внештатный командир Земли', 1993);
    """)

#Бременские музыканты Муслим Магомаев (Луч солнца золотого, Романтики с большой дороги)
connection.execute("""INSERT  INTO Album(id, name_album, year_bithday )
    VALUES(8, 'Бременские музыканты', 1969);
    """)

#Арлекино и другие аЛЛА пУГАЧЕВА («Мне нравится»#из т/ф «Ирония судьбы, или С лёгким паром!»,
# «У зеркала» из т/ф «Ирония судьбы, или С лёгким паром!»
# «По улице моей» из т/ф «Ирония судьбы, или С лёгким паром!»)
connection.execute("""INSERT  INTO Album(id, name_album, year_bithday )
    VALUES(9, 'Арлекино и другие', 1979);
    """)
#Леонид Агутин - La Vida Cosmopolita 2020
# Funky Cha
# Quédate / Diego Torres
connection.execute("""INSERT  INTO Album(id, name_album, year_bithday )
    VALUES(10, 'La Vida Cosmopolita', 2020);
    """)

# Гаррик Сукачев Ночной полет
# 	Моя бабушка курит трубку 05:59
# Свободу Анджеле Дэвис! 04:21
connection.execute("""INSERT  INTO Album(id, name_album, year_bithday )
    VALUES(11, 'Ночной полет', 2002);
    """)

# Моргенштерн Легендарная пыль 2020
# ЧЕТЫРЕ УКРАИНКИ 2:03
# Я ПЫЛЬ 1:48
connection.execute("""INSERT  INTO Album(id, name_album, year_bithday )
    VALUES(12, 'Легендарная пыль', 2020);
    """)

# Мадонна True Blue 1986
# «Open Your Heart» 4:13
# «True Blue» 4:18
connection.execute("""INSERT  INTO Album(id, name_album, year_bithday )
    VALUES(13, ' True Blue', 1986);
    """)

#Добавляем треки Michelle,  Rubber Soul - The Beatles 1965
connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(1, ' Michelle', 167, 1);
    """)
# Girl
connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(2, ' Girl', 160, 1);
    """)



# White Album - The Beatles 1968 (While My Guitar Gently Weeps, )
connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(3, 'While My Guitar Gently Weeps', 286, 2);
    """)

# White Album - The Beatles 1968 - Back in the U.S.S.R.)
connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(4, 'Back in the U.S.S.R.', 163, 2);
    """)

# # Заполняем 	«Ты и я" - Секрет 1984 («Тысяча пластинок»
connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(5, 'Тысяча пластинок', 187, 3);
    """)

# # Заполняем 	«Ты и я" - Секрет 1984 (Моя любовь на пятом этаже)
connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(6, 'Моя любовь на пятом этаже', 180, 3);
    """)

# # Заполняем 	«Бит-квартет Секрет" - Секрет 1984 (Моя любовь на пятом этаже)
connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(7, 'Сара Бара-Бу', 154, 4);
    """)

# # Заполняем 	«Бит-квартет Секрет" - Секрет 1984 (Моя любовь на пятом этаже)
connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(8, 'Именины у Кристины', 178, 4);
    """)

# # Заполняем 	"Отрываясь" - Машина-Времени 1997 (Однажды мир прогнётся под нас 03:14,
# # Такие дела, ангел мой 02:23, Старая песня о главном (П. Подгородецкий — А. Макаревич) 04:10)
connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(9, 'Однажды мир прогнётся под нас', 194, 5);
    """)

connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(10, 'Такие дела, ангел мой', 143, 5);
    """)
connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(11, 'Старая песня о главном', 250, 5);
    """)


# # Заполняем 	"Картонные крылья любви" - Машина-Времени 1996
# # (Спускаясь к великой реке (Александр Кутиков — Макаревич) — 3:38,
# Картонные крылья любви (Макаревич) — 4:28 )
connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(12, 'Спускаясь к великой реке', 218, 6);
    """)

connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(13, 'Картонные крылья любви', 268, 6);
    """)

 # Заполняем 	"Внештатный командир Земли" - Машина-Времени 1993
# # (Мой друг (лучше всех играет блюз)  04:09, )
# # Когда я был большим  03:08

connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(14, 'Мой друг (лучше всех играет блюз)', 249, 7);
    """)
connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(15, 'Когда я был большим', 188, 7);
    """)

# #Бременские музыканты Муслим Магомаев (Луч солнца золотого, Романтики с большой дороги)
connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(16, 'Луч солнца золотого', 123, 8);
    """)

connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(17, 'Романтики с большой дороги', 135, 8);
    """)


# #Арлекино и другие аЛЛА пУГАЧЕВА («Мне нравится»#из т/ф «Ирония судьбы, или С лёгким паром!»,
# # «У зеркала» из т/ф «Ирония судьбы, или С лёгким паром!»
# # «По улице моей» из т/ф «Ирония судьбы, или С лёгким паром!»)

connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(18, 'Мне нравится', 97, 9);
    """)

connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(19, 'У зеркала', 109, 9);
    """)

connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(20, 'По улице моей', 109, 9);
    """)

# #Леонид Агутин - La Vida Cosmopolita 2020
# # Funky Cha
# # Quédate / Diego Torres
connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(21, 'Funky Cha', 212, 10);
    """)

connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(22, 'Quédate', 207, 10);
    """)

# # Гаррик Сукачев Ночной полет
# # 	Моя бабушка курит трубку 05:59
# # Свободу Анджеле Дэвис! 04:21
connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(23, 'Моя бабушка курит трубку', 359, 11);
    """)
connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(24, 'Свободу Анджеле Дэвис!', 261, 11);
    """)
# # Моргенштерн Легендарная пыль 2020
# # ЧЕТЫРЕ УКРАИНКИ 2:03
# # Я ПЫЛЬ 1:48
connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(25, 'Легендарная пыль', 123, 12);
    """)
connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(26, 'Я ПЫЛЬ', 108, 12);
    """)


#
# # Мадонна True Blue 1986
# # «Open Your Heart» 4:13
# # «True Blue» 4:18
connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(27, 'Open Your Heart', 253, 13);
    """)
connection.execute("""INSERT  INTO Record(id, name_record, length, album_id )
    VALUES(28, 'True Blue', 258, 13);
    """)

# Создаем коллекции
# Love 2006 года из песен The Beatles
connection.execute("""INSERT  INTO Collection(id, name_collection, year_bithday)
    VALUES(1, 'Love', 2006);
    """)

connection.execute("""INSERT  INTO СollectionRecord(id, collection_id, record_id)
    VALUES(1, 1, 1);
    """)
connection.execute("""INSERT  INTO СollectionRecord(id, collection_id, record_id)
    VALUES(2, 1, 2);
    """)
connection.execute("""INSERT  INTO СollectionRecord(id, collection_id, record_id)
    VALUES(3, 1, 3);
    """)
connection.execute("""INSERT  INTO СollectionRecord(id, collection_id, record_id)
    VALUES(4, 1, 4);
    """)

#Коллекция русского рока
connection.execute("""INSERT  INTO Collection(id, name_collection, year_bithday)
    VALUES(2, 'Коллекция русского рока', 2002);
    """)

connection.execute("""INSERT  INTO СollectionRecord(id, collection_id, record_id)
    VALUES(5, 2, 9);
    """)
connection.execute("""INSERT  INTO СollectionRecord(id, collection_id, record_id)
    VALUES(6, 2, 23);
    """)

#Баллады о любви
connection.execute("""INSERT  INTO Collection(id, name_collection, year_bithday)
    VALUES(3, 'Баллады о любви', 2006);
    """)

connection.execute("""INSERT  INTO СollectionRecord(id, collection_id, record_id)
    VALUES(7, 3, 2);
    """)
connection.execute("""INSERT  INTO СollectionRecord(id, collection_id, record_id)
    VALUES(8, 3, 16);
    """)
connection.execute("""INSERT  INTO СollectionRecord(id, collection_id, record_id)
    VALUES(9, 3, 27);
    """)

#Песни из Мультиков 2010
connection.execute("""INSERT  INTO Collection(id, name_collection, year_bithday)
    VALUES(4, 'Песни из Мультиков', 2010);
    """)
connection.execute("""INSERT  INTO СollectionRecord(id, collection_id, record_id)
    VALUES(10, 4, 16);
    """)
connection.execute("""INSERT  INTO СollectionRecord(id, collection_id, record_id)
    VALUES(11, 4, 17);
    """)

#Анталогия русской эстрады 1997
connection.execute("""INSERT  INTO Collection(id, name_collection, year_bithday)
    VALUES(5, 'Анталогия русской эстрады', 1997);
    """)
connection.execute("""INSERT  INTO СollectionRecord(id, collection_id, record_id)
    VALUES(12, 5, 6);
    """)
#Дискотека 90-х
connection.execute("""INSERT  INTO Collection(id, name_collection, year_bithday)
    VALUES(6, 'Дискотека 90-х', 1996);
    """)
connection.execute("""INSERT  INTO СollectionRecord(id, collection_id, record_id)
    VALUES(13, 6, 7);
    """)
connection.execute("""INSERT  INTO СollectionRecord(id, collection_id, record_id)
    VALUES(14, 6, 11);
    """)
#Песни из советских кинофильмов
connection.execute("""INSERT  INTO Collection(id, name_collection, year_bithday)
    VALUES(7, 'Песни из советских кинофильмов', 2017);
    """)

connection.execute("""INSERT  INTO СollectionRecord(id, collection_id, record_id)
    VALUES(15, 7, 18);
    """)
connection.execute("""INSERT  INTO СollectionRecord(id, collection_id, record_id)
    VALUES(16, 7, 20);
    """)

#Классика русского рэпа
connection.execute("""INSERT  INTO Collection(id, name_collection, year_bithday)
    VALUES(8, 'Классика русского рэпа', 2021);
    """)
connection.execute("""INSERT  INTO СollectionRecord(id, collection_id, record_id)
    VALUES(17, 8, 25);
    """)

#Заполнем таблицу MusicianAlbum
connection.execute("""INSERT  INTO MusicianAlbum(id, musician_id, album_id)
    VALUES
      (1, 1, 1),
      (2, 1, 2),
      (3, 2, 1),
      (4, 2, 2), 
      (5, 3, 5),
      (6, 3, 6),
      (7, 3, 7),
      (8, 4, 8),
      (9, 5, 9),
      (10, 6, 10),
      (11, 7, 3),
      (12, 7, 4),
      (13, 8, 3),
      (14, 8, 4),
      (15, 9, 11),
      (16, 10, 12),
      (17, 11, 13),
      (18, 11, 14);
    """)