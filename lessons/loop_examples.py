"""Examples using loops."""

count: int = 0
while input("Do you need more love? yes/no - ") == "yes":
    # Body block of the while block is evaluated
    # when the test expression is true
    print("I love you!")
    count += 1
    print(f"Count is {count}")

# Iterating a specific number of times
i: int = 0 # i is short for index
iterations: int = 1000000
while i < iterations:
    if  i % 1000 == 0:
        print(f"I love you! i: {i}")
    i += 1 # Important that this increment is not in the if statement to prevent infinite loops

print("Have a lovely day.")