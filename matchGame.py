'''William Soccorsi
Django Bootcamp Python Game
April 27th 2019
'''
import random
digits = list(range(10))
random.shuffle(digits)
#print(digits[:3])

position = ((0, digits[0]), (1, digits[1]), (2, digits[2]))
#print(position)


# https://www.geeksforgeeks.org/python-convert-a-list-of-multiple-integers-into-a-single-integer/
# iterating each element
def convert(list):
    # Converting integer list to string list
    s = [str(i) for i in list]

    # Join list items using join()
    res = int("".join(s))

    return (res)


check1 = convert(digits[:3])






end = False

while end==False:

    # https://stackoverflow.com/questions/13905936/converting-integer-to-digit-list
    guess = input("What is your guess? ")
    check2 = guess
    guess = map(int, str(guess))
    print("You Guessed: " + str(guess))


    for i in range(len(digits[:3])):
        if end == True:
            break
        for index, value in position:

            if (check1 == check2):
                print("Perfect Guess Good Job!")
                end = True
                break


            if (i == index and guess[i] == value):
                print("Match: You've guessed a correct number in the correct position")
            elif (i != index and guess[i] == value):
                print("Close: You've guessed a correct number but in the wrong position")


    # if (i == guess[i]):



# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
