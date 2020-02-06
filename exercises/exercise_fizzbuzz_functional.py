from time import sleep

def check(checknum):
    return(checknum % 3 == 0)

def check2(checknum2):
    return(checknum2 % 15 == 0)

def check3(checknum3):
    return(checknum3 % 5 == 0)

while True:
    num = int(input('Please input your number (type 0000 to end the game):    '))
    count_num = 1

    if num == 0000:
        break

    while num >= count_num:
            if check2(count_num):
                print('Fizzbuzz')
                sleep(0.1)

            elif check(count_num):
                print('Fizz')
                sleep(0.1)

            elif check3(count_num):
                print('Buzz')
                sleep(0.1)

            else:
                print(count_num)
                sleep(0.1)
            count_num += 1
