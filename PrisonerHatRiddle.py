"""
Prisoner Hat Riddle

Titus Dillon

Implementation of the prisoner hat riddle

Problem Source: http://ed.ted.com/lessons/can-you-solve-the-prisoner-hat-riddle-alex-gendler
"""

import random

# Counts a specific type of hat
def hatCounter(hats, hatType):

    count = 0

    for hat in hats:
        if (hat == hatType):
            count += 1

    return count

# Provides random hats
def stockHats(numberOfHats):

    hats = []
    choices = ["W","B"]

    for i in range(numberOfHats):
        hats.append(choices[random.randint(0,1)])

    return hats
        
def guess(hats):

    hatGuesses = []

    for guessPosition in range(len(hats)):

        # Person can only see hats in front of them
        hatTypeCount = hatCounter(hats[guessPosition+1:], "B")

        # Establishes the initial parity of black hats
        if guessPosition == 0:
            if (hatTypeCount % 2 == 1):
                hatGuesses.append("B")
                parity = 1
            else:
                hatGuesses.append("W")
                parity = 0

        # Number of black hats seen matches parity
        elif hatTypeCount % 2 == 0 and parity == 0:
            hatGuesses.append("W")
            parity = 0

        # Number of black hats seen does not match parity
        elif hatTypeCount % 2 == 0 and parity == 1:
            hatGuesses.append("B")
            parity = 0

        # Number of black hats seen does not match parity
        elif hatTypeCount % 2 == 1 and parity == 0:
            hatGuesses.append("B")
            parity = 1
            
        # Number of black hats seen matches parity
        elif hatTypeCount % 2 == 1 and parity == 1:
            hatGuesses.append("W")
            parity = 1
        
    return hatGuesses
        
hats = stockHats(10)
guesses = guess(hats)
print("Original:\t" + str(hats))
print("Guesses:\t" + str(guesses))
