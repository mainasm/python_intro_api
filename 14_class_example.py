#Create a class, plane
class Plane:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    # Method to add passenger to plane
    def add_passenger(self, name):
        if len(self.passengers) < self.capacity:
            self.passengers.append(name)
            return f"Passenger {name} added."
        else:
            return "The plane is full."

    # Method to list passengers
    def list_passengers(self):
        return self.passengers
    
# Creating a Plane instance with a capacity of 4
plane = Plane(4)
#plane_medium = Plane(10)

# Adding passengers
print(plane.add_passenger("Alice"))
print(plane.add_passenger("Bob"))
print(plane.add_passenger("Charlie"))
print(plane.add_passenger("David")) 
print(plane.add_passenger("Mary"))# This should indicate the plane is full

# Listing passengers
print(plane.list_passengers()) # Output: ['Alice', 'Bob', 'Charlie']