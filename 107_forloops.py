import time
# for loops
# iterations

# syntax

# for <placeholder> in <iterable>:
    # block of code
    # indented lines are part of this block

cars = ['Skoda Felicia Fun', 'Mustang Boss 429', 'Fiat 500', 'Jaguar 420G', 'Aston Martin Vanquish']

#for car in cars:
 #   print(car)
  #  time.sleep(1)   # prints each one every second (needs import time)

# interating over a Dictionary

student1 = {
    'name': 'Arya Stark',
    'stream': 'Many Faces',
    'grade': '10'
}

#for key in student1:
 #   print(key) # this prints the keys
  #  print(student1) # this prints the dictionary
   # print(student1[key])  # this prints the values (dictionary + keys)
   # print(value, student1[value]) # this prints key + value

    # because it's a for loop it will print them out in order, that's why the dictionary is printed out 3 times


#iterate over student1
# get output for name is arya stark
# stream is many faces

for value in student1:
    print(f'{value} is {student1[value]}')   # this prints the key + 'is' + value

