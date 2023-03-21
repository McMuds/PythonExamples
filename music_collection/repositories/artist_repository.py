from db.run_sql import run_sql
from models.artist import Artist

def select_all():
    sql_string = "SELECT * FROM artists"
    results = run_sql(sql_string)
    artist_list = []
    for row in results:
        artist = Artist(
            row['artist_name'],
            row['id']
            )
        artist_list.append(artist)

    return artist_list

def insert_artist(artist):
    sql_string = "INSERT INTO artists (artist_name)  VALUES (%s) RETURNING *"
    values = [artist.artist_name]
    results = run_sql(sql_string, values)
    id = results[0]['id']
    # we should amend the object in this routine rather than just pass it back and have the calling module do it
    # because when we save an artist, we should create a whole artist. We return the complete artist
    artist.id = id
    return artist

def update_artist(artist):
    sql_string = "UPDATE artists SET artist_name = %s WHERE id = %s"
    values = [artist.artist_name, artist.id]
    run_sql(sql_string, values)

def select_artist(id):
    sql_string = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    row = run_sql(sql_string, values)
    artist = Artist(row[0]['artist_name'], id)
    return artist

def delete_all():
    sql_string = "DELETE FROM artists"
    run_sql(sql_string)

def delete_artist(artist):
    sql_string = "DELETE FROM artists WHERE id = %s"
    values = [artist.id]
    run_sql(sql_string,values)