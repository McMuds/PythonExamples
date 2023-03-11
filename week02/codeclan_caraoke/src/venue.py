class Venue:
    
    def __init__(self,name,till):
        self.name = name
        self.till = till
        self.rooms = [] #blank canvas - have to add rooms
        self._venue_age_limit = 15
        self.drinks = []

    def add_room(self,room_to_add):
        self.rooms.append(room_to_add)    

    def add_money_to_till(self,amount):
        self.till += amount

    def check_guest_in(self,room,guest):
        if guest.age < self._venue_age_limit:
            return False
        if room.add_guest_to_room(guest):
            self.add_money_to_till(room._room_cost)
            return True

    def transfer_guest(self,guest,old_room,new_room):
        if old_room.remove_guest(guest):
            if self.check_guest_in(new_room,guest):
                pass
            else:
                self.check_guest_in(old_room,guest)
                self.refund_charges(guest,old_room)

    def refund_charges(self,guest,old_room):
        refund_amount = old_room._room_cost * -1
        guest.decrease_wallet(refund_amount)
        self.add_money_to_till(refund_amount)

    def add_drink(self,drink):
        self.drinks.append(drink)

    def sell_drink(self,drink,guest):
        if drink in self.drinks:
            if (guest.age > 18 and drink.abv > 0) or drink.abv == 0: #ignore the law
                self.drinks.remove(drink)
                guest.decrease_wallet(drink.price)
                self.add_money_to_till(drink.price)