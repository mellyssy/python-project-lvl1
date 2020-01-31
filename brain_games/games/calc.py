from .. import cli
from random import randint, choice


def calc():
    operators = ['+', '-', '*']

    a = randint(1, 100)
    b = randint(1, 100)

    operator = choice(operators)

    question = f'{a} {operator} {b}'

    output = int(cli.get_num(question))
    correct = eval(question)

    return {
        'output': output,
        'correct': correct
    }


if __name__ == '__main__':
    calc()
