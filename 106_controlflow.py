# Control flow
# if statements
# control where the code will execute, depending on assertions/conditions
# An assertion/condition is something that returns true or false

# Syntax:
# block of code - refers to consecutive lines of code that are indented and will run together.
# in simple words, block of code is a specific piece of code that will run at a specific time

# if <condition>:
    # Block of code indented
# elif <condition>:
    # Block of code
# else:              (if none are true do else)
    # block of code

weather = 'stormy and rainy'   # remember case sensitive

if weather == 'rainy':
    print('Take umbrella!')
elif weather == 'stormy':
    print('take rain coat')
elif 'stormy' in weather and 'rainy' in weather:      # if it is both stormy and rainy, then stay at home
    print('stay at home')
else:
    print('Take sunglasses')

# print('I am outside and will always run')


age = 17
driver_license = True

if age >= 18 and driver_license == True:
    print('You can vote and drive')
elif age >= 18:
    print('You can vote')
elif age == 17 and driver_license == True:
    print('You can drive but cannot buy drinks')
elif driver_license == True:
    print('You can drive')
elif age >= 16 < 18:
    print("You can't buy drinks, but someone might help you out")
else:
    print('Go back to school!')
