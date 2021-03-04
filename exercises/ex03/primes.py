"""EX03 - prime functions."""

__author__: str = "730405231"


def main() -> None:
    """Entrypoint of the program."""
    print(is_prime(77)) 
    print(list_primes(9, 79))


def is_prime(num: int) -> bool:
    """Verifies if a number is prime."""
    divisor: int = 2
    while divisor < num:
        remainder: int = num % divisor
        if remainder == 0:
            return False
        divisor += 1
    return True
        

def list_primes(a: int, b: int) -> list[int]:
    """Lists all prime numbers between a and b."""
    prime_list: list[int] = []
    i: int = 0
    length_ref: int = abs(b - a) + 1
    while i < length_ref:
        if is_prime(a + i):
            prime_list.append(a + i)
        i += 1
    return prime_list


if __name__ == "__main__":
    main()