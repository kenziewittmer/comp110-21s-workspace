"""Project 1: Choose Your Own Adventure"""

__author__: str = "730405231"

from random import randint

player: str = ""
points: int = 0
pet: str = ""
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
ZZZ_EMOJI: str = "\U0001F4A4"
SLEEP_EMOJI: str = "\U0001F634"
MOUSE_EMOJI: str = "\U0001F42D"
COWBOY: str = "\U0001F920"
BRITNEY: str = "\U0001F483"
BOOT: str = "\U0001F97E"
PET_BIRD: str = "\U0001F99C"
HUNDRED: str = "\U0001F4AF"

print("Welcome.")
print("Before we begin, know that your responses here ARE case-sensitive. When responding with 'yes', please do not capitalize the Y.")
print("Similarly, when you want to complete a task, please repeat it back in the same format.")
print("For example, if I ask, 'Do you want to go to the park or go home?' please respond exactly, 'go to the park' or 'go home'.")
input()


def main() -> None:
    """Entrypoint to the game."""
    greet()
    choice_1: int = input("Would you like to adopt, donate, or learn to code? \n")
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
        choice_2: int = input("Can I help you with anything else? \n")
        if choice_2 == "yes":
            choice_3: int = input("Do you want to adopt or donate? \n")
            if choice_3 == "adopt":
                adoption()
                go_home()
            if choice_3 == "donate":
                donation()
                go_home()
        else:
            print("Sorry to hear that. Have a good one!")
            go_home()


def greet() -> None:
    """Welcomes player to the game and gives instructions"""
    print(f"Hi, welcome to Wittmer Python Facility! {WAVE} {SNAKE_EMOJI}")
    global player
    player = input("What's your name? \n")
    print(f"Hi {player}, nice to meet you! {SMILE}")
    input()


def adoption() -> None:
    """Where the player can adopt a python!"""
    print(f"+{HUNDRED} points")
    global points
    points = points + 100
    print(f"It's wonderful that you're looking to adopt, {player}! {MONEY_EYES}")
    input()
    view_snakes: str = input("Would you like to see what we have available? \n")
    if view_snakes == "yes":
        print(stock())
        input()
        want_to_adopt: str = input("Would you like to adopt one of these snakes? \n")
        if want_to_adopt == "yes":
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
    """Where the player can donate to the Wittmer Python Facility"""
    print("+50 points")
    global points
    points = points + 50
    print(f"Wow, {player}, that's so kind of you to donate to our nonprofit! {MONEY_EYES}")
    input()
    donation_quant: int = int(input("How much would you like to donate? \n $"))
    print("You're so generous! Thank you very much.")
    input()
    input("Please type your full name here to e-sign the check. \n")
    print("Thanks again!")
    points = points + donation_quant
    print(f"+{donation_quant} points")
    

def stock() -> str:
    """Function which can be updated based on availability at Wittmer Python Facility"""
    Malbolge: str = f"Malbolge is a 22 year old reticulated python, so his care is pretty challenging. One might think he was raised to be difficult! {HAND_OVER_FACE} \n"
    Java: str = f"Java is a green tree python great for beginner snake owners, but intermediate owners will enjoy her more. Her care is intuitive, but she prefers structure. {GLASSES} \n"
    Cici: str = f"Cici, or C, for short, is a very simple snake to care for! C is a ball python, which is one of the best kinds of snake for beginners. {STAR_EYES}"
    stock: str = f"We have three snakes available today: \n {Malbolge} {Java} Lastly, {Cici}"
    return stock


