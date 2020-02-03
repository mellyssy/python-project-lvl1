from brain_games.cli import run
from ..games.interface import game_run


def main():
    name = run("Find the greatest common divisor of given numbers.")
    game_run(name, "gcd")


if __name__ == "__main__":
    main()
