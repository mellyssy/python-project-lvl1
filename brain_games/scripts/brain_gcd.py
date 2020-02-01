from brain_games.cli import run
from ..games.interface import game_run


def main():
    print("Welcome to the Brain Games!")
    print("Find the greatest common divisor of given numbers.")
    print()
    name = run()
    game_run(name, "gcd")


if __name__ == "__main__":
    main()
