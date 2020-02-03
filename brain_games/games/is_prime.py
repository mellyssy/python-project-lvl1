from .. import cli
from random import randint
import math

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    mx = math.sqrt(num)

    i = 2
    while i <= mx:
        if num % i == 0:
            return "no"
        else:
            i += 1
    else:
        return "yes"


def run_game():
    n = randint(0, 100)

    output = cli.get_answer(f"{n}")
    prime = is_prime(n)

    return (output, prime)
