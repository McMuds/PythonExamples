import psycopg2
from psycopg2 import extras as ext

from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repo
import repositories.album_repository as album_repo


print(f"Starting - should be empty database")

artist1 = Artist("Bjork")
artist1 = artist_repo.insert_artist(artist1)

artist2 = Artist("Eminem")
artist2 = artist_repo.insert_artist(artist2)

artist1.artist_name = "Pink Floyd"
artist_repo.update_artist(artist1)

artist_results = artist_repo.select_all()
for artist in artist_results:
    print(f"Artist {artist.artist_name} has ID {artist.id}")

print(f"Returning Eminiem")
returned_artist = artist_repo.select_artist(2)
print(f"Artist number 2 is: {returned_artist.artist_name}")

album1 = Album("Dark Side of the Moon", 1963, artist1)
album1 = album_repo.insert_album(album1)

album2 = Album("Slim Shady", 1999, artist2)
album2 = album_repo.insert_album(album2)

album3 = Album("Recovery", 2005, artist2)
album3 = album_repo.insert_album(album3)

album4 = Album("Recovery", 2015, artist2)
album4 = album_repo.insert_album(album4)

album_list = album_repo.select_all()
print(f"\nSELECT ALL")
for album in album_list:
    print(f"Album {album.name} has ID {album.id} and was released by {album.artist.artist_name}")

# album_repo.delete_all()
# album_results = album_repo.select_all()
# for album in album_results:
#     print(f"Album {album.name} has ID {album.id} and was released by {album.artist.artist_name}")

# artist_repo.delete_all()
# artist_results = artist_repo.select_all()
# for artist in artist_results:
#     print(f"Artist {artist.name} has ID {artist.id}")

returned_album = album_repo.select_album(2)
print(f"Returning album 2 {returned_album.name} and was released by {album.artist.artist_name}")

print(f"\n SELECT ALL EMINEM'S ALBUMS")
album_list = album_repo.select_artists_albums(artist2)
print(f"There are {len(album_list)} albums returned for artist {artist2.id}")
for album in album_list:
    print(f"Album {album.name} has ID {album.id} and was released by {album.artist.artist_name}")

print(f"\n delete album 3")
album_repo.delete_album(album3)
album_list = album_repo.select_all()
for album in album_list:
    print(f"Album {album.name} has ID {album.id} and was released by {album.artist.artist_name}")

print(f"\n delete eminem and show all albums remaining")
artist_repo.delete_artist(artist2)
album_list = album_repo.select_all()
for album in album_list:
    print(f"Album {album.name} has ID {album.id} and was released by {album.artist.artist_name}")


print(f"\n showing no Eminem in the artist list")
artist_list = artist_repo.select_all()
for artist in artist_list:
    print(f"Artist {artist.artist_name} has ID {artist.id}")