from brain_games.cli import run
from ..games.interface import game_run


def main():
    print("Welcome to the Brain Games!")
    print('Answer "yes" if number even otherwise answer "no".')
    print()
    name = run()
    game_run(name, "even")


if __name__ == "__main__":
    main()
