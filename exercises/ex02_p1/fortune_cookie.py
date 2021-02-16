"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730405231"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())


def fortune_cookie() -> str:
    """Hear your fortune from the all knowing fortune teller!"""
    all_knowing_fortune_teller: int = randint(1, 4)
    if all_knowing_fortune_teller < 2:
        return "This too shall pass."
    else:
        if all_knowing_fortune_teller < 3:
            return "You must make yourself your first priority."
        else:
            if all_knowing_fortune_teller < 4:
                return "Every step you take is a step towards progress."
            else:
                if all_knowing_fortune_teller < 5:
                    return "Choose happiness."


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
