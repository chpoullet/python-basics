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

# place an f behind the string and use {} inside the string to
# interpolate variable/python

# Special methods for strings

my_stringy = "      Hello this is an amazing string"

# .count() method
print(my_stringy.count('i'))

# .strip() removes trailing white spaces
print(my_stringy.strip())

# len() - function not a method!
print(len(my_stringy))
print(len(my_stringy.strip()))

# .capitalize() - capitalises the first letter and everything else underscore
print(my_stringy.strip().capitalize())

# .upper() - capitalises every character
print(my_stringy.upper())

# .lower() - lowercases every character
print(my_stringy.lower())

# .split() - splits the characters

print(my_stringy.split())

