#Simple function to display a greeting
def greeting():
    print("Hello World. This is a function-generated greeting")

greeting()


#Enhanced greeting function
def greeting(g):
    print(f"Hello {g} ")

greeting("Team")

def name(n):
    return n

# Less efficient approach
def name(n):
    print (n)


# name("")

#Function to compute the area of a traingle
def triangle (b, h):
    return 0.5*b*h

print(triangle(10, 15))

#Definition of cube method
#Calculates volume of a cube
def cube(c):
    return c**3

print(cube(5))

#Default parameters
def greet(name='world'):
    print(f'Hello, {name}!')

#Calling without an argument. Default parameter is invoked
greet()

#Calling with an argument. Default paramter is overridden
greet("Mark")


#Keyword arguments
def greet(greeting, name):
    print(f'{greeting}, {name}!')

#Without keyword arguments
greet('Alice', 'Hi')

#With keyword arguments
greet(name='Alice', greeting='Hi')


#Arbitrary Arguments - The function takes any number of arguments
def greet(*names):
    for name in names:
        print(f'Hello, {name}!')

greet('Alice', 'Bob', 'Charlie', 'Mark', 'Jane')
