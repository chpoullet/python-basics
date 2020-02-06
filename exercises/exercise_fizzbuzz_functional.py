from time import sleep

def check(checknum):
    return(checknum % 15 == 0)

def check2(checknum):
    return(checknum % 3 == 0)

def check3(checknum):
    return(checknum % 5 == 0)

while True:
    num = int(input('Please input your number (type 0000 to end the game):    '))
    count_num = 1       # counter starts from 1

    if num == 0000:    # if the user types 0000, process stops
        break

    while num >= count_num:   # while the user input number is greater than or equal to count_num,
                              # the while loop will run

        if check(count_num):
                print('Fizzbuzz')
                sleep(0.1)

        elif check2(count_num):
                print('Fizz')
                sleep(0.1)

        elif check3(count_num):
                print('Buzz')
                sleep(0.1)

        else:
                print(count_num)
                sleep(0.1)
        count_num += 1
