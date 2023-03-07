class BusStop:
    def __init__(self, name):
        self.name = name
        self.queue = []

    def add_to_queue(self, passenger):
        self.queue.append(passenger)

    def queue_length(self):
        return len(self.queue)
    
    def clear_queue(self):
        self.queue.clear()