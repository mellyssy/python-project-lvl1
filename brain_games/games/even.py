from random import randint
from .. import cli

RULES = 'Answer "yes" if number even otherwise answer "no".'


def run_game():
    question = randint(1, 100)
    output = cli.get_answer(question)

    if question % 2 == 0:
        is_even = "yes"
    else:
        is_even = "no"

    return (output, is_even)
