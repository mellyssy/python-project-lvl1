from .. import cli
from random import randint


def even():
    question = randint(1, 100)
    output = cli.get_num(question)

    if question % 2 == 0:
        is_even = 'yes'
    else:
        is_even = 'no'

    return {
        'output': output,
        'correct': is_even
    }


if __name__ == '__main__':
    even()
