class Venue:
    
    def __init__(self,name,till):
        self.name = name
        self.till = till
        self.rooms = [] #blank canvas - have to add rooms

    def add_room(self,room_to_add):
        self.rooms.append(room_to_add)    

    def add_money_to_till(self,amount):
        self.till += amount

    def check_guest_in(self,room,guest):
        room.add_guest_to_room(guest)
        self.add_money_to_till(room._room_cost)
