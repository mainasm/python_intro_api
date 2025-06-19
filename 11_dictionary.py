# Declaring a dictionary
# my_phone = {
#     "Brand" : "Samsung",
#     "Make"  : "Galaxy",
#     "Version" : "S21",
#     "YoM" : 2021,
#     "Origin" : "South Korea"
# }


# print (my_phone)

# # Access a value by its key
# print(f'My phone make is: {my_phone["Make"]} and the version is : {my_phone["Version"]}')

# A nested dictionary
my_phones = {
    "phone_one": {
        "Brand": "Samsung",
        "Make": "Galaxy",
        "Version": "S21",
        "YoM": 2021,
        "Origin": "South Korea"
    },

    "phone_two": {
        "Brand": "Apple",
        "Make": "iPhone",
        "Version": "13",
        "YoM": 2021,
        "Origin": "USA"
    }
}


print(my_phones["phone_one"])
print(my_phones["phone_two"])


for phone in my_phones:
    print(my_phones[phone])


