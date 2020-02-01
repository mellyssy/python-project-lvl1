from .. import cli
from random import randint


def generate_progression():
    start = randint(1, 100)
    step = randint(1, 10)

    res = [start]

    for i in range(1, 10):
        elem = res[i - 1] + step
        res.append(elem)

    return res


def progression():
    ap_lst = generate_progression()
    ind = randint(0, 9)
    question = ""

    for i in range(len(ap_lst)):
        if i == ind:
            question += ".. "
        else:
            question = question + str(ap_lst[i]) + " "

    output = int(cli.get_num(question.rstrip()))
    correct = ap_lst[ind]

    return (output, correct)


if __name__ == "__main__":
    progression()
