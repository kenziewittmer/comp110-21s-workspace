"""Some examples of list concepts."""

rolls: list[int] # Declare a variable whose type is list of ints

rolls = [2, 3, 2, 6] # Initialize with list literal syntax

print(f"Length of rolls is {len(rolls)}")
print(f"The last item in the list is {rolls[len(rolls)-1]}")

from random import randint
rolls.append(randint(1, 6)) # List's append method adds to the end of a list
print(rolls)

rolls.pop() # List's pop method, w/ no argument, removes the last item of the list
rolls.pop()
print(rolls)

words: list[str] = list() # Construct an empty list using the list constructor
words.append("Hello")
words.append("Goodbye")
print(words)

words.pop(0) # List's pop method, with one argument, pops a specific index
print(words)