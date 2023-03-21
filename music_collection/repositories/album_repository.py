from db.run_sql import run_sql
from models.album import Album
import repositories.artist_repository as artist_repo

import pdb

def select_all():
    sql_string = "SELECT * FROM albums"
    results = run_sql(sql_string)
    album_list = []
    for row in results:
        artist = artist_repo.select_artist(row['artist_id'])
        album = Album(
            row['album_name'],
            row['year_released'],
            artist,
            row['id']
            )
        album_list.append(album)

    return album_list

def insert_album(album):
    sql_string = "INSERT INTO albums (album_name, year_released, artist_id)  VALUES (%s, %s, %s) RETURNING *"
    values = [album.name, album.year, album.artist.id]
    results = run_sql(sql_string, values)
    id = results[0]['id']
    # we should amend the object in this routine rather than just pass it back and have the calling module do it
    # because when we save an album, we should create a whole album. We return the complete album
    album.id = id
    return album

def update_album(album):
    sql_string = "UPDATE albums SET album_name = %s WHERE id = %s"
    values = [album.album_name, album.id]
    run_sql(sql_string, values)

def delete_all():
    sql_string = "DELETE FROM albums"
    run_sql(sql_string)


def select_album(id):
    sql_string = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    row = run_sql(sql_string, values)
    artist = artist_repo.select_artist(row[0]['artist_id'])
    album = Album(row[0]['album_name'], row[0]['year_released'], artist, id)
    return album

def select_artists_albums(artist):
    sql_string = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql_string, values)
    album_list = []
    for row in results:
        album = Album(
            row['album_name'],
            row['year_released'],
            artist,
            row['id']
            )
        album_list.append(album)

    return album_list

def delete_album(album):
    # pdb.set_trace()
    sql_string = "DELETE FROM albums WHERE id = %s"
    values = [album.id]
    run_sql(sql_string,values)