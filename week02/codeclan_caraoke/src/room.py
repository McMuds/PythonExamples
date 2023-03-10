class Room:
    def __init__(self,id,guests):
        self.id = id
        self.guests = guests

    def add_guest_to_room(self,new_guest):
        self.guests.append(new_guest)