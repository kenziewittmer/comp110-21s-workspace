"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730405231"


def main() -> None: 
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    x: int = days_to_target(population, doses, doses_per_day, target)
    y: str = future_date(x)
    print("We will reach " + str(target) + "% vaccination in " + str(x) + " days, which falls on " + y + ".")


def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int: 
    """Calculates number of days left until target vaccine population is reached!"""
    doses = int(((population * 2) * (target / 100)) - doses)
    a: float = doses / doses_per_day
    b: int = round(a)
    return b


def future_date(number_days: int) -> str: 
    """Converts number of days from today to a future date!"""
    today: datetime = datetime.today()
    days_to_goal: timedelta = timedelta(number_days)
    date_reach_goal: datetime = today + days_to_goal
    final_date: str = date_reach_goal.strftime("%B %d, %Y")
    return final_date


if __name__ == "__main__": 
    main()