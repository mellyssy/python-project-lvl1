from .. import cli
from random import randint
import math


def is_prime(num):
    mx = math.sqrt(num)

    i = 2
    while i <= mx:
        if num % i == 0:
            return 'no'
        else:
            i += 1
    else:
        return 'yes'


def get_prime():
    n = randint(0, 100)

    output = cli.get_answer(f'{n}')
    prime = is_prime(n)

    return (output, prime)


if __name__ == "__main__":
    get_prime()
