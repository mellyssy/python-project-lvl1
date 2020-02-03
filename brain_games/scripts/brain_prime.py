from brain_games.cli import run
from ..games.interface import game_run


def main():
    name = run('Answer "yes" if given number is prime. Otherwise answer "no".')
    game_run(name, "is-prime")


if __name__ == "__main__":
    main()
