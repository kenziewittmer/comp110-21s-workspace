"""An exercise in remainders and boolean logic."""

__author__ = "730405231"

number: int = int(input("Please enter a number: "))
remainder_2: int = number % 2
remainder_7: int = number % 7

if remainder_2 == 0:
    if remainder_7 == 0:
        print("TAR HEELS")
    else:
        print("TAR")
else:
    if remainder_7 == 0:
        print("HEELS")
