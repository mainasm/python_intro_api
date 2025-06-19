# Conditional statements in Python

# print("Please enter your age")

# age = int(input("Age: "))

# if age >= 21: #if evaluates a given condition 
#     print("Eligible to drive PSV") #execute if true
# elif age >= 18: # evaluate if condition 1 is false
#     print("Eligible to drive private car only") #  execute if true
# else: # evaluates if second condition is false
#     Sprint("Not eligible to drive") #  execute if true


    # Conditional statements in Python

# A small application to compute grade based on marks input evaluation
print("Please enter your mark")
mark = int(input("Mark: "))

if mark >= 70:
    print("Passed. Grade A")
elif mark >= 60:
    print("Passed. Grade B")
elif mark >= 50:
    print("Passed. Grade C")
else:
    print("Fail. Grade D")