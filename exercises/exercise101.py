# create a little program that asks the user for the following details:
# name, height, favourite colour, a secret

print('Hello there! What is your name?')
name = input()

print(f'{name} is a great name! Now what is your height in cm?')
height = input()

print('Cool, now what is your favourite colour?')
colour = input()

print(f'Finally {name}, what is your secret number?')
secret = input()

print(f'Your name is {name}, your height is {height}, your favourite colour is {colour}, and your secret number is {secret}.')