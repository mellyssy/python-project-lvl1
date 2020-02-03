from random import randint, choice
from operator import add, sub, mul
from .. import cli

RULES = "What is the result of the expression?"
OPERATIONS = [("+", add), ("-", sub), ("*", mul)]


def run_game():
    a = randint(1, 100)
    b = randint(1, 100)

    operator, func = choice(OPERATIONS)

    question = f"{a} {operator} {b}"

    output = cli.get_answer(question)

    correct = func(a, b)

    return (output, str(correct))
