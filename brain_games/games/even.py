from random import randint
from .. import cli


def even():
    question = randint(1, 100)
    output = cli.get_answer(question)

    if question % 2 == 0:
        is_even = "yes"
    else:
        is_even = "no"

    return (output, is_even)


if __name__ == "__main__":
    even()
