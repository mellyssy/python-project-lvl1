import prompt


def run():
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def get_num(num):
    print(f"Question: {num}")
    answer = prompt.string("Your answer: ")
    return answer


def main():
    run()
    get_num()


if __name__ == "__main__":
    main()
