
#Creating and initializing a set
my_cities = {"Kampala", "Kigali", "Nairobi", "Mombasa", "Arusha", "Nairobi"}

#printing all the set elements
print(my_cities)

#printing the length of the set
print(len(my_cities))

#printing the type of structure
print(type(my_cities))

#add items to set
my_cities.add("Cape Town")

print(my_cities)

other_cities = {"Nakuru", "Naivasha", "Mwanza","Jiji", "Busia"}

my_cities.update(other_cities)

print(my_cities)

super_cities = {"New York", "Washington", + {"California","Oakland", "LA"}}