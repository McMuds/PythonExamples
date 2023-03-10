class Room:
    def __init__(self,id,guests, songs):
        self.id = id
        self.guests = guests
        self.songs = songs
        self._room_size = 3 #default room size.
        self._room_cost = 15 #default room cost

    def add_guest_to_room(self,new_guest):
        if len(self.guests) < self._room_size and \
        self._room_cost <= new_guest.wallet:
            self.guests.append(new_guest)
            new_guest.decrease_wallet(self._room_cost)
            return True
        return False

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
   
    def set_room_cost(self, cost):
        self._room_cost = cost