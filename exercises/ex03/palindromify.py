"""EX03 - palindromify function."""

__author__: str = "730405231"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("han", True))
    print(palindromify("live on time ", False))


def palindromify(phrase: str, even: bool) -> str:
    """Returns an even or odd palindrome given the first half."""
    i: int = 0
    phrase_list: list[str] = []
    length: int = len(phrase)
    if even is True:
        while i < len(phrase):
            phrase_list.append(phrase[i])
            i += 1
        i = 0
        while len(phrase_list) > 0:
            phrase += phrase_list[len(phrase_list)-1]
            phrase_list.pop()
        return phrase
    else:
        while i < len(phrase):
            phrase_list.append(phrase[i])
            i += 1
        i = 0
        phrase_list.pop()
        while len(phrase_list) > 0:
            phrase += phrase_list[len(phrase_list) - 1]
            phrase_list.pop()
        return phrase


if __name__ == "__main__":
    main()