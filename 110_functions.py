# Functions
# Functions have one job
# Functions are like machines - they can take in inputs (optionally), do some work (block of code),
# and have outputs

# Best practices
# functions do one small task --> makes things testable
# generally, do not print inside a function, you return instead.

# DRY = don't repeat yourself

# run's a block of code when called


# functions need to be defined then called


#Syntax

#def <name>(args, arg2):
#   block of code
#   block of code
#   return <something> (optional)

# function no arguments
def say_hello():
    return 'hello'

print(say_hello())

# function with arguments

def full_name(f_name, l_name):     # takes in two arguments
    return f_name + ' ' + l_name   # when called, it will concatenate f_name with l_name

print(full_name('Charlie', 'Poullet'))  # prints out full_name

def welcome_message(f_name, l_name):
    full_name_str = full_name(f_name, l_name)
    welcome_str = say_hello()
    return welcome_str + ' ' + full_name_str

print(welcome_message('Charlie','Poullet'))

def adding(num1, num2):
    return num1 + num2

print(adding(4, 5))