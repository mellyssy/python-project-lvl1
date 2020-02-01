from .. import cli
from random import randint


def gcd():
    a = randint(1, 100)
    b = randint(1, 100)

    question = f"{a} {b}"
    output = int(cli.get_num(question))

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

    return (output, a)


if __name__ == "__main__":
    gcd()
