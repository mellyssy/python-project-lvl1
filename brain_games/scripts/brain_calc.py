from brain_games.cli import run
from ..games.interface import game_run


def main():
    name = run("What is the result of the expression?")
    game_run(name, "calc")


if __name__ == "__main__":
    main()
