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

# .split() - splits the string into my strings and returns a list
print(my_stringy.split())






# Numerical data types
# int, long, float, complex
# These are numerical types which can use numerical operators

# Complex are built with imaginary numbers.
    # an example would be if you need to track 2 separate currencies
    # in one variable

# Long are just integers of unlimited size

# Int and float
    # int - stands for integer and is a whole number
    # float - numbers with decimal places

# int
my_int = 10
print(my_int)
print(type(my_int))

# float
my_float = 10.1
print(my_float)
print(type(my_float))

# operators - add, subtract, divide, multiply and modulus
num1 = 12
num2 = 21

print(num1 + num2)
print(num1 - num2)
print(num1 / num2)
print(num1 * num2)

# modulus returns the remainder
print(10 % 3) # it does 3 * 3 and 1 is the remainder

print(20//3) # removes the decimal places


# Comparison operators output boolean values
    # == - equating things on both sides
    # < / > - smaller than / bigger than
    # <= - smaller than or equals
    # >= - bigger than or equals
    # != - not equal to
    # is - will give true/false
    # is not - will give true/false

my_variable = 10
my_variable2 = 13

print(my_variable == my_variable2)
print(my_variable == 10)
print(my_variable < my_variable2)

print(my_variable is 10)
print(my_variable is not 10)

# Booleans
# true (1) or false (0)

# None
print(type(None))

print(0 == None)

# Operators, logical and logical Or
a_var = True
b_var = False

# Logical and  & requires both side to be true to result in true
print(a_var & True)
print(a_var & False)


# Logical or, only one side needs to be true to return true:
print(True or False)

# or = one side needs to be True to be True
# & = both sides need to be True to be True