def go_home() -> None:
    """Gives players options once they have completed the first round"""
    print(f"You're home now! You've earned {points} points today. Great job! {CELEBRATE_EMOJI}")
    input()
    if pet == "Malbolge":
        print("Now, you can play with Malbolge, return to the rescue, or go to sleep.")
        home_decision: str = input("Which would you like to do? \n")
        if home_decision == "play with Malbolge":
                play()
                input()
                print(f"That was fun, but now Malbolge is exhausted. I think it's time to sleep. {ZZZ_EMOJI}")
                input()
                sleep()
                if home_decision == "return to the rescue":
                    return_to_rescue: str = input(f"Hello again, {player}! Would you like to donate today?")
                    if return_to_rescue == "yes":
                        donation()
                        home()
                    else:
                        print("Alright, bye!")
                        input()
                        print(f"You're very tired, you should get some rest! {ZZZ_EMOJI}")
                        input()
                        sleep()
                if home_decision == "go to sleep":
                    sleep()
    else:
        if pet == "Java":
            print("Now, you can play with Java, return to the rescue, or go to sleep.")
            home_decision: str = input("Which would you like to do? \n")
            if home_decision == "play with Java":
                play()
                input()
                print(f"That was fun, but now Java is exhausted. I think it's time to sleep {ZZZ_EMOJI}")
                input()
                sleep()
                if home_decision == "return to the rescue":
                    return_to_rescue: str = input(f"Hello again, {player}! Would you like to donate today?")
                    if return_to_rescue == "yes":
                        donation()
                        home()
                    else:
                        print("Alright, bye!")
                        input()
                        print(f"You're very tired, you should get some rest! {ZZZ_EMOJI}")
                        input()
                        sleep()
                if home_decision == "go to sleep":
                    sleep()
        else:
            if pet == "C":
                print("Now, you can play with C, return to the rescue, or go to sleep.")
                home_decision: str = input("Which would you like to do? \n")
                if home_decision == "play with C":
                    play()
                    input()
                    print(f"That was fun, but now C is exhausted. I think it's time to sleep {ZZZ_EMOJI}")
                    input()
                    sleep()
                if home_decision == "return to the rescue":
                    return_to_rescue: str = input(f"Hello again, {player}! Would you like to donate today?")
                    if return_to_rescue == "yes":
                        donation()
                        home()
                    else:
                        print("Alright, bye!")
                        input()
                        print("You're very tired, you should get some rest!")
                        input()
                        sleep()
                if home_decision == "go to sleep":
                    sleep()
            else:
                print("Now, you can return to the rescue or go to sleep.")
                home_decision: str = input("Which would you like to do? \n")
                if home_decision == "return to the rescue":
                    main()
                if home_decision == "go to sleep":
                    print("Goodnight!")
                    exit()


def play() -> None:
    """Function that allows interaction with the adopted python"""
    print("+20 points")
    global points
    points += 20
    a: str = f"You feed your snake a mouse (yuck!) {MOUSE_EMOJI}"
    b: str = f"You crochet your snake a little cap {COWBOY}"
    c: str = f"You wear your snake as a necklace and people think you are Britney Spears {BRITNEY}"
    d: str = f"You put your snake in a boot and say 'There's a snake in my boot!' {BOOT}"
    e: str = f"You introduce your snake to your pet bird, and they become friends. {PET_BIRD}"
    generator: int = randint(0, 4)
    games: list[int] = [a, b, c, d, e]
    print(a)
    i: int = 1
    while i < 11:
        while input("Do you want to play again? \n") == "yes":
            print(games[randint(0, 4)])
            i += 1


def sleep() -> None:
    """A fun ending to the program!"""
    print(f"Sweet dreams... {ZZZ_EMOJI}")
    input()
    print("click.")
    input()
    print("click click.")
    input()
    print("click click click.")
    curious_noise: str = input("Do you want to figure out what the noise is? \n")
    if curious_noise == "yes":
        print(f"+{HUNDRED} points")
        global points
        points += 100
        print(f"You notice {pet} is not in their cage.")
        input()
        print(f"The noise is coming from your office, so you open the door...")
        lines_code: int = randint(50, 500)
        input()
        print(f"There, you see {pet} on your laptop.")
        input()
        print(f"And on your laptop, in VSCode, {pet} has written {lines_code} lines of code! {SHOCK_FACE}")
        print(f"You have a PYTHON-CODING PYTHON! {SNAKE_EMOJI} {GLASSES}")
        exit()
    else:
        print(f"Alright, sweet dreams {SLEEP_EMOJI}")
        exit()

if __name__ == "__main__":
    main()