from brain_games.cli import run
from ..games.interface import game_run


def main():
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?')
    print()
    name = run()
    game_run(name, 'calc')


if __name__ == '__main__':
    main()
