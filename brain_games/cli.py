import prompt


def run(game_intro=""):
    print("Welcome to the Brain Games!")
    if game_intro:
        print(f"{game_intro}")
    print()
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def get_answer(num):
    print(f"Question: {num}")
    answer = prompt.string("Your answer: ")
    return answer


def main():
    run()
    get_answer()


if __name__ == "__main__":
    main()
