from brain_games.cli import run
from ..games.interface import game_run


def main():
    name = run('Answer "yes" if number even otherwise answer "no".')
    game_run(name, "even")


if __name__ == "__main__":
    main()
