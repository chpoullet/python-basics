# List

# defining a list
crazy_landlords = []

# We can dynamically define a list or redefine a list
crazy_landlords = ['Mr Richards', 'Raj', 'Mr. Shirik', 'Zemu']

# Access a object in a list
# to do this we use indexes (0,1,2,3,4)
# to access landlord 'Raj' we need the index number '1'.
print(crazy_landlords[1])

# we can also redefine at a specific index
# change Zemu to Zemmu
crazy_landlords[3] = 'Zemmu'
print(crazy_landlords[3])

# Printing the last record
print(crazy_landlords[-1])

# another way it to get the length and make into an index
length_list = len(crazy_landlords)
last_index = length_list - 1
print(crazy_landlords[last_index])

# Adding a record to the list
# .append()

crazy_landlords.append('Lana')
print(crazy_landlords)

# What if we need to insert a record on a specific index
# .insert()

crazy_landlords.insert(0, 'Bob')
print(crazy_landlords)

# Remove item from list, according to value
# .remove()

crazy_landlords.remove('Zemmu')
print(crazy_landlords)

# Remove using index
# .pop()

crazy_landlords.pop() # removes entry on last index
crazy_landlords.pop(0)  # removes at specific index
print(crazy_landlords)


## We can have mixed data list
hybrid_last = ['JSON', 'Jason', 13, 53, [1, 2]]
print(hybrid_last)
print(type(hybrid_last))





## Tuples
# immutable list and is () instead of []

my_tuple = (2, 'hello', 22, 'more values')
print(my_tuple)

# my_tuple[0] = 10 will not work as tuples cannot be reassigned

print(my_tuple[1][0]) # this shows you the first character of index 1 (h from hello)

# Range slicing ---  ['Mr Richards', 'Raj', 'Mr. Shirik', 'Zemu']
print(crazy_landlords[0:1])    # 0 to 1, but not inclusive of index 1
print(crazy_landlords[1:2])    # 1 to 2, not inclusive of 2


# Jumping
# syntax[B:E:S]
# B is where it starts
# E is where it ends
# S is how much it jumps
example_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(example_list[1:5:1])     # start:end:steps

print(example_list[0:5:2])



# Dictionaries!
# we need to know where our crazy landlords live. we need more info
# introducing.. dictionaries

# dictionaries are organised using key:value pairs like a real dictionary
# If you want to look up 'omnipresent', you don't start reading the dictionary
# 'A' to 'O'

# Syntax
my_dictionary = {
    'key': 'value',
    'other_key': 'values'
}

# create one dictionary
my_crazy_landlords = {
    'Name': 'Charlie',
    'Phone': '07949053978'
}

# create one key value pair:
my_crazy_landlords['Address'] = 'Nottingham, England'
# read all data of dictionary
print(my_crazy_landlords)
# read one entry in a dictionary (read value of one key)
print(my_crazy_landlords['Phone'])
# update the value in a key
my_crazy_landlords['Phone'] = '079999999'
print(my_crazy_landlords)

# destroy one key value pair
my_crazy_landlords.pop('Address')
print(my_crazy_landlords)

# Getting all the keys out
keys = my_crazy_landlords.keys()
print(keys)

# Getting all the values out
values = my_crazy_landlords.values()
print(values)