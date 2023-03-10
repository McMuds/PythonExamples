class Room:
    def __init__(self,id,guests, songs):
        self.id = id
        self.guests = guests
        self.songs = songs
        self._room_size = 3

    def add_guest_to_room(self,new_guest):
        self.guests.append(new_guest)

    def add_song_to_room(self,song):
        self.songs.append(song)

    def remove_guest(self,guest):
        # design decision here - it won't return a message, it'll just handle it.
        if guest in self.guests:
            self.guests.remove(guest)

    def remove_song(self,song):
        # design decision here - it won't return a message, it'll just handle it.
        if song in self.songs:
            self.songs.remove(song)

    def set_room_size(self, size):
        self._room_size = size