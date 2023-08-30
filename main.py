"""Dice Simulation

Dice Rolling Simulator is a basic cube that creates a random number when a
user rolls it.

"""

import random

diceStyle = input("What style do you want (numbers, () - parenthesis)?\n")
while True:
    isRoll = input("1 - To roll\n2 - Exit\nEnter: ")

    if isRoll == '1':
        x = random.randint(1, 6)

        if diceStyle == 'numbers':
            if x == 1:
                print("\n -------\n|       |\n|   1   |\n|       |\n -------\n")
            elif x == 2:
                print("\n -------\n| 2     |\n|       |\n|     2 |\n -------\n")
            elif x == 3:
                print("\n -------\n| 3     |\n|   3   |\n|     3 |\n -------\n")
            elif x == 4:
                print("\n -------\n| 4   4 |\n|       |\n| 4   4 |\n -------\n")
            elif x == 5:
                print("\n -------\n| 5   5 |\n|   5   |\n| 5   5 |\n -------\n")
            elif x == 6:
                print("\n -------\n| 6   6 |\n| 6   6 |\n| 6   6 |\n -------\n")
        elif diceStyle == '()' or diceStyle == "parenthesis":
            if x == 1:
                print("\n --------\n|        |\n|   ()   |\n|        |\n --------\n")
            elif x == 2:
                print("\n --------\n| ()     |\n|        |\n|     () |\n --------\n")
            elif x == 3:
                print("\n --------\n| ()     |\n|   ()   |\n|     () |\n --------\n")
            elif x == 4:
                print("\n --------\n| ()  () |\n|        |\n| ()  () |\n --------\n")
            elif x == 5:
                print("\n --------\n| ()  () |\n|   ()   |\n| ()  () |\n --------\n")
            elif x == 6:
                print("\n --------\n| ()  () |\n| ()  () |\n| ()  () |\n --------\n")
    else:
        break