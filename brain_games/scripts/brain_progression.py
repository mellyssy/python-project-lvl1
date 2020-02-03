from brain_games.cli import run
from ..games.interface import game_run


def main():
    name = run("What number is missing in the progression?")
    game_run(name, "progression")


if __name__ == "__main__":
    main()
