from brain_games.cli import run
from ..games.interface import game_run


def main():
    print("Welcome to the Brain Games!")
    print("What number is missing in the progression?")
    print()
    name = run()
    game_run(name, "progression")


if __name__ == "__main__":
    main()
