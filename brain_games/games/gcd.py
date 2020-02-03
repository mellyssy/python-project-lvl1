from .. import cli
from random import randint

RULES = "Find the greatest common divisor of given numbers."


def run_game():
    a = randint(1, 100)
    b = randint(1, 100)

    question = f"{a} {b}"
    output = cli.get_answer(question)

    if a == b:
        return (output, a)

    if a < b:
        b, a = a, b

    remainder = a % b

    if remainder == 0:
        return (output, b)

    while remainder != 0:
        remainder = a % b
        a, b = b, remainder

    return (output, str(a))
