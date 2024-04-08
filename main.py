"""Dice Simulation

Dice Rolling Simulator is a basic cube that creates a random number when a
user rolls it.

"""

import random
import sys
import time

typing_speed = 500 #wpm

def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)

diceStyle = input("What style do you want (numbers, () - parenthesis)?\n")
while True:
    isRoll = input("1 - To roll\n2 - Exit\nEnter: ")

    if isRoll == '1':
        x = random.randint(1, 6)

        if diceStyle == 'numbers':
            if x == 1:
                slow_type("\n -------\n|       |\n|   1   |\n|       |\n -------\n")
            elif x == 2:
                slow_type("\n -------\n| 2     |\n|       |\n|     2 |\n -------\n")
            elif x == 3:
                slow_type("\n -------\n| 3     |\n|   3   |\n|     3 |\n -------\n")
            elif x == 4:
                slow_type("\n -------\n| 4   4 |\n|       |\n| 4   4 |\n -------\n")
            elif x == 5:
                slow_type("\n -------\n| 5   5 |\n|   5   |\n| 5   5 |\n -------\n")
            elif x == 6:
                slow_type("\n -------\n| 6   6 |\n| 6   6 |\n| 6   6 |\n -------\n")
        elif diceStyle == '()' or diceStyle == "parenthesis":
            if x == 1:
                slow_type("\n --------\n|        |\n|   ()   |\n|        |\n --------\n")
            elif x == 2:
                slow_type("\n --------\n| ()     |\n|        |\n|     () |\n --------\n")
            elif x == 3:
                slow_type("\n --------\n| ()     |\n|   ()   |\n|     () |\n --------\n")
            elif x == 4:
                slow_type("\n --------\n| ()  () |\n|        |\n| ()  () |\n --------\n")
            elif x == 5:
                slow_type("\n --------\n| ()  () |\n|   ()   |\n| ()  () |\n --------\n")
            elif x == 6:
                slow_type("\n --------\n| ()  () |\n| ()  () |\n| ()  () |\n --------\n")
    else:
        break
