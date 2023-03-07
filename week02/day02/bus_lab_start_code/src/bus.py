class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []

    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passengers)
    
    def pick_up(self, passenger_in):
        self.passengers.append(passenger_in)

    def drop_off(self, passenger_out):
        self.passengers.remove(passenger_out)

    def empty_bus(self):
        self.passengers.clear()

    def pick_up_from_stop(self, bus_stop):
        self.passengers.extend(bus_stop.queue)