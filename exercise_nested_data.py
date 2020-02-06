# define a dictionary with the following keys:

# beginning
# middle
# end
# heroine/hero

# populate the values of the keys, with a story broken into beginning, middle, end.
# use your hero/heroine too

# print the story by calling your dictionary keys individually
defined_name = input("What would you like your hero/heroine's name to be?  ").strip().capitalize()

story = {
    'Beginning': ' you are being chased and reach a door.',
    'Middle': 'The door says "DO NOT ENTER".',
    'End': 'You are caught, game over.',
    'hero': defined_name
}


print(f"{story['hero']}{story['Beginning']}")
print(story['Middle'])


middle_input = input("Do you enter the door? Y/N:  ").strip().upper()
if middle_input == 'Y':
    print('You enter the door and escape.')
else:
    print(story['End'])
