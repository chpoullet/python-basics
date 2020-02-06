# Nested loops

# Looping over embedded lists

normal_list = [1, 2, 3, 4, 5]
embedded_list = [[1, 2, 3], [4, 5, 6]]

# for num in normal_list:
 #   print(num * 5)          # for x in normal_list, * by 5


# for number in embedded_list:
#     print(number)
#     for num in number:
#         print(num)

dict_data = {1: {'name': 'Stanley Ho', 'money': '$0.05'},
             2: {'name': 'Jeff Bezos', 'money': '$0.08'},
             3: {'name': 'Trump', 'money': '$0.02'}}


#print(dict_data[1]['name']) # prints name from 1)

# objective
# --> name
# --> money*4000000

for key_dict1 in dict_data:
    print(key_dict1) # prints the key (1, 2, 3)
    print(dict_data[key_dict1]) # prints the different dictionaries
    sub_dict = dict_data[key_dict1] # this assigns sub_dict as different dictionaries
    print(sub_dict) # this prints dict_data[key_dict1]
    money_var = float(sub_dict['money'].replace('$', ''))
    money_var = money_var * 4000000
    money_string = str(money_var)
    print('$' + money_string)
