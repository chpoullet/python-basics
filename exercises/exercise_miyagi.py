# mr Miyagi trainee ##projct
# Ask for user input and depending on the response, mr Miyagi will respond.
#
# prompt user for input
# Evaluate each input and print the appropriate responses
# Follow these rules:
#
# every time you ask a question --> Mr. Miyagi responde with
    # --> 'questions are wise, but for now. Wax on, and Wax off!'  (DONE)
# every statement/question must start with Sensei, otherwise:
    # --> 'You are smart, but not wise - address me as Sensei please' (DONE)
# every time you mention 'block' or 'blocking' --> Mr. Miyagi responde with
    # --> 'Remeber, best block, not to be there..' (DONE)
# anything else you say:
    # --> 'do not lose focus. Wax on. Wax off.' (DONE)

# Make it so you keep playing until we say: 'Sensei, I am at peace'
    # --> 'Sometimes, what heart know, head forget' (DONE)

while True:
    question = input("Ask Mr. Miyagi a question:    ").lower().strip()

    if question.find('sensei') == -1:
        print('You are smart, but not wise - address me as Sensei please')

    elif 'block' in question or 'blocking' in question:
        print('Remember, best block, not to be there.')

    elif question == 'sensei, i am at peace':
        print('Sometimes, what heart know, head forget')
        break

    elif question[-1] == '?':
        print('Questions are wise, but for now. Wax on, and Wax off!')

    else:
        print("Do not lose focus. Wax on. Wax off.")
