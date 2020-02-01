from .calc import calc
from .even import even
from .gcd import gcd


def game_run(player_name, game_name):
    score = 0

    while score < 3:

        if game_name == "calc":
            res = calc()
        elif game_name == "even":
            res = even()
        elif game_name == "gcd":
            res = gcd()

        if res[0] == res[1]:
            print("Correct")
            score += 1
        else:
            print(
                f"'{res[0]}' is wrong answer ;(.",
                f"Correct answer was '{res[1]}'.",
            )
            print(f"Let's try again, {player_name}!")
            break
    else:
        print(f"Congratulations, {player_name}!")


if __name__ == "__main__":
    game_run()
