"""Project 1: Choose Your Own Adventure!"""

from random import randint

__author__: str = "730405231"

player: str = ""
points: int = 0
pet: str = ""
SNAKE: str = "\U0001F40D"
HEART: str = "\U0001F49E"
HAND: str = "\U0001F92D"
CELEBRATE: str = "\U0001F973"
WAVE: str = "\U0001F44B"
SMILE: str = "\U0001F60A"
MONEY_EYES: str = "\U0001F911"
STAR: str = "\U0001F929"
GLASSES: str = "\U0001F60E"
SHOCK: str = "\U0001F631"
ZZZ: str = "\U0001F4A4"
SLEEP_EMOJI: str = "\U0001F634"
MOUSE: str = "\U0001F42D"
COWBOY: str = "\U0001F920"
BRITNEY: str = "\U0001F483"
BOOT: str = "\U0001F97E"
BIRD: str = "\U0001F99C"
HUNDRED: str = "\U0001F4AF"


def main() -> None:
    """Entrypoint to the game."""
    greet()
    loop_q: str = input("Can I help you? (yes/no) \n")
    while loop_q == "yes":
        choice_1: str = str(input("Would you like to adopt, donate, or leave the game? \n"))
        if choice_1 == "adopt":
            adoption()
            go_home()
        if choice_1 == "donate":
            global points
            points = donation(points)
            go_home()
        if choice_1 == "leave the game":
            game_over()
        input()
        print(f"You've earned {points} points so far! Great job.")
        loop_q = input("Good morning! Would you like to return to the rescue? \n")
    print(f"Okay! It was so nice to meet you, {player}.")
    game_over()


def greet() -> None:
    """Welcomes player to the game and gives instructions."""
    print(f"Welcome to Wittmer Python Facility! {WAVE} {SNAKE}")
    global player
    player = input("What's your name? \n")
    print(f"Hi {player}, nice to meet you! {SMILE}")


def adoption() -> None:
    """Where the player can adopt a python!"""
    print(f"+{HUNDRED} points!")
    global points
    points += 100
    print(f"It's wonderful that you're looking to adopt, {player}! {MONEY_EYES}")
    input()
    view_snakes: str = input("Would you like to see what we have available? (yes/no) \n")
    if view_snakes == "yes":
        print("+20 points!")
        points += 20
        print(stock())
        global pet
        pet = input("Which python would you like to adopt? Malbolge, Java, or C? \n")
        print("+150 points!")
        points = points + 150
        print(f"That's amazing, {player}! You and {pet} are going to be best friends forever! {SNAKE} {HEART}")
        input()
    else:
        print(f"Aww, that's a bummer, {player}, but don't worry. Check us out online at WittmerPythons.com.")


def donation(point_param: int) -> int:
    """Where the player can donate to the Wittmer Python Facility."""
    print("+50 points!")
    point_param += 50
    if point_param > 50:
        print(f"Welcome back, {player}! You're so kind to continue supporting this establishment.")
        input()
        print("We'd like to honor you by naming you patron of the week!")
        print("To reward for your patronage, we'll double your point total, plus one point per dollar you donate!")
        input()
        donation_quant: int = int(input("How much would you like to donate? \n $"))
        print("You're so generous! Thank you very much.")
        input()
        input("Please type your full name here to e-sign the check. \n")
        print(f"Thanks, {player}.")
        print(f"+{point_param + donation_quant + 50} points!")
        point_param = point_param * 2 + donation_quant
    else:
        print(f"Wow, {player}, that's so kind of you to donate to our nonprofit! {MONEY_EYES}")
        input()
        donation_quant = int(input("How much would you like to donate? \n $"))
        print(f"+{donation_quant} points!")
        print("You're so generous! Thank you very much.")
        input()
        input("Please type your full name here to e-sign the check. \n")
        print("Thanks again!")
        point_param += donation_quant
    return point_param


def stock() -> str:
    """Function which can be updated based on availability at Wittmer Python Facility."""
    Malbolge: str = f"Malbolge is a 22 year old reticulated python, so his care is pretty challenging. {HAND} \n"
    Java: str = f"Java is a green tree python great for intermediate-level snake owners. {GLASSES} \n"
    Cici: str = f"Cici, or C for short, is a ball python--one of the best kinds of snake for beginners. {STAR}"
    stock: str = f"We have three snakes available today: \n {Malbolge} {Java} Lastly, {Cici}"
    return stock


def go_home() -> None:
    """Gives players options once they have completed the first round."""
    print(f"You're home now! You've earned {points} points today. \nGreat job! {CELEBRATE}")
    input()
    if pet != "":
        print(f"Now, you can play with {pet} or go to sleep.")
        home_decision: str = input("Which would you like to do? \n")
        if home_decision == f"play with {pet}":
            play()
            input()
            print(f"That was fun, but now {pet} is exhausted. I think it's time to sleep. {ZZZ}")
            input()
            sleep()
        if home_decision == "go to sleep":
            sleep()
    else:
        print("It's been a long day. Time to sleep!")
        input()
        print("Goodnight!")


def play() -> None:
    """Function that allows interaction with the adopted python."""
    print("+20 points!")
    global points
    points += 20
    a: str = f"You feed your snake a mouse (yuck!) {MOUSE}"
    b: str = f"You crochet your snake a little cap {COWBOY}"
    c: str = f"You wear your snake as a necklace and people think you are Britney Spears {BRITNEY}"
    d: str = f"You put your snake in a boot and say 'There's a snake in my boot!' {BOOT}"
    e: str = f"You introduce your snake to your pet bird, and they become friends. {BIRD}"
    games: list[str]
    games = [a, b, c, d, e]
    print(a)
    while input("Do you want to play again? (yes/no) \n") == "yes":
        print("+20 points!")
        points += 20
        print(games[randint(0, 4)])


def sleep() -> None:
    """A fun ending to the program!"""
    print("+20 points! Sleep is important.")
    global points
    points += 20
    print(f"Sweet dreams... {ZZZ}")
    input()
    print("click.")
    input()
    print("click click.")
    input()
    print("click click click.")
    while input("Do you want to figure out what the noise is? (yes/no) \n") == "no":
        print("Okay.")
        input()
        print("click.")
        input()
        print("click click.")
        input()
        print("click click click.")
    print(f"+{HUNDRED} points")
    points += 100
    print(f"You notice {pet} is not in their cage.")
    input()
    print("The noise is coming from your office, so you open the door...")
    lines_code: int = randint(50, 500)
    input()
    print(f"There, you see {pet} on your laptop.")
    input()
    print(f"And on your laptop, in VSCode, {pet} has written {lines_code} lines of code! {SHOCK}")
    print(f"You have a PYTHON-CODING PYTHON! {SNAKE} {GLASSES}")
    input()
    

def game_over() -> None:
    """Ends game and returns point total."""
    print(f"Game over! You earned {points} points. Not too shabby!")
    exit()


if __name__ == "__main__":
    main()