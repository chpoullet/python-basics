# Strings
    # these are a list of characters put together in a list
    # defined by '' or ""

my_string = "Amazing grilled fish"
print(my_string)
print(type(my_string))

# Joining of two strings (concatenation)

first_name = 'Boris'
last_name = 'May'
print(first_name + ' ' + last_name)

full_name = first_name + ' ' + last_name

print(full_name)

# Interpolation --- you inject a string into another string

name = 'Lana'
welcome_message = "Welcome to the DANGEERRZOOOOOOOONE {}".format(name)
welcome_message2 = f"{name}, welcome to the DANGEERRZOOOOOOOONE"
print(welcome_message2)