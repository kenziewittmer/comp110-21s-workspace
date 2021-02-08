"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730405231"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

all_knowing_fortune_teller: int = randint(1, 4)

print("Your fortune cookie says...")

if all_knowing_fortune_teller == 1:
    print("You are going to get a 4.0 GPA this semester.")
else:
    if all_knowing_fortune_teller == 2:
        print("You are on the right path.")
    else:
        if all_knowing_fortune_teller == 3:
            print("You have already met your greatest love.")
        else:
            print("A big change is coming, but it will be for the better.")

print("Now, go spread positive vibes!")


