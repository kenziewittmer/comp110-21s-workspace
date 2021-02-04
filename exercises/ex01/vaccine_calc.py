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

need_vaccine: int = population - administered
days_total: int = need_vaccine // per_day
days_to_goal_int: int = int(days_total * (target / 100))

today: datetime = datetime.today()
days_to_goal_time: timedelta = timedelta(days_to_goal_int)
date_reach_goal: datetime = today + days_to_goal_time


print("We will reach " + str(target) + "% vaccination in " + str(days_to_goal_int) + " days, which falls on " + date_reach_goal.strftime("%B %d, %Y") + ".")

