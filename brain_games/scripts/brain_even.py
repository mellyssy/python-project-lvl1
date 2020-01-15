from brain_games.cli import run
from brain_games.even import even


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    print()
    name = run()
    even(name)


if __name__ == '__main__':
    main()
