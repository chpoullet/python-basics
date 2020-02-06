import time
# while loops

# while loops will continue until the condition/requirement has been fulfilled

# syntax

# while <condition>:
    # run block of code
    # block of code
    # something here that might alter the condition

counter = 5

# while 10 >= counter:
#     print(counter)
#     print('now increasing counter')
#     counter = counter + 1
#     time.sleep(1)

# syntax and patterns for while loops

# while True:
    # block of code
    # control flow
    # if <condition>:
        # break

# The game Fizz AND Buzz!
# multiple of 3 are POP
# multiple of 5 are TOC
# multiples of 3 and 5 are FizzBuzz
# as a user I should be ask for a number,
 # so that I can play the game with my input
# As a player, I should see the game counting up to my number and
 # substituting the multiples of 3 and 5 with the appropriate values,
 # So that I can see if it is working
## EXTRA TASK!
# As a player, I should be able to exit the game using a key word,
  # so that I can stop playing
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
                time.sleep(0.1)

            elif check(count_num):
                print('Fizz')
                time.sleep(0.1)

            elif check3(count_num):
                print('Buzz')
                time.sleep(0.1)

            else:
                print(count_num)
                time.sleep(0.1)
            count_num += 1
