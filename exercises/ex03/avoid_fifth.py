"""EX03 - avoid_fifth function."""

__author__: str = "730405231"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("hello there"))


def avoid_fifth(arg: str) -> str:
    """Removes any E's or e's from a string"""
    i: int = 0
    length: int = len(arg)
    phras: str = ""
    while i < length:
        if arg[i] != "e":
            if arg[i] != "E":
                phras += arg[i]
    return phras


if __name__ == "__main__":
    main()