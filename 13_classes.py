class Person:

    #Constructor for class variables
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old.')

    def message(self):
        print(f"{self.name} loves APIs")

#Instances of person
person_alice = Person('Alice', 30)
person_john = Person('John', 25)

#Calling greet function for each instance
person_alice.greet()  # Output: Hello, my name is Alice and I am 30 years old.
person_john.greet() # Output: Hello, my name is John and I am 25 years old.
person_john.message() 



