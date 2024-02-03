# def __init__(self, capacity): to create a new flight 
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passangers = []
        
# self.passangers.append(name) to add a new name to the passangers list    
# if not self.open_seats() means if there are no more seats, equivalent to if self.open_seats() == 0:
# return False means there are no more seats on the flight
# return True means there are seats on the flight
    def add_passanger(self,name):
        if not self.open_seats():
            return False
        self.passangers.append(name)
        return True

# def open_seats(): to return the number of open seats on the flight
# len means the length of that sequence, to get the number of passenger there are on the flight
    def open_seats(self):
        return self.capacity - len(self.passangers)
        
flight = Flight(4)

people = ["Amira", "Frida", "Hamada", "Yassin", "Tom"]
for person in people:
    if flight.add_passanger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}.")    
