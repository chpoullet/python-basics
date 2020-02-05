student1 = {
    'name': 'Morty',
    'stream': 'universal quest',
    'grade': 12
}

student2 = {
    'name': 'Summer',
    'stream': 'Terrestrial Quest',
    'grade': 20
}

# List of dictionaries
students_list = [student1, student2]

print(students_list[0]) # only gives you student one
print(students_list) # gives you both students

# Nested dictionary of dictionaries
students_dict = {
    'student1': student1,
    'student2': student2
}

# Use the list to print the individual student names
print(student1['name']) # when taking from a list only need one []
print(student2['name'])

# Use the dictionary to print individual student names
print(students_dict['student1']['name']) # from a dictionary you need two []
print(students_dict['student2']['name'])

