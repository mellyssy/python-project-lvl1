from .. import cli
from random import randint

RULES = "What number is missing in the progression?"

def generate_progression():
    start = randint(1, 100)
    step = randint(1, 10)

    res = [start]

    for i in range(1, 10):
        elem = res[i - 1] + step
        res.append(elem)

    return res


def run_game():
    ap_lst = generate_progression()
    ind = randint(0, 9)
    question = ""

    for i in range(len(ap_lst)):
        if i == ind:
            question += ".. "
        else:
            question = question + str(ap_lst[i]) + " "

    output = cli.get_answer(question.rstrip())
    correct = ap_lst[ind]

    return (output, str(correct))
