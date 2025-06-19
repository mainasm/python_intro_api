
#declaring and initializing a tuple
car_tuple = ("Toyota", "BMW", 25, "Merc")

#printing the elements in the tuple
print (car_tuple)

#retrieving the first element of a tuple
print(car_tuple[0])

#retrieving the second element of a tuple
print(car_tuple[1])

#Fetch the length of the tuple
print (len(car_tuple))

#convert tuple to list
car_list = list(car_tuple)

#add item to list
car_list.append("Jeep")

#printing the new list
print(car_list)

#create tuple from casted list
new_car_tuple = tuple(car_list)

#type of new tuple
print(type(new_car_tuple))