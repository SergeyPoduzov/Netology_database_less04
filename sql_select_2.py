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

#количество исполнителей в каждом жанре;
print('\nколичество исполнителей в каждом жанре:')
sel = connection.execute("""
   SELECT Style.name_style, COUNT(StyleMusician.musician_id) from Style
   JOIN StyleMusician ON Style.id = StyleMusician.style_id
   
   GROUP BY Style.name_style
   ORDER BY COUNT(StyleMusician.musician_id) DESC

""").fetchall()
print(sel)

#количество треков, вошедших в альбомы 2019-2020 годов;
print('\nколичество треков, вошедших в альбомы 2019-2020 годов:')
sel = connection.execute("""
   SELECT COUNT(Record.id) from Album
   JOIN Record ON Album.id = Record.album_id
   WHERE Album.year_bithday BETWEEN 2019 AND 2020;
   

""").fetchall()
print(sel)

#Название треков и год выпуска, вошедших в альбомы 2019-2020 годов;
print('\nНазвание треков и год выпуска, вошедших в альбомы 2019-2020 годов: ')
sel = connection.execute("""
   SELECT Record.name_record, Album.year_bithday  from Album
   JOIN Record ON Album.id = Record.album_id
   WHERE Album.year_bithday BETWEEN 2019 AND 2020;


""").fetchall()
print(sel)

# средняя продолжительность треков по каждому альбому;
print('\nНазвание и средняя продолжительность треков по каждому альбому: ')
sel = connection.execute("""
   SELECT Album.name_album, AVG(Record.length)  from Album
   JOIN Record ON Album.id = Record.album_id
   GROUP BY Album.name_album


""").fetchall()
print(sel)

# все исполнители, которые не выпустили альбомы в 2020 году; (Вывожу исполнителя и год выпкска альбома
print('\nвсе исполнители, которые не выпустили альбомы в 2020 году: ')
sel = connection.execute("""
   SELECT Musician.nickname, Album.year_bithday FROM Musician
   JOIN MusicianAlbum ON Musician.id = MusicianAlbum.musician_id
   JOIN Album ON MusicianAlbum.album_id = Album.id
    WHERE Album.year_bithday !=2020;
   
""").fetchall()
print(sel)

#названия сборников, в которых присутствует конкретный исполнитель (выберите сами  Пол Маккартни) - ;
print('\nназвания сборников, в которых присутствует конкретный исполнитель (  Пол Маккартни):')
sel = connection.execute("""
   SELECT  DISTINCT name_collection, year_bithday FROM Collection
   JOIN СollectionRecord ON Collection.id = СollectionRecord.collection_id
   JOIN Record ON СollectionRecord.record_id = Record.id
   JOIN MusicianAlbum ON Record.album_id = MusicianAlbum.album_id
   JOIN Musician ON MusicianAlbum.musician_id = Musician.id
    WHERE Musician.nickname = 'Пол Маккартни';

""").fetchall()
print(sel)

# название альбомов, в которых присутствуют исполнители более 1 жанра;
print('\nназвание альбомов, в которых присутствуют исполнители более 1 жанра :')
sel = connection.execute("""
   SELECT  Album.name_album FROM Album
   
   JOIN MusicianAlbum ON Album.id = MusicianAlbum.album_id
    JOIN StyleMusician ON MusicianAlbum.musician_id = StyleMusician.musician_id
    JOIN Style ON StyleMusician.style_id = Style.id
    
    GROUP BY Album.name_album
    HAVING COUNT(Style.id)  > 1


""").fetchall()
print(sel)



# наименование треков, которые не входят в сборники;
print('\nнаименование треков, которые не входят в сборники (версия 1 :')
sel = connection.execute("""
    SELECT  Record.id, Record.name_record  FROM Record
    LEFT JOIN СollectionRecord ON Record.id = СollectionRecord.record_id
    WHERE СollectionRecord.record_id is null
    

""").fetchall()
print(sel)


# наименование треков, которые не входят в сборники;
print('\nнаименование треков, которые не входят в сборники (версия 2 :')
sel = connection.execute("""
    SELECT  Record.id, Record.name_record  FROM Record
    WHERE Record.id NOT IN (
            SELECT  Record.id  FROM Record
            JOIN СollectionRecord ON Record.id = СollectionRecord.record_id
            
            )


""").fetchall()
print(sel)


# исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
print('\nисполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько):')
sel = connection.execute("""
    SELECT  Musician.nickname, Record.name_record, Record.length  FROM Musician
    LEFT JOIN MusicianAlbum ON Musician.id = MusicianAlbum.musician_id
    LEFT JOIN Album ON MusicianAlbum.album_id = Album.id
    LEFT JOIN Record ON Album.id = Record.album_id
    
    
    WHERE Record.length = (
             SELECT MIN(Record.length)  FROM Record
            

            )


""").fetchall()
print(sel)



# название альбомов, содержащих наименьшее количество треков.
print('\nназвание альбомов, содержащих наименьшее количество треков:')
sel = connection.execute("""
    SELECT  distinct  Album.name_album  FROM Album
    LEFT JOIN Record ON Record.album_id = Album.id
    WHERE Record.album_id IN (
        SELECT album_id from Record
        GROUP BY album_id
        HAVING  COUNT(id) = (
                SELECT COUNT(id) from Record
                GROUP BY album_id
                ORDER BY COUNT(id) 
                LIMIT 1
      )  
    
    )
   




""").fetchall()
print(sel)