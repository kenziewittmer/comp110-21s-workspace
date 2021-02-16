"""A vaccination calculator."""

__author__ = "730405231"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: int = int(input("What is the population? "))
administered: int = int(input("How many doses have already been administered? "))
per_day: int = int(input("How many doses are being administered per day? "))
target: int = int(input("What is the target percent of the population that you want to be vaccinated? "))

vaccines_needed: int = int((population * 2) * (target / 100) - administered)
days_left: int = vaccines_needed // per_day

today: datetime = datetime.today()
days_to_goal: timedelta = timedelta(days_left)
date_reach_goal: datetime = today + days_to_goal

final_date: str = date_reach_goal.strftime("%B %d, %Y")
days_left: str = str(int(days_left))
target: str = str(target)

print("We will reach " + target + "% vaccination in " + days_left + " days, which falls on " + final_date + ".")