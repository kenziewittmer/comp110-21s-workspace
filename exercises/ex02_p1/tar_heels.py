"""Tar Heels exercise redux as a structured program."""

__author__ = "730405231"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))


def tar_heels(b: int) -> int:
    remainder_7: int = b % 7
    remainder_2: int = b % 2
    if remainder_7 + remainder_2 == 0:
        return "TAR HEELS"
    else:  
        if remainder_7 == 0:
            return "HEELS"
        else:
            if remainder_2 == 0:
                return "TAR"
            else:
                return "CAROLINA"


if __name__ == "__main__":
    main()
