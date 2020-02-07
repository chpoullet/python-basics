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
    response = input("Speak to Mr. Miyagi. You can exit by saying 'Sensei, I am at peace':    ").lower().strip()  # user response

    if response.find('sensei') == -1:
        print('You are smart, but not wise - address me as Sensei please')   # checks to see if sentence begins with 'Sensei'

    elif 'block' in response:
        print('Remember, best block, not to be there.')     # if block or blocking in response, a specific reply is given

    elif response == 'sensei, i am at peace':
        print('Sometimes, what heart know, head forget')   # user response breaks the loop
        break

    elif response[-1] == '?':
        print('Questions are wise, but for now. Wax on, and Wax off!')   # if sentence ends in '?', a specific reply is given

    else:
        print("Do not lose focus. Wax on. Wax off.")

