class Room:
    def __init__(self,id,guests, songs):
        self.id = id
        self.guests = guests
        self.songs = songs

    def add_guest_to_room(self,new_guest):
        self.guests.append(new_guest)

    def add_song_to_room(self,song):
        self.songs.append(song)