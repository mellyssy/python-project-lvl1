from random import randint, choice
from operator import add, sub, mul
from .. import cli

RULES = "What is the result of the expression?"

def run_game():
    operations = [("+", add), ("-", sub), ("*", mul)]

    a = randint(1, 100)
    b = randint(1, 100)

    operator, func = choice(operations)

    question = f"{a} {operator} {b}"
    
    output = cli.get_answer(question)

    correct = func(a, b)

    return (output, str(correct))