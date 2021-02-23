"""Project 1: Choose Your Own Adventure"""
__author__: str = "730405231"

from random import randint

player: str = ""
points: int = 0
SNAKE_EMOJI: str = "\U0001F40D"
HEART_EMOJI: str = "\U0001F49E"
HAND_OVER_FACE: str = "\U0001F92D"
CELEBRATE_EMOJI: str = "\U0001F973"
WAVE: str = "\U0001F44B"
SMILE: str = "\U0001F60A"
MONEY_EYES: str = "\U0001F911"
STAR_EYES: str = "\U0001F929"
GLASSES: str = "\U0001F60E"
SHOCK_FACE: str = "\U0001F631"
pet: str = ""


def main() -> None:
    greet()
    choice_1: int = input("Are you here to adopt, donate, or learn to code? \n")
    if choice_1 == "adopt":
        adoption()
        go_home()
    if choice_1 == "donate":
        donation()
        go_home()
    if choice_1 == "learn to code":
        print("+10 points for spirit!")
        global points
        points = points + 10
        print("Sorry, this isn't a coding facility! We are a python rescue. Check out Kris Jordan on Youtube to learn to code!")
        go_home()


def greet() -> None:
    print(f"Hi, welcome to Wittmer Python Facility! {WAVE} {SNAKE_EMOJI}")
    global player
    player = input("What's your name? \n")
    print(f"Hi {player}, nice to meet you! {SMILE}")
    input()


def adoption() -> None:
    print("+100 points")
    global points
    points = points + 100
    print(f"It's wonderful that you're looking to adopt, {player}! {MONEY_EYES}")
    input()
    view_snakes: str = input("Would you like to see what we have available? \n")
    if view_snakes == "yes" or "Yes" or "YES" or "sure" or "Sure" or "SURE" or "yeah" or "Yeah" or "YEAH":
        print(stock())
        input()
        want_to_adopt: str = input("Would you like to adopt one of these snakes? \n")
        if want_to_adopt == "yes" or "Yes" or "YES" or "sure" or "Sure" or "SURE" or "yeah" or "Yeah" or "YEAH":
            print(f"That's wonderful! {CELEBRATE_EMOJI}")
            input()
            global pet
            pet = input("Which python would you like to adopt? Malbolge, Java, or C? \n")
            print("+150 points")
            points = points + 150
            print(f"That's amazing, {player}! You and {pet} are going to be best friends forever! {SNAKE_EMOJI} {HEART_EMOJI}")
            input()
        else:
            print("Sorry to hear that. In a few weeks, we are supposed to get some more pythons. Check back soon!")
    else:
        print(f"Aww, that's a bummer, {player}, but don't worry. Check us out online at WittmerPythons.com.")


def donation() -> None:
    print("+50 points")
    print(f"Wow, {player}, that's so kind of you to donate to our nonprofit! {MONEY_EYES}")
    input()
    donation_quant: int = int(input("How much would you like to donate? \n $"))
    print("You're so generous! Thank you very much.")
    input()
    input("Please type your full name here to e-sign the check. \n")
    print("Thanks again!")
    global points
    points = points + donation_quant
    print(f"+{donation_quant} points")
    

def stock() -> str:
    Malbolge: str = f"Malbolge is a 22 year old reticulated python, so his care is pretty challenging. One might think he was raised to be difficult! {HAND_OVER_FACE} \n"
    Java: str = f"Java is a green tree python great for beginner snake owners, but intermediate owners will enjoy her more. Her care is intuitive, but she prefers structure. {GLASSES} \n"
    Cici: str = f"Cici, or C, for short, is a very simple snake to care for! C is a ball python, which is one of the best kinds of snake for beginners. {STAR_EYES}"
    stock: str = f"We have three snakes available today: \n {Malbolge} {Java} Lastly, {Cici}"
    return stock


def go_home() -> None:
    print(f"You're home now! You've earned {points} points today. Great job!")
    input()
    if pet == "Malbolge" or "Java" or "C":
        print(f"Now, you can interact with {pet}, return to the rescue, or go to sleep.")
        home_decision: str = input("Which would you like to do? \n")
        if home_decision == f"interact with {pet}":
            print(play())
        if home_decision == "return to the rescue" or "return":
            main()
        if home_decision == "go to sleep" or "sleep":
            sleep()
    else:
        print("Now, you can return to the rescue or go to sleep.")
        home_decision: str = input("Which would you like to do? \n")
        if home_decision == "return to the rescue" or "return":
            input()
            main()
        if home_decision == "go to sleep" or "sleep":
            sleep()


def play() -> None:
    print("+20 points")
    a: str = "You feed your snake a mouse (yuck!)"
    b: str = "You crochet your snake a little cap."
    c: str = "You wear your snake as a necklace and people think you are Britney Spears."
    d: str = "You put your snake in a boot and say 'There's a snake in my boot!'"
    e: str = "You introduce your snake to your pet bird, and they become friends."
    generator: int = randint(1, 5)
    if generator > 4:
        return e
    if generator > 3:
        return d
    if generator > 2:
        return c
    if generator > 1:
        return b
    if generator > 0:
        return a


def sleep() -> None:
    print("Sweet dreams...")
    input()
    print("click.")
    input()
    print("click click click.")
    curious_noise: str = input("Do you want to figure out what the noise is? \n")
    if curious_noise == "yes" or "Yes" or "YES" or "sure" or "Sure" or "SURE" or "yeah" or "Yeah" or "YEAH":
        print("+100 points")
        global points
        points = points + 100
        print(f"You notice {pet} is not in their cage.")
        input()
        print(f"The noise is coming from your office, so you open the door...")
        lines_code: int = randint(10, 500)
        input()
        print(f"There, you see {pet} on your laptop.")
        input()
        print(f"And on your laptop, in VSCode, {pet} has written {lines_code} lines of code! {SHOCK_FACE}")
        print(f"You have a PYTHON-CODING PYTHON! {SNAKE_EMOJI} {GLASSES}")
    else:
        print("Alright, sweet dreams.")

if __name__ == "__main__":
    main